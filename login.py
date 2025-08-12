import streamlit as st

# Dados de usuários (em um ambiente real, isso deve ser armazenado em um banco de dados seguro)
USUARIOS = {
    "admin": {"senha": "admin123", "perfil": "admin"},
    "usuario": {"senha": "user123", "perfil": "usuario"}
}

# Função para verificar o login
def verificar_login(usuario, senha):
    if usuario in USUARIOS and USUARIOS[usuario]["senha"] == senha:
        return True
    return False

# Função para obter o perfil do usuário
def obter_perfil(usuario):
    return USUARIOS[usuario]["perfil"]

# Página de login
def pagina_login():
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Login"):
        if verificar_login(usuario, senha):
            st.session_state["usuario"] = usuario
            st.session_state["perfil"] = obter_perfil(usuario)
            st.success("Login realizado com sucesso!")
            st.rerun()  # Recarrega a página para atualizar o estado
        else:
            st.error("Usuário ou senha incorretos")

# Página restrita para administradores
def pagina_admin():
    st.title("Página do Administrador")
    st.write("Bem-vindo, administrador!")
    st.write("Aqui você pode gerenciar o sistema.")

# Página restrita para usuários comuns
def pagina_usuario():
    st.title("Página do Usuário")
    st.write("Bem-vindo, usuário!")
    st.write("Aqui você pode visualizar suas informações.")

# Página principal do aplicativo
def main():
    if "usuario" not in st.session_state:
        pagina_login()
    else:
        perfil = st.session_state["perfil"]
        if perfil == "admin":
            pagina_admin()
        elif perfil == "usuario":
            pagina_usuario()
        
        if st.button("Logout"):
            del st.session_state["usuario"]
            del st.session_state["perfil"]
            st.rerun()  # Recarrega a página para voltar ao login

if __name__ == "__main__":
    main()