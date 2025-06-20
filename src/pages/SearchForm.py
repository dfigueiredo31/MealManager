import streamlit as st
from infrastructure import Api
from infrastructure import Db
from pages import SearchResults


## Search form callback ##
def searchCallBackFunction():

    user = Db.getUser(st.user["email"])
    diets = []
    intolerances = []
    readyTime = None

    if st.session_state.userDiets:
        diets = list(map(lambda x: x.description, user.preferedDiets))

    if st.session_state.userIntolerances:
        intolerances = list(map(lambda x: x.description, user.intolerances))

    if st.session_state.under25:
        readyTime = 25

    searchResults = Api.getRecipes(
        st.session_state.queryString,
        diets,
        intolerances,
        [],
        [],
        True,
        True,
        True,
        True,
        True,
        readyTime,
        10,
    ).json()["results"]

    SearchResults.displaySearchResults(searchResults)


## Search form UI ##
def displaySearchForm():
    st.text_input(
        "Pesquisar refeições",
        placeholder="Pesquisar refeições",
        key="queryString",
        on_change=searchCallBackFunction,
        label_visibility="collapsed",
        icon="🔎",
    )

    st.toggle("Receitas rápidas", key="under25")
    st.toggle("Considerar dietas?", key="userDiets")
    st.toggle("Considerar intolerâncias?", key="userIntolerances")
