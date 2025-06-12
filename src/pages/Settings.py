import streamlit as st
from entities import *
from infrastructure import *

## Settings page ##
user = st.session_state["user"]

st.title("Definições")

st.subheader("Utilizador")
with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        user.firstname = st.text_input("Primeiro nome", value=user.firstname)
        user.lastname = st.text_input("Apelido", value=user.lastname)
        user.email = st.text_input("E-mail", value=user.email)
    with col2:
        user.preferedDiet = st.selectbox(
            "Preferencias alimentares?",
            Diet.AvailableDiets,
            (
                Diet.AvailableDiets.index(user.preferedDiet)
                if user.preferedDiet is not None
                else None
            ),
        )
        user.intolerances = st.multiselect(
            "Intolerancias alimentares?", Diet.Intolerances, user.intolerances
        )
    with col3:
        user.age = st.number_input("Idade", 0, 100, value=user.age)
        user.height = st.slider("Altura", 1.0, 2.5, value=user.height)
        user.weight = st.slider("Peso", 10.0, 200.0, value=user.weight)

st.subheader("Aplicação")
with st.container(border=True):
    if st.button("Logout"):
        st.logout()
