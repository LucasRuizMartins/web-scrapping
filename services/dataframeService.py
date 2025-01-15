from services.ConversorService import *
from entities.ScrappingFidic import *
from entities.Consolidado import  *

def gerar_dataframe(path):

    # -------------- CALCULAR MULTISSETORIAL
    df = ler_zip(path)
    consolidado = Consolidado(df)
    consolidadoFaturaCartao = Consolidado(filtrar_tipo(df,"Operacao Cartao de Credito DIGITAL"))
    consolidadoCartao = Consolidado(filtrar_tipo(df,"FATURA DE CARTAO DE CREDITO"))


    #---------------------------------------- TOTAL -----------------
    print("Total \n")
    imprimir(consolidado)
    print("Cartao Digital \n")
    imprimir(consolidadoFaturaCartao)
    print("Fatura de Cartão de Crédito \n")
    imprimir(consolidadoCartao)