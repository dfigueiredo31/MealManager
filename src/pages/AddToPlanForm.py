import streamlit as st
from entities import MealPlanItem
from infrastructure import Db

user = Db.getUser(st.user["email"])


def addToPlanCallbackFunction(planId, selectedDate, recipe):
    Db.addMealPlanItem(
        planId,
        MealPlanItem.MealPlanItem(
            0, recipe["title"], selectedDate, recipe["id"], recipe["image"]
        ),
    )


## Add to plan UI ##
def displayAddToPlanForm(recipe):
    with st.expander("Adicionar ao plano"):
        selection = st.selectbox(
            "Plano",
            map(
                lambda x: f"{x.id} - {x.name} - {x.startDate} a {x.endDate}",
                user.mealPlans,
            ),
            key=f"{recipe["id"]}_plan",
        )

        selectedSplit = selection.split(" - ")
        selectedPlan = selectedSplit[0]
        selectedPlanStarDate = selectedSplit[2].split(" a ")[0]
        selectedPlanEndDate = selectedSplit[2].split(" a ")[1]

        selectedDate = st.date_input(
            "Adicionar a ",
            value=selectedPlanStarDate,
            min_value=selectedPlanStarDate,
            max_value=selectedPlanEndDate,
            key=f"{recipe["id"]}_date",
        )

        st.button(
            "Adicionar",
            key=f"{recipe["id"]}_add",
            on_click=addToPlanCallbackFunction,
            args=[selectedPlan, selectedDate, recipe],
        )
