import streamlit as st
from infrastructure import *
from entities import *

## session state ##
if "searchString" not in st.session_state:
    st.session_state.searchString = ""

## inicialização do user ##

if st.user.is_logged_in and Db.getUser(st.user["email"]) is None:  # no primeiro login
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
            st.Page("pages/SearchResults.py", title="Pesquisa"),
        ],
    }
else:
    pages = [st.Page("pages/Login.py", title="Login")]


pg = st.navigation(pages)
pg.run()
