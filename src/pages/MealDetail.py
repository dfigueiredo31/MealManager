import streamlit as st
import datetime as dt
from typing import Literal


# st.subheader(result["title"])
# col1, col2 = st.columns(2)
# with col1:
#     st.image(
#         result["image"],
#     )


# with col2:
#     declaracaoNutricional = list(
#         result["nutrition"]["nutrients"][i] for i in [0, 1, 3, 7, 10]
#     )
#     col1, col2 = st.columns(2)
#     for infoNutricional in declaracaoNutricional:
#         with col1:
#             with st.container(height=20, border=False):
#                 st.caption(
#                     f"{infoNutricional["name"]} : {infoNutricional["amount"]} {infoNutricional["unit"]}"
#                 )
#         with col2:
#             with st.container(height=20, border=False):
#                 st.progress(
#                     (
#                         infoNutricional["percentOfDailyNeeds"]
#                         if infoNutricional["percentOfDailyNeeds"] <= 100
#                         else 100
#                     )
#                     / 100
#                 )
def mealNutritionalInfo(meal):
    nutritionStats = list(meal["nutrition"]["nutrients"][i] for i in [0, 1, 3, 7, 10])
    col1, col2 = st.columns(2)
    for stat in nutritionStats:
        with col1:
            with st.container(height=20, border=False):
                st.caption(f"{stat["name"]} : {stat["amount"]} {stat["unit"]}")
        with col2:
            with st.container(height=20, border=False):
                st.progress(
                    (
                        stat["percentOfDailyNeeds"]
                        if stat["percentOfDailyNeeds"] <= 100
                        else 100
                    )
                    / 100
                )


def mealDetailStandalone(
    recipe,
    showTitle: bool,
    showImage: bool,
    showSummary: bool,
    showIngredients: bool,
    showNutrition: bool,
):
    st.json(recipe, expanded=False)
    if showTitle:
        st.subheader(recipe["title"])

    if showImage and not showNutrition:
        st.image(recipe["image"], use_container_width=True)

    if showNutrition and not showImage:
        with st.expander("Declaração nutricional"):
            mealNutritionalInfo(recipe)

    if showImage and showNutrition:
        col1, col2 = st.columns(2)
        with col1:
            st.image(
                recipe["image"],
            )

        with col2:
            mealNutritionalInfo(recipe)

    if showSummary:
        st.html(
            recipe["summary"],
        )

    if showIngredients:
        with st.expander("Ingredientes"):
            for ingrediente in recipe["nutrition"]["ingredients"]:
                st.caption(ingrediente["name"])


@st.dialog("Detalhe")
def mealDetailModal(
    recipe,
    showTitle: bool,
    showImage: bool,
    showSummary: bool,
    showIngredients: bool,
    showNutrition: bool,
):
    mealDetailStandalone(
        recipe, showTitle, showImage, showSummary, showIngredients, showNutrition
    )


def displayMealDetail(
    recipe,
    displayMode: Literal["modal", "standalone"],
    showTitle: bool,
    showImage: bool,
    showSummary: bool,
    showIngredients: bool,
    showNutrition: bool,
):
    if displayMode == "modal":
        mealDetailModal(
            recipe, showTitle, showImage, showSummary, showIngredients, showNutrition
        )
    else:
        mealDetailStandalone(
            recipe, showTitle, showImage, showSummary, showIngredients, showNutrition
        )
