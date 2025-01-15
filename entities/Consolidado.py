from services.ConversorService import *

class Consolidado:
    def __init__(self, dataframe):
        self.dataframe_vencido = filtrar_situacao(dataframe,"Vencido")
        self.dataframe_a_vencer = filtrar_situacao(dataframe, "A vencer")
        self.data = "31/12/2024"
        self.a_vencer = somar_colunas(self.dataframe_a_vencer, "VALOR_PRESENTE")
        self.vencido =  somar_colunas(self.dataframe_vencido, "VALOR_PRESENTE")
        self.total =    somar_colunas(dataframe, "VALOR_PRESENTE")
        self.pdd = somar_colunas(dataframe, "VALOR_PDD")
        self.wop = None
        self.ticket_medio_aquisicao_a_vencer = calcular_ticket_medio(self.dataframe_a_vencer,"VALOR_AQUISICAO")
        self.ticket_medio_aquisicao_vencido = calcular_ticket_medio(self.dataframe_vencido,"VALOR_AQUISICAO")
        self.ticket_medio_aquisicao_total = calcular_ticket_medio(dataframe,"VALOR_AQUISICAO")
        self.ticket_medio_atual_a_vencer = calcular_ticket_medio(self.dataframe_a_vencer,"VALOR_PRESENTE")
        self.ticket_medio_atual_vencido =  calcular_ticket_medio(self.dataframe_vencido,"VALOR_PRESENTE")
        self.ticket_medio_atual_total = calcular_ticket_medio(dataframe,"VALOR_PRESENTE")
        self.ticket_medio_nominal_a_vencer =  calcular_ticket_medio(self.dataframe_a_vencer,"VALOR_NOMINAL")
        self.ticket_medio_nominal_vencido = calcular_ticket_medio(self.dataframe_vencido,"VALOR_NOMINAL")
        self.ticket_medio_nominal_total = calcular_ticket_medio(dataframe,"VALOR_NOMINAL")
        self.taxa_cessao_mediana_a_vencer = None
        self.taxa_cessao_mediana_vencido = None
        self.taxa_cessao_mediana_total = None
        self.prazo_medio_a_vencer = None
        self.prazo_medio_vencido = None
        self.prazo_medio_total = None
        self.ultima_quinzena_ticket_medio_aquisicao_a_vencer = calcular_ticket_medio_quinzena(self.dataframe_a_vencer, "VALOR_AQUISICAO", "DATA_AQUISICAO", self.data)
        self.ultima_quinzena_ticket_medio_aquisicao_vencido = calcular_ticket_medio_quinzena(self.dataframe_vencido, "VALOR_AQUISICAO", "DATA_AQUISICAO", self.data)
        self.ultima_quinzena_ticket_medio_aquisicao_total = calcular_ticket_medio_quinzena(dataframe,"VALOR_AQUISICAO","DATA_AQUISICAO",self.data)
        self.ultima_quinzena_ticket_medio_atual_a_vencer = calcular_ticket_medio_quinzena(self.dataframe_a_vencer, "VALOR_PRESENTE", "DATA_AQUISICAO", self.data)
        self.ultima_quinzena_ticket_medio_atual_vencido = calcular_ticket_medio_quinzena(self.dataframe_vencido, "VALOR_PRESENTE", "DATA_AQUISICAO", self.data)
        self.ultima_quinzena_ticket_medio_atual_total = calcular_ticket_medio_quinzena(dataframe,"VALOR_PRESENTE","DATA_AQUISICAO",self.data)
        self.ultima_quinzena_ticket_medio_nominal_a_vencer = calcular_ticket_medio_quinzena(self.dataframe_a_vencer, "VALOR_NOMINAL", "DATA_AQUISICAO", self.data)
        self.ultima_quinzena_ticket_medio_nominal_vencido = calcular_ticket_medio_quinzena(self.dataframe_vencido, "VALOR_NOMINAL", "DATA_AQUISICAO", self.data)
        self.ultima_quinzena_ticket_medio_nominal_total = calcular_ticket_medio_quinzena(dataframe,"VALOR_NOMINAL","DATA_AQUISICAO",self.data)
        self.ultima_quinzena_taxa_cessao_mediana_a_vencer = None
        self.ultima_quinzena_taxa_cessao_mediana_vencido = None
        self.ultima_quinzena_taxa_cessao_mediana_total = None
        self.ultima_quinzena_prazo_medio_a_vencer = None
        self.ultima_quinzena_prazo_medio_vencido = None
        self.ultima_quinzena_prazo_medio_total = None
        self.quantidade_titulos_a_vencer = dataframe[dataframe["PRAZO_ATUAL"] > 0].shape[0]
        self.quantidade_titulos_vencido = dataframe[dataframe["PRAZO_ATUAL"] < 1].shape[0]
        self.quantidade_titulos_total = dataframe.shape[0]
        self.valor_total_adquirido = None
        self.quantidade_total_adquirido = None
        self.total_cedentes = dataframe["DOC_CEDENTE"].nunique()
        self.total_sacados = dataframe["DOC_SACADO"].nunique()
        self.a_vencer_ate_15 = somar_intervalo(dataframe,0,15)
        self.a_vencer_16_a_30 = somar_intervalo(dataframe,15,30)
        self.a_vencer_31_a_60 = somar_intervalo(dataframe,30,60)
        self.a_vencer_61_a_90 = somar_intervalo(dataframe,60,90)
        self.a_vencer_91_a_120 = somar_intervalo(dataframe,90,120)
        self.a_vencer_121_a_150 = somar_intervalo(dataframe,120,150)
        self.a_vencer_151_a_180 = somar_intervalo(dataframe,150,180)
        self.a_vencer_181_a_365 = somar_intervalo(dataframe,180,365)
        self.a_vencer_acima_365 = somar_intervalo(dataframe,365,999999999)
        self.vencido_ate_15 =  somar_intervalo_negativo(self.dataframe_vencido,1,-15)
        self.vencido_16_a_30 = somar_intervalo_negativo(self.dataframe_vencido,-15,-30)
        self.vencido_31_a_60 =  somar_intervalo_negativo(self.dataframe_vencido,-30,-60)
        self.vencido_61_a_90 = somar_intervalo_negativo(self.dataframe_vencido,-60,-90)
        self.vencido_91_a_120 = somar_intervalo_negativo(self.dataframe_vencido,-90,-120)
        self.vencido_121_a_150 = somar_intervalo_negativo(self.dataframe_vencido,-120,-150)
        self.vencido_151_a_180 = somar_intervalo_negativo(self.dataframe_vencido,-150,-180)
        self.vencido_181_a_365 = somar_intervalo_negativo(self.dataframe_vencido,-180,-365)
        self.vencido_acima_365 =  somar_intervalo_negativo(self.dataframe_vencido,-365,-999999999)
        self.projecao_pdd_d0 = None
        self.projecao_pdd_d1 = None
        self.projecao_pdd_d2 = None
        self.projecao_pdd_d3 = None
        self.projecao_pdd_d4 = None
        self.projecao_pdd_d5 = None


