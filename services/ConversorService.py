import pandas as pd


def filtrar_situacao(df,situacao):
    return df[df["SITUACAO_RECEBIVEL"] == situacao]

def filtrar_tipo(df,tipo):
    return df[df["TIPO_RECEBIVEL"] == tipo]

def remover_colunas(df):
    colunas_a_remover = [
        'TAXA_JUROS_VENCIDOS', 'DATA_CARENCIA', 'TAXA_JUROS_INDEXADOR', 'TP_JUROS', 'DEFASAGEM',
        'NOME', 'VALOR_NOMINAL_IOF', 'NU_BANCO_CHEQUE', 'NU_AGENCIA_CHEQUE', 'NU_CONTA_CHEQUE',
        'CMC7_CHEQUE', 'CODIGO_ORIGEM', 'CODIGO_FINALIDADE', 'ID_REGISTRO', 'FAIXA_PDD_GERAL',
        'TIPO_PDD_GERAL', 'VALOR_PDD_GERAL'
    ]
    return df.drop(colunas_a_remover, axis=1)

def converter_col_numeric(df, nome_coluna):
    try:
        df.loc[:, nome_coluna] = df[nome_coluna].str.replace(r'\.', '', regex=True)
        df.loc[:, nome_coluna] = df[nome_coluna].str.replace(r',', '.', regex=True)
        df.loc[:, nome_coluna] = pd.to_numeric(df[nome_coluna], errors='coerce')
    except Exception as e:
        print(f"Erro ao converter a coluna {nome_coluna}: {e}")
    return df



#------------ UTILITARIO



#--------------REFATORAR

""" 
def substituir_virgula_por_ponto(df, nome_coluna):
    try:
        df[nome_coluna] = df[nome_coluna].str.replace(',', '.', regex=True)
    except Exception as e:
        print(f"Erro ao substituir vírgula na coluna {nome_coluna}: {e}")
    return df


def calcular_ticket_medio_condicacao_quinzena(df,coluna_data,coluna_calculada,coluna_condicao, data):
    converter_col_numeric(df, coluna_calculada)
    if isinstance(data, str):
        data = pd.to_datetime(data, format='%d/%m/%Y')

    df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')
    data_inicial = data - pd.Timedelta(days=14)
    df_filtrado = df[df[coluna_data] >= data_inicial]

    if df_filtrado.empty:
        return 0


    sum = df_filtrado[coluna_calculada].sum()
    total_linhas = df_filtrado.shape[0]
    result = sum / total_linhas
    return round(result,2)

def somar_condicao(df,coluna_calculada,coluna_analise,condicao):
    df = converter_col_numeric(df,coluna_calculada)
    valores_vencidos = df[df[coluna_analise] == condicao]

    return valores_vencidos[coluna_calculada].sum()

def converter_numeros(df):
    df['VALOR_PRESENTE'] = df['VALOR_PRESENTE'].str.replace(r'(?<=\d),(?=\d{3}\.)', '', regex=True)
    df['VALOR_PRESENTE'] = pd.to_numeric(df['VALOR_PRESENTE'], errors='coerce')
    df['VALOR_NOMINAL'] = df['VALOR_NOMINAL'].str.replace(r'(?<=\d),(?=\d{3}\.)', '', regex=True)
    df['VALOR_NOMINAL'] = pd.to_numeric(df['VALOR_NOMINAL'], errors='coerce')
    df['VALOR_AQUISICAO'] = df['VALOR_AQUISICAO'].str.replace(r'(?<=\d),(?=\d{3}\.)', '', regex=True)
    df['VALOR_AQUISICAO'] = pd.to_numeric(df['VALOR_AQUISICAO'], errors='coerce')

    df['DATA_VENCIMENTO_AJUSTADA'] = pd.to_datetime(df['DATA_VENCIMENTO_AJUSTADA'], format='%d/%m/%Y')
    df['DATA_EMISSAO'] = pd.to_datetime(df['DATA_EMISSAO'], format='%d/%m/%Y')
    df['DATA_AQUISICAO'] = pd.to_datetime(df['DATA_AQUISICAO'], format='%d/%m/%Y')
    df['DATA_VENCIMENTO_ORIGINAL'] = pd.to_datetime(df['DATA_VENCIMENTO_ORIGINAL'], format='%d/%m/%Y')
    df['DATA_FUNDO'] = pd.to_datetime(df['DATA_FUNDO'], format='%d/%m/%Y')
    df['DATA_REFERENCIA'] = pd.to_datetime(df['DATA_REFERENCIA'], format='%d/%m/%Y')

    return df

def calcular_ticket_medio_condicacao(df,coluna_analise,coluna_calculada, condicao):
    converter_col_numeric(df, coluna_calculada)
    df_filtrada = df[df[coluna_analise] == condicao]
    sum = df_filtrada[coluna_calculada].sum()
    total = df_filtrada.shape[0]
    result = sum / total
    return round(result,2)
"""