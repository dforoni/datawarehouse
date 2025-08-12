import streamlit as st
import colaborador
import financeiro
import metas

st.set_page_config(page_title="Produtividade Médica POC", page_icon="📊")

# Criar menu de navegação
menu = st.sidebar.radio("**Menu de Cadastro**", ["Início", "Metas", "Colaborador", "Financeiro"])

# Exibir a página correspondente
if menu == "Início":
    st.title("Bem-vindo ao Aplicativo")
    st.write("Escolha uma página no menu lateral para começar.")

elif menu == "Metas":
    metas.main()  

elif menu == "Colaborador":
    colaborador.main() 

elif menu == "Financeiro":
    financeiro.main()  

# Criar menu de navegação
menu = st.sidebar.radio("**Menu de Gráficos**", ["Laudos Realizados", "Análise de Voluntários", "Análise de Outros Vínculos"])

# Criar menu de navegação
menu = st.sidebar.radio("**Menu de Folha de Pagamento**", ["Folha de Pagamento"])


