import streamlit as st
from entities.MealPlan import MealPlan
from infrastructure import Db


## Meal plan page ##
user = Db.getUser(st.user["email"])
userMealPlans = Db.getUserMealPlans(user.id)


@st.dialog("Novo plano")
def newPlan():
    name = st.text_input("Nome do plano")
    startDate = st.date_input("Data inicio")
    endDate = st.date_input("Data fim")

    if st.button("Criar"):
        Db.addUserMealPlan(user, MealPlan(0, startDate, endDate, name))
        st.rerun()


st.title("Plano alimentar")

if len(userMealPlans) == 0:
    st.info("Não há nenhum plano criado para o utilizador.")

with st.form("mealSearch"):
    st.session_state.searchString = st.text_input(
        "Pesquisar refeições",
    )
    if st.form_submit_button("Pesquisa"):
        st.switch_page(st.Page("pages/SearchResults.py", title="Pesquisa"))


for mealPlan in userMealPlans:
    st.divider()
    st.write(f"Nome: {mealPlan.name}")
    st.write(f"Data inicio: {mealPlan.startDate}")
    st.write(f"Data fim: {mealPlan.endDate}")

if st.button("Novo plano"):
    newPlan()
