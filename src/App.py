import streamlit as st
from infrastructure import *
from entities import *
from pages import SearchForm


if st.user.is_logged_in:

    ## inicialização do user ##
    user = Db.getUser(st.user["email"])
    if user:  # apos primeiro login
        if "currentUser" not in st.session_state:
            st.session_state.currentUser = user
    else:  # no primeiro login
        user = User.User(
            0, st.user["given_name"], st.user["family_name"], st.user["email"]
        )
        Db.addUser(user)

    ## configuração da sidebar de navegação ##
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

    with st.sidebar:
        SearchForm.displaySearchForm()
else:  # sem login
    pages = [st.Page("pages/Login.py", title="Login")]


pg = st.navigation(pages)
pg.run()
