import streamlit as st
from entities.MealPlan import MealPlan
from infrastructure import *


## Meal plan page ##
user = Db.getUser(st.user["email"])
userMealPlans = Db.getUserMealPlans(user.id)


@st.dialog("Novo plano")
def newPlan():
    name = st.text_input("Nome do plano")
    startDate = st.date_input("Data inicio")
    endDate = st.date_input("Data fim")

    if st.button("Criar"):
        user.mealPlans.append(MealPlan(0, startDate, endDate, name))
        Db.addUserMealPlan(user)


st.title("Plano alimentar")

if len(userMealPlans) == 0:
    st.info("Não há nenhum plano criado para o utilizador.")

if st.button("Novo plano"):
    newPlan()
