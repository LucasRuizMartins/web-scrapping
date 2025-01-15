import os
import psycopg2
from io import StringIO
import psycopg2
import os
import time

def conectar_postgresql():
    host = os.getenv('DB_HOST')
    #database = os.getenv('Databases')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    nome_database = "desenvolvimento"


    try:
        conn = psycopg2.connect(
            dbname=nome_database,
            host=host,
           #database=database,
            user=user,
            password=password,
            port = "5432"
        )
        #print("Conexão com o PostgreSQL estabelecida com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def executar_consulta(conn, query, parametros=None):
    try:
        cursor = conn.cursor()
        cursor.execute(query, parametros)
        resultados = cursor.fetchall()  # Para SELECT
        cursor.close()
        return resultados
    except Exception as e:
        print(f"Erro ao executar consulta: {e}")
        return None


def executar_insert(conn, query, parametros=None):
    try:
        cursor = conn.cursor()
        cursor.execute(query, parametros)
        conn.commit()  # Confirma a transação
        cursor.close()
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao executar insert: {e}")
        conn.rollback()  # Reverte a transação em caso de erro


def inserir_df(conn, df, tabela):
    # Obtém os nomes das colunas do DataFrame
    colunas = df.columns.tolist()

    # Formata a query de insert
    query = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['%s'] * len(colunas))})"

    # Itera sobre as linhas do DataFrame e insere os dados
    for _, linha in df.iterrows():
        parametros = tuple(linha)  # Converte a linha para tupla, que é o formato aceito para execução
        executar_insert(conn, query, parametros)

def inserir_df_com_copy(conn, df, tabela):
    # Converte o DataFrame para um formato CSV em memória
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False, sep='\t')
    df.columns = df.columns.str.lower()
    buffer.seek(0)


    inicio = time.time()

    with conn.cursor() as cursor:
        # Usa o comando COPY para inserir os dados
        cursor.copy_from(buffer, tabela, sep='\t', columns=df.columns)
    conn.commit()


    fim = time.time()


    tempo_gasto = fim - inicio
    print(f"Tempo para inserir os dados: {tempo_gasto:.2f} segundos")

def listar_tabelas(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT schemaname, tablename
            FROM pg_catalog.pg_tables
            WHERE schemaname NOT IN ('pg_catalog', 'information_schema');
        """)
        tabelas = cursor.fetchall()
        cursor.close()
        return tabelas
    except Exception as e:
        print(f"Erro ao listar tabelas: {e}")
        return None
