import streamlit as st
from pages import MealDetail


@st.dialog("Resultados pesquisa")
def displaySearchResults(results):
    if len(results) == 0:
        st.info("Nenhum resultado encontrado")
    else:
        for result in results:
            MealDetail.displayMealDetail(
                result, "standalone", True, True, False, True, True, True, True
            )
