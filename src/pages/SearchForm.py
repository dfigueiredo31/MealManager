import streamlit as st
from infrastructure import Api
from pages import SearchResultsModal


def searchCallBackFunction():
    searchResults = Api.getRecipes(
        st.session_state.queryString,
        [],
        [],
        [],
        [],
        True,
        True,
        True,
        True,
        True,
        120,
        10,
    ).json()["results"]
    # st.switch_page(st.Page("pages/SearchResults.py"))
    SearchResultsModal.displaySearchResults(searchResults)


def displaySearchForm():
    st.text_input(
        "Pesquisar refeições",
        key="queryString",
        on_change=searchCallBackFunction,
        label_visibility="hidden",
        icon="🔎",
    )