#--------------QUINZENA -------------

def calcular_ticket_medio_quinzena(df,coluna_calculada,coluna_data,data):
    if isinstance(data, str):
        data = pd.to_datetime(data, format='%d/%m/%Y')

    df.loc[:, coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce', dayfirst=True)

    data_inicial = data - pd.Timedelta(days=14)
    df_filtrado = df[df[coluna_data] >= data_inicial]

    if df_filtrado.empty:
        return 0
    df_filtrado.loc[:, coluna_calculada] = pd.to_numeric(df_filtrado[coluna_calculada], errors='coerce')

    return round(df_filtrado[coluna_calculada].sum() / df_filtrado.shape[0], 2)


#------------ CALCULOS SIMPLES

def calcular_ticket_medio(df,coluna_calculada):
    converter_col_numeric(df,coluna_calculada)
    return round(df[coluna_calculada].sum() / df.shape[0],2)

def calcular_titulos_vencidos(df):
    return  df[df["PRAZO_ATUAL"] < 1].shape[0]

def somar_colunas(df,nome_coluna):
    df = converter_col_numeric(df,nome_coluna)
    return df[nome_coluna].sum()

def somar_intervalo(df,data_ini,data_fim):
    df_filtrado = df[(df["PRAZO_ATUAL"] > data_ini) & (df["PRAZO_ATUAL"] <= data_fim)]
    return round(somar_colunas(df_filtrado,"VALOR_PRESENTE"),2)

def somar_intervalo_negativo(df,data_ini,data_fim):
    df_filtrado = df[(df["PRAZO_ATUAL"] < data_ini) & (df["PRAZO_ATUAL"] >= data_fim)]
    return round(somar_colunas(df_filtrado,"VALOR_PRESENTE"),2)


def imprimir(consolidado):
    print(f"Valor à vencer: {round(consolidado.a_vencer, 2)}")
    print(f"Valor vencido: {round(consolidado.vencido, 2)}")
    print(f"Total: {round(consolidado.total, 2)}")
    print(f"pdd: {round(consolidado.pdd, 2)}")
    print(f"Ticket Medio Aquisicao a vencer: {consolidado.ticket_medio_aquisicao_a_vencer}")
    print(f"Ticket Medio Aquisicao vencido: {consolidado.ticket_medio_aquisicao_vencido}")
    print(f"Ticket Medio Aquisicao: {consolidado.ticket_medio_aquisicao_total}")
    print(f"Ticket Medio atual a vencer: {consolidado.ticket_medio_atual_a_vencer}")
    print(f"Ticket Medio atual vencido: {consolidado.ticket_medio_atual_vencido}")
    print(f"Ticket Medio: {consolidado.ticket_medio_atual_total}")
    print(f"Ticket Medio Nominal a vencer: {consolidado.ticket_medio_nominal_a_vencer}")
    print(f"Ticket Medio Nominal vencido: {consolidado.ticket_medio_nominal_vencido}")
    print(f"Ticket Medio Nominal: {consolidado.ticket_medio_nominal_total}")
    print(f"Tkt medio Quinzena Aquisicao A vencer: {consolidado.ultima_quinzena_ticket_medio_aquisicao_a_vencer}")
    print(f"Tkt medio Quinzena Aquisicao Vencido: {consolidado.ultima_quinzena_ticket_medio_aquisicao_vencido}")
    print(f"Tkt medio Quinzena Aquisicao Total: {consolidado.ultima_quinzena_ticket_medio_aquisicao_total}")
    print(f"Tkt medio Quinzena Atual A vencer: {consolidado.ultima_quinzena_ticket_medio_atual_a_vencer}")
    print(f"Tkt medio Quinzena Atual Vencido: {consolidado.ultima_quinzena_ticket_medio_atual_vencido}")
    print(f"Tkt medio Quinzena Atual Total: {consolidado.ultima_quinzena_ticket_medio_atual_total}")
    print(f"Tkt medio Quinzena Nominal A vencer: {consolidado.ultima_quinzena_ticket_medio_nominal_a_vencer}")
    print(f"Tkt medio Quinzena Nominal Vencido: {consolidado.ultima_quinzena_ticket_medio_nominal_vencido}")
    print(f"Tkt medio Quinzena Nominal Total: {consolidado.ultima_quinzena_ticket_medio_nominal_total}")
    print(f"Titulos A vencer: {consolidado.quantidade_titulos_a_vencer}")
    print(f"Titulos vencidos: {consolidado.quantidade_titulos_vencido}")
    print(f"Titulos Total: {consolidado.quantidade_titulos_total}")
    print(f"Total Cedente: {consolidado.total_cedentes}")
    print(f"Total Sacados: {consolidado.total_sacados}")
    print(f"A vencer ate 15 dias: {consolidado.a_vencer_ate_15}")
    print(f"A vencer ate 16 ~30 dias: {consolidado.a_vencer_16_a_30}")
    print(f"A vencer ate 31 ~ 60 dias: {consolidado.a_vencer_31_a_60}")
    print(f"A vencer ate 61 ~ 90 dias: {consolidado.a_vencer_61_a_90}")
    print(f"A vencer ate 91 ~ 120 dias: {consolidado.a_vencer_91_a_120}")
    print(f"A vencer ate 121 ~ 150 dias: {consolidado.a_vencer_121_a_150}")
    print(f"A vencer ate 151 ~ 180 dias: {consolidado.a_vencer_151_a_180}")
    print(f"A vencer ate 181 ~365 dias: {consolidado.a_vencer_181_a_365}")
    print(f"A vencer acima de 365 : {consolidado.a_vencer_acima_365}")
    print(f"A Vencido ate 15 dias: {consolidado.vencido_ate_15}")
    print(f"A Vencido ate 16 ~30 dias: {consolidado.vencido_16_a_30}")
    print(f"A Vencido ate 31 ~ 60 dias: {consolidado.vencido_31_a_60}")
    print(f"A Vencido ate 61 ~ 90 dias: {consolidado.vencido_61_a_90}")
    print(f"A Vencido ate 91 ~ 120 dias: {consolidado.vencido_91_a_120}")
    print(f"A Vencido ate 121 ~ 150 dias: {consolidado.vencido_121_a_150}")
    print(f"A Vencido ate 151 ~ 180 dias: {consolidado.vencido_151_a_180}")
    print(f"A Vencido ate 181 ~365 dias: {consolidado.vencido_181_a_365}")
    print(f"A Vencido acima de 365 : {consolidado.vencido_acima_365}")
    print("----------------------------\n\n\n")