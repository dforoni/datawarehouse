import streamlit as st
from pages import metas, colaborador, financeiro

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
menu = st.sidebar.radio("**Menu de Gráficos**", ["Laudos Realizados", "Análise de Voluntários"])

# Criar menu de navegação
menu = st.sidebar.radio("**Menu de Folha de Pagamento**", ["Folha de Pagamento"])


