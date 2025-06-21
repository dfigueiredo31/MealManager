import streamlit as st
from typing import Literal


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
    showPreparationSteps: bool,
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

    if showPreparationSteps:
        with st.expander("Preparação"):
            for step in recipe["analyzedInstructions"][0]["steps"]:
                st.caption(step["step"])


@st.dialog("Detalhe")
def mealDetailModal(
    recipe,
    showTitle: bool,
    showImage: bool,
    showSummary: bool,
    showIngredients: bool,
    showNutrition: bool,
    showPreparationSteps: bool,
):
    mealDetailStandalone(
        recipe,
        showTitle,
        showImage,
        showSummary,
        showIngredients,
        showNutrition,
        showPreparationSteps,
    )


def displayMealDetail(
    recipe,
    displayMode: Literal["modal", "standalone"],
    showTitle: bool,
    showImage: bool,
    showSummary: bool,
    showIngredients: bool,
    showNutrition: bool,
    showPreparationSteps: bool,
):
    if displayMode == "modal":
        mealDetailModal(
            recipe,
            showTitle,
            showImage,
            showSummary,
            showIngredients,
            showNutrition,
            showPreparationSteps,
        )
    else:
        mealDetailStandalone(
            recipe,
            showTitle,
            showImage,
            showSummary,
            showIngredients,
            showNutrition,
            showPreparationSteps,
        )
