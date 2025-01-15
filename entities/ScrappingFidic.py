from selenium import webdriver
from selenium.common import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
import time
import zipfile
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, JavascriptException

def realizar_login(url, username, password,nome_fundo,driver):
    driver.get(url + "/login")
    driver.find_element(By.ID, "j_username").send_keys(username)
    driver.find_element(By.ID, "j_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    if(url == "https://portalfidc4.singulare.com.br/portal/login"):
        validacao_fidc4(driver)


def validacao_fidc4(driver):
    label_text = driver.find_element(By.CLASS_NAME, 'control-label').get_attribute('for')

    if label_text.lower() == "sobrenome":
        secret_login = os.getenv("SECRET_SOBRENOME")
    elif label_text.lower() == "datanascimento":
        secret_login = os.getenv("SECRET_NASCIMENTO")
    else:
        secret_login = os.getenv("SECRET_MAE")

    driver.find_element(By.CLASS_NAME, "input-xlarge").send_keys(secret_login)
    driver.find_element(By.ID, "btnValidarDupla").click()

def gerar_relatorio(data, nome_fundo, driver, url):
    driver.get(url + "/reports/estoque")

    # Selecionar o fundo
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.chzn-single.chzn-default"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//ul[contains(@class, 'chzn-results')]//li[contains(text(), '{nome_fundo}')]"))).click

    # Preencher a data
    data_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "data")))
    data_input.clear()
    data_input.send_keys(data)
    driver.find_element(By.TAG_NAME, "body").click()

    try:
        # Tentar localizar o botão CSV com tempo limite
        btn_csv = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "csv")))
        driver.execute_script("arguments[0].click();", btn_csv)
    except TimeoutException:
        print("Botão CSV não encontrado.")
        script = """
        return confirm('O botão CSV não está disponível no momento.');
        """
        try:
            user_response = driver.execute_script(script)
            if not user_response:
                print("Processo interrompido pelo usuário.")
                return
        except Exception as e:
            print(f"Erro ao executar script JavaScript: {e}")
            return

    # Aguarde o download ou prossiga com outras ações
    time.sleep(1)

def baixar_relatorio(driver,nome_fundo):
    driver.get("https://portalfidc3.brltrust.com.br/portal/reports/meusRelatorios")

   # tabela = driver.find_element(By.CLASS_NAME, "table-striped")
    tabela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "table-striped")))
    linhas = tabela.find_elements(By.XPATH, ".//tbody/tr")
    nome_fundo_slice = nome_fundo[:17] + "..."

    for linha in linhas:
        status = linha.find_elements(By.TAG_NAME, "td")[3].text.strip()
        fundo_linha =  linha.find_elements(By.TAG_NAME, "td")[0].text.strip()

        if status == "FINALIZADO" and  nome_fundo_slice == fundo_linha:
            diretorio_download = "C:\\Users\Lucas Martins\\Downloads"
            botao = linha.find_elements(By.TAG_NAME, "td")[4].find_element(By.TAG_NAME, "button")
            acao = ActionChains(driver)
            acao.move_to_element(botao).click().perform()

            # Aguarde o processamento (ajuste o tempo conforme necessário)
            arquivo_baixado = aguardar_download(diretorio_download)
            print(f"Arquivo baixado: {arquivo_baixado}")
            return os.path.join(diretorio_download, arquivo_baixado)

def obter_arquivo_mais_recente(diretorio):
        """Retorna o arquivo mais recente em um diretório."""
        arquivos = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
        if not arquivos:
            raise FileNotFoundError("Nenhum arquivo encontrado no diretório de downloads.")
        arquivo_mais_recente = max(arquivos, key=os.path.getmtime)
        return arquivo_mais_recente


