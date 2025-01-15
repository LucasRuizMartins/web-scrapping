import os
import time
from entities.ScrappingFidic import *
from services.ConversorService import *
from services.dataframeService import gerar_dataframe
from services.PostgressService import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import zipfile
import pandas as pd
from io import BytesIO


# Configuração do WebDriver
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

#nome_fundo = "CDC EMPRÉSTIMOS FIDC  CLASSE ÚNICA FECHADA"
#nome_fundo = "FIDARA FIDC"
#nome_fundo = "ENEL2 LEGAL CLAIMS FIDC CLASSE UNICA FECHADA"

data ="31/12/2024"

#FIDIC3
#url = "https://portalfidc3.brltrust.com.br/portal/login"
#user = os.getenv('LOGIN_FIDC3')
#password = os.getenv('SENHA_FIDC3')

#FIDIC4
#url = "https://portalfidc4.singulare.com.br/portal/"
#user = os.getenv('LOGIN_FIDC4')
#password = os.getenv('SENHA_FIDC4')



#conn = conectar_postgresql()
#resultados = executar_consulta(conn, "SELECT * FROM tb_teste_estoque_cobuccio",None)
#listar_tabelas(conn)
#print( resultados)

try:


    #realizar_login(url, user,password, driver)
    #realizar_login(url,user,password,nome_fundo,driver)
    #time.sleep(2)
    #gerar_relatorio(data, nome_fundo, driver,url)
    #time.sleep(5)

    #path_arq = baixar_relatorio(driver,nome_fundo)
    #df = ler_zip(path_arq)
    #df = gerar_df_multisetorial(path_arq)
    #time.sleep(2)
    #df=gerar_df_multisetorial("C:\\Users\Lucas Martins\\Downloads\\23956882000169_Estoque_SB CREDITO FIDC MULTISSETORIAL (1).zip")
    #df=gerar_df_multisetorial("C:\\Users\Lucas Martins\\Downloads\\50200709000109_Estoque_MOOVPAY FIDC - SUBORDINADA.zip")
    df = gerar_dataframe(r"C:\Users\Lucas Martins\Downloads\50200709000109_Estoque_MOOVPAY FIDC - SUBORDINADA.zip")

    #df = remover_colunas(df)




finally:
    print("fim")
    #driver.quit()
    #conn.close()


#-------------- DELETAR
    #print(df.columns)
    #inserir_df(conn, df, "tb_cobbucio")
    #inserir_df_com_copy(conn,df,"tb_cobbucio")
    #pd.set_option('display.max_columns', None)
    #print(df.head)
    #print(df[['DATA_VENCIMENTO_AJUSTADA', 'DATA_EMISSAO', 'DATA_AQUISICAO', 'DATA_VENCIMENTO_ORIGINAL', 'DATA_FUNDO','DATA_REFERENCIA']].head())
    #print(df.dtypes)

   ###CALCULAR CDC
#    df= ler_zip("C:\\Users\Lucas Martins\\Downloads\\57996195000199_Estoque_CDC EMPRÉSTIMOS FIDC  CLASSE ÚNICA FECHADA (17).zip")
#    soma = somar_colunas(df,'VALOR_PRESENTE')
#    aVencer = somar_condicao(df,"VALOR_PRESENTE","SITUACAO_RECEBIVEL","A vencer")
#    vencido = somar_condicao(df,"VALOR_PRESENTE","SITUACAO_RECEBIVEL","Vencido")
#    ticket_medio = calcular_ticket_medio(df,"VALOR_PRESENTE")
#    tkt_medio_vencido = calcular_ticket_medio_condicacao(df,"SITUACAO_RECEBIVEL","VALOR_PRESENTE","Vencido")
#    tkt_medio_Avencer = calcular_ticket_medio_condicacao(df, "SITUACAO_RECEBIVEL", "VALOR_PRESENTE", "A vencer")
   # print(f"Ticket medio: {ticket_medio}")
   # print(f"Ticket medio vencido: {tkt_medio_vencido}")
   # print(f"Ticket medio a vencer: {tkt_medio_Avencer}")
   # print(f"linhas : {df.shape[0]}")
   # df.to_excel('resultado2.xlsx', index=False)

