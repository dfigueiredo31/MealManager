import streamlit as st
from pages import MealDetail


@st.dialog("Resultados pesquisa")
def displaySearchResults(results):
    if len(results) == 0:
        st.info("Nenhum resultado encontrado")
    else:
        for result in results:
            st.subheader(result["title"])
            col1, col2 = st.columns(2)
            with col1:
                st.image(
                    result["image"],
                )

            with col2:
                declaracaoNutricional = list(
                    result["nutrition"]["nutrients"][i] for i in [0, 1, 3, 7, 10]
                )
                col1, col2 = st.columns(2)
                for infoNutricional in declaracaoNutricional:
                    with col1:
                        with st.container(height=20, border=False):
                            st.caption(
                                f"{infoNutricional["name"]} : {infoNutricional["amount"]} {infoNutricional["unit"]}"
                            )
                    with col2:
                        with st.container(height=20, border=False):
                            st.progress(
                                (
                                    infoNutricional["percentOfDailyNeeds"]
                                    if infoNutricional["percentOfDailyNeeds"] <= 100
                                    else 100
                                )
                                / 100
                            )
            MealDetail.displayMealDetail(
                result, "standalone", False, False, True, True, False
            )
