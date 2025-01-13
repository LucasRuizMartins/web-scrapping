import os
import time
from entities.ScrappingFidic3 import *
from services.PostgressService import *
#from entities.ScrappingFidic4 import realizar_login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
import pandas as pd
from io import BytesIO

# Configuração do WebDriver
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

nome_fundo = "CDC EMPRÉSTIMOS FIDC  CLASSE ÚNICA FECHADA"
#nome_fundo = "ENEL2 LEGAL CLAIMS FIDC CLASSE UNICA FECHADA"

data ="08/01/2025"

#FIDIC3
url = "https://portalfidc3.brltrust.com.br/portal/login"
user = os.getenv('LOGIN_FIDC3')
password = os.getenv('SENHA_FIDC3')

#FIDIC4
#url = "https://portalfidc4.singulare.com.br/portal/login"
#user =  os.getenv('LOGIN_FIDC3')
#password =  os.getenv('SENHA_FIDC4')


conn = conectar_postgresql()
#resultados = executar_consulta(conn, "SELECT * FROM tb_teste_estoque_cobuccio",None)
#listar_tabelas(conn)
#print( resultados)



try:

    realizar_login(url,user,password,nome_fundo,driver)
    time.sleep(2)
    gerar_relatorio(data, nome_fundo, driver)
    time.sleep(5)

    path_arq = baixar_relatorio(driver,nome_fundo)
    df = ler_zip(path_arq)
    #df= ler_zip("C:\\Users\Lucas Martins\\Downloads\\57996195000199_Estoque_CDC EMPRÉSTIMOS FIDC  CLASSE ÚNICA FECHADA (17).zip")

    #print("HEAD:\n", df.head())
    #print(f'colunas : {df.shape}')
    #print(df.columns)

    time.sleep(2)

    df['VALOR_PRESENTE'] = df['VALOR_PRESENTE'].str.replace(r'(?<=\d),(?=\d{3}\.)', '', regex=True)
    df['VALOR_PRESENTE'] = pd.to_numeric(df['VALOR_PRESENTE'], errors='coerce')
    df['VALOR_NOMINAL'] = df['VALOR_NOMINAL'].str.replace(r'(?<=\d),(?=\d{3}\.)', '', regex=True)
    df['VALOR_NOMINAL'] = pd.to_numeric(df['VALOR_NOMINAL'], errors='coerce')
    df['VALOR_AQUISICAO'] = df['VALOR_AQUISICAO'].str.replace(r'(?<=\d),(?=\d{3}\.)', '', regex=True)
    df['VALOR_AQUISICAO'] = pd.to_numeric(df['VALOR_AQUISICAO'], errors='coerce')

    #df = pd.DataFrame(data)
    df['DATA_VENCIMENTO_AJUSTADA'] = pd.to_datetime(df['DATA_VENCIMENTO_AJUSTADA'], format='%d/%m/%Y')
    df['DATA_EMISSAO'] = pd.to_datetime(df['DATA_EMISSAO'], format='%d/%m/%Y')
    df['DATA_AQUISICAO'] = pd.to_datetime(df['DATA_AQUISICAO'], format='%d/%m/%Y')
    df['DATA_VENCIMENTO_ORIGINAL'] = pd.to_datetime(df['DATA_VENCIMENTO_ORIGINAL'], format='%d/%m/%Y')
    df['DATA_FUNDO'] = pd.to_datetime(df['DATA_FUNDO'], format='%d/%m/%Y')
    df['DATA_REFERENCIA'] = pd.to_datetime(df['DATA_REFERENCIA'], format='%d/%m/%Y')

    colunas_a_remover = [
        'TAXA_JUROS_VENCIDOS', 'DATA_CARENCIA', 'TAXA_JUROS_INDEXADOR', 'TP_JUROS', 'DEFASAGEM',
        'NOME', 'VALOR_NOMINAL_IOF', 'NU_BANCO_CHEQUE', 'NU_AGENCIA_CHEQUE', 'NU_CONTA_CHEQUE',
        'CMC7_CHEQUE', 'CODIGO_ORIGEM', 'CODIGO_FINALIDADE', 'ID_REGISTRO', 'FAIXA_PDD_GERAL',
        'TIPO_PDD_GERAL', 'VALOR_PDD_GERAL'
    ]

    # Remover as colunas do DataFrame
    df = df.drop(colunas_a_remover, axis=1)
    print(df.columns)
    #inserir_df(conn, df, "tb_cobbucio")
    inserir_df_com_copy(conn,df,"tb_cobbucio")
    #pd.set_option('display.max_columns', None)
    #print(df.head)

    #print(df[['DATA_VENCIMENTO_AJUSTADA', 'DATA_EMISSAO', 'DATA_AQUISICAO', 'DATA_VENCIMENTO_ORIGINAL', 'DATA_FUNDO','DATA_REFERENCIA']].head())

    #print(df.dtypes)

    #soma = df['VALOR_PRESENTE'].sum()
    #print(f"Soma dos valores: {soma}")

finally:
    driver.quit()
    conn.close()
