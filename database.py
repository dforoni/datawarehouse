import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
from contrato import Metas
import streamlit as st

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para criar os dados validados
def criar_dados(dados: Metas):
    """
    Função para criar um registro no banco de dados.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS     
        )
        # Mensagem de sucesso para a conexão
        st.success("Conexão com o banco de dados realizada com sucesso!")

        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de compras
        insert_query = sql.SQL(
            "INSERT INTO cadastro.meta (login, dt_inicio, dt_fim, meta, piso_remuneracao) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.login,
            dados.dt_inicio,
            dados.dt_fim,
            dados.meta,
            dados.piso_remuneracao

        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")

def buscar_dados_por_login(login: str):
    """
    Função para buscar os dados de um registro no banco de dados pelo login.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        # Query para buscar o registro
        query = sql.SQL("SELECT dt_inicio, dt_fim, meta, piso_remuneracao FROM cadastro.meta WHERE login = %s")
        cursor.execute(query, (login,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado:
            return {
                "dt_inicio": resultado[0],
                "dt_fim": resultado[1],
                "meta": resultado[2],
                "piso_remuneracao": resultado[3],
            }
        else:
            return None
    except Exception as e:
        st.error(f"Erro ao buscar os dados no banco: {e}")
        return None

# Função para atualizar os dados
def atualizar_dados(login, novos_dados: Metas):
    """
    Função para atualizar um registro no banco de dados.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        # Mensagem de sucesso para a conexão
        st.success("Conexão com o banco de dados realizada com sucesso!")

        cursor = conn.cursor()

        # Query para atualizar os dados
        update_query = sql.SQL(
            """
            UPDATE cadastro.meta
            SET dt_inicio = %s,
                dt_fim = %s,
                meta = %s,
                piso_remuneracao = %s
            WHERE login = %s
            """
        )
        cursor.execute(update_query, (
            novos_dados.dt_inicio,
            novos_dados.dt_fim,
            novos_dados.meta,
            novos_dados.piso_remuneracao,
            login
        ))

        # Confirmação da transação
        conn.commit()
        cursor.close()
        conn.close()

        st.success("Dados atualizados com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao atualizar no banco de dados: {e}")

# Função para deletar os dados
def deletar_dados(login: str):
    """
    Função para deletar um registro no banco de dados.
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        # Mensagem de sucesso para a conexão
        st.success("Conexão com o banco de dados realizada com sucesso!")

        cursor = conn.cursor()

        # Query para deletar o registro
        delete_query = sql.SQL("DELETE FROM cadastro.meta WHERE login = %s")
        cursor.execute(delete_query, (login,))

        # Confirmação da transação
        conn.commit()

        if cursor.rowcount == 0:
            st.warning("Nenhum registro encontrado com o login fornecido.")
        else:
            st.success("Registro deletado com sucesso!")

        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Erro ao deletar registro no banco de dados: {e}")

