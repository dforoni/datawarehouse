import streamlit as st
import pandas as pd
from datetime import datetime
from contrato import Metas
from pydantic import ValidationError
from database import criar_dados, buscar_dados_por_login, atualizar_dados, deletar_dados

# Interface do Streamlit

from decimal import Decimal

def main():
    st.title("Gerenciador de Metas")

    # Seletor de ação (Cadastrar, Atualizar, Deletar)
    opcao = st.radio("Selecione a ação:", ["Cadastrar", "Atualizar", "Deletar"])

    if opcao == "Cadastrar":
        # Formulário para cadastro
        with st.form("form_create"):
            login = st.text_input("Login")
            dt_inicio = st.date_input("Data Início")
            dt_fim = st.date_input("Data Fim")
            meta = st.number_input("Meta", min_value=0.0, value=1.0, step=1.0, format="%.2f")
            piso_remuneracao = st.number_input("Piso de Remuneração", min_value=0.0, value=0.0, step=0.1, format="%.2f")
            submitted = st.form_submit_button("Adicionar")

            if submitted:
                if not login:
                    st.warning("O campo Login é obrigatório.")
                else:
                    try:
                        cadastro_metas = Metas(
                            login=login,
                            dt_inicio=dt_inicio,
                            dt_fim=dt_fim,
                            meta=Decimal(meta),
                            piso_remuneracao=Decimal(piso_remuneracao)
                        )
                        criar_dados(cadastro_metas)
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {e}")

    elif opcao == "Atualizar":
        # Formulário para atualização
        st.header("Atualizar Registro Existente")

        # Campo para buscar registro pelo login
        login = st.text_input("Login do registro que deseja atualizar:")
        buscar = st.button("Buscar Dados")

        if buscar:
            if not login:
                st.warning("Digite o login para buscar os dados.")
            else:
                dados = buscar_dados_por_login(login)
                if dados:
                    st.success("Dados encontrados!")
                    dt_inicio = dados["dt_inicio"]
                    dt_fim = dados["dt_fim"]
                    meta = float(dados["meta"])  # Convertendo para float
                    piso_remuneracao = float(dados["piso_remuneracao"])  # Convertendo para float
                else:
                    st.warning("Nenhum registro encontrado com o login fornecido.")
                    dt_inicio = None
                    dt_fim = None
                    meta = 0.0
                    piso_remuneracao = 0.0
        else:
            dt_inicio = None
            dt_fim = None
            meta = 0.0
            piso_remuneracao = 0.0

        with st.form("form_update"):
            dt_inicio = st.date_input("Nova Data Início", value=dt_inicio if dt_inicio else None)
            dt_fim = st.date_input("Nova Data Fim", value=dt_fim if dt_fim else None)
            meta = st.number_input("Nova Meta", min_value=0.0, value=meta, step=1.0, format="%.2f")
            piso_remuneracao = st.number_input("Novo Piso de Remuneração", min_value=0.0, value=piso_remuneracao, step=0.1, format="%.2f")
            submitted_update = st.form_submit_button("Atualizar")

            if submitted_update:
                if not login:
                    st.warning("O campo Login é obrigatório.")
                else:
                    try:
                        novos_dados = Metas(
                            login=login,
                            dt_inicio=dt_inicio,
                            dt_fim=dt_fim,
                            meta=Decimal(meta),
                            piso_remuneracao=Decimal(piso_remuneracao)
                        )
                        atualizar_dados(login, novos_dados)
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {e}")

    elif opcao == "Deletar":
        # Formulário para deletar registro
        st.header("Deletar Registro")

        with st.form("form_delete"):
            login = st.text_input("Login do registro que deseja deletar")
            submitted_delete = st.form_submit_button("Deletar")

            if submitted_delete:
                if not login:
                    st.warning("O campo Login é obrigatório.")
                else:
                    try:
                        deletar_dados(login)
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {e}")

if __name__=="__main__":
    main()     