def aguardar_download(diretorio, timeout=60):
    """
    Aguarda o download ser concluído no diretório especificado.

    :param diretorio: Caminho para o diretório de downloads.
    :param timeout: Tempo máximo para aguardar o download (em segundos).
    :return: Nome completo do arquivo baixado (sem a extensão .tmp).
    :raises TimeoutError: Se o download não for concluído dentro do tempo limite.
    """
    tempo_inicial = time.time()
    while True:
        # Obter a lista de arquivos no diretório
        arquivos = os.listdir(diretorio)

        # Filtra arquivos temporários (.tmp) indicando que o download ainda está em andamento
        arquivos_temporarios = [f for f in arquivos if
                                f.endswith('.crdownload') or f.endswith('.part') or f.endswith('.tmp')]

        if not arquivos_temporarios:
            # Não há arquivos temporários, presumimos que o download está completo
            arquivos_completos = [f for f in arquivos if
                                  os.path.isfile(os.path.join(diretorio, f)) and not f.endswith('.tmp')]

            if arquivos_completos:
                # Retorna o caminho completo do arquivo final (sem .tmp)
                arquivo_final = max(arquivos_completos, key=lambda f: os.path.getmtime(os.path.join(diretorio, f)))
                caminho_completo = os.path.join(diretorio, arquivo_final)
                return caminho_completo

        # Verificar se atingiu o tempo limite
        if time.time() - tempo_inicial > timeout:
            raise TimeoutError("O download não foi concluído dentro do tempo limite.")

        # Aguarde um curto intervalo antes de verificar novamente
        time.sleep(1)


def ler_zip(caminho_zip):
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        arquivos_zip = zip_ref.namelist()

        # Procurar pelo CSV
        csv_file = None
        for arquivo in arquivos_zip:
            if arquivo.endswith('.csv'):
                csv_file = arquivo
                break

        if csv_file is None:
            raise ValueError("Nenhum arquivo CSV encontrado no arquivo ZIP.")

        with zip_ref.open(csv_file) as my_file:
            df = pd.read_csv(my_file, encoding = 'ISO-8859-1', on_bad_lines = 'skip', delimiter = ";")
#cp1252
    return df


"""
with zip_file.open(file) as csv_file:
            df = pd.read_csv(
                csv_file,
                sep=";",
                encoding="ISO-8859-1",
            )
 zip_file = zipfile.ZipFile(io.BytesIO(response_zip.content))
 file_names = zip_file.namelist()
import zipfile
import pandas as pd

zip_path = "exemplo.zip"

dataframes = []

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    files_in_zip = zip_ref.namelist()

    csv_files = [file for file in files_in_zip if file.endswith('.csv')]

    for csv_filename in csv_files:
        with zip_ref.open(csv_filename) as csv_file:
            df = pd.read_csv(csv_file)
            dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

print(combined_df)

def gerar_relatorio(data, nome_fundo, driver,url):
    driver.get(url+"/reports/estoque")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.chzn-single.chzn-default"))).click()

    option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//ul[contains(@class, 'chzn-results')]//li[contains(text(), '{nome_fundo}')]")))
    option.click()

    data_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "data")))

    try:
        data_input.clear()
        data_input.send_keys(data)
    except ElementNotInteractableException:
        driver.execute_script("arguments[0].value = arguments[1];", data_input, data)

    body = driver.find_element(By.TAG_NAME, "body")
    body.click()

    btn_csv = driver.find_element(By.ID, "csv")
    driver.execute_script("arguments[0].click();", btn_csv)

    time.sleep(1)

    def gerar_relatorio(data, nome_fundo, driver, url):
        driver.get(url + "/reports/estoque")

        # Selecionar o fundo
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.chzn-single.chzn-default"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//ul[contains(@class, 'chzn-results')]//li[contains(text(), '{nome_fundo}')]"))).click()


        # Preencher a data
        data_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "data")))
        try:
            data_input.clear()
            data_input.send_keys(data)
        except ElementNotInteractableException:
            driver.execute_script("arguments[0].value = arguments[1];", data_input, data)

        # Tirar o foco do campo de data
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Tentar encontrar o botão CSV
        try:
            btn_csv = driver.find_element(By.ID, "csv")
            driver.execute_script("arguments[0].click();", btn_csv)
        except NoSuchElementException:
            # Exibir mensagem no navegador
            script = 
            if (confirm("O botão CSV não está disponível no momento. Deseja continuar o processo mesmo assim?")) {
                return true;
            } else {
                return false;
            }
   
            user_response = driver.execute_script(script)
            if not user_response:
                print("Processo interrompido pelo usuário.")
                return

        # Aguarde o download (ou outro comportamento adicional, se necessário)
        time.sleep(1)



"""