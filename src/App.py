import streamlit as st
from infrastructure import *
from entities import *

## inicialização do user ##

if st.user.is_logged_in and not Db.userExists(st.user["email"]):  # no primeiro login
    user = User.User(0, st.user["given_name"], st.user["family_name"], st.user["email"])
    Db.addUser(user)


## configuração da sidebar de navegação ##
if st.user.is_logged_in:
    pages = {
        "Pessoal": [
            st.Page("pages/Home.py", title="Home"),
            st.Page("pages/Settings.py", title="Definições"),
        ],
        "Recursos": [
            st.Page("pages/Meal plan.py", title="Plano Alimentar"),
            st.Page("pages/Shopping list.py", title="Lista de Compras"),
        ],
    }
else:
    pages = [st.Page("pages/Login.py", title="Login")]


pg = st.navigation(pages)
pg.run()
