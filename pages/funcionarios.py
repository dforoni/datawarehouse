import streamlit as st
import pandas as pd
from datetime import datetime
from contrato import Funcionarios
from pydantic import ValidationError
from database import criar_dados, buscar_dados_por_login, atualizar_dados, deletar_dados

# Interface do Streamlit

from decimal import Decimal

def main():
    st.title("Cadastro de Colaborador")

    # Seletor de ação (Cadastrar, Atualizar, Deletar)
    opcao = st.radio("Selecione a ação:", ["Cadastrar", "Atualizar", "Deletar"])

    if opcao == "Cadastrar":
        # Formulário para cadastro
        with st.form("form_create"):
            nome = st.text_input("Nome Colaborador")
            login = st.text_input("Login")
            grupo = st.text_input("Grupo")
            vinculo = st.text_input("Vinculo")
            dt_inicio = st.date_input("Data Início")
            dt_fim = st.date_input("Data Fim")
            submitted = st.form_submit_button("Adicionar")

            if submitted:
                if not login:
                    st.warning("O campo Login é obrigatório.")
                else:
                    try:
                        cadastro_metas = Funcionarios(
                            nome=nome,
                            login=login,
                            vinculo=vinculo,
                            grupo=grupo,
                            dt_inicio=dt_inicio,
                            dt_fim=dt_fim
                            
                        )
                        criar_dados(cadastro_metas)
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {e}")

   

if __name__=="__main__":
    main()     


