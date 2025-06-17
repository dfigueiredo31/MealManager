import streamlit as st
from entities import *
from infrastructure import *

## Settings page ##
user = Db.getUser(st.user["email"])
diets = Db.getDiets()
intolerances = Db.getIntolerances()

st.write(user.__dict__)

st.title("Definições")

st.subheader("Utilizador")
with st.form("userform", border=True):
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Nome", value=f"{user.firstname} {user.lastname}", disabled=True)
        st.text_input("E-mail", value=user.email, disabled=True)

        selectedDiets = st.multiselect(
            "Preferencias alimentares?",
            map(lambda x: x.description, diets),
            map(lambda x: x.description, user.preferedDiets),
        )

        user.preferedDiets = [
            diet for diet in diets if diet.description in selectedDiets
        ]

        selectedIntolerances = st.multiselect(
            "Intolerancias alimentares?",
            map(lambda x: x.description, intolerances),
            map(lambda x: x.description, user.intolerances),
        )

        user.intolerances = [
            intolerance
            for intolerance in intolerances
            if intolerance.description in selectedIntolerances
        ]

    with col2:
        user.birthday = st.date_input(
            "Data nascimento",
            value=user.birthday,
            min_value="1900-01-01",
            max_value="today",
        )
        user.height = st.slider("Altura", 1.0, 2.5, value=user.height)
        user.weight = st.slider("Peso", 10.0, 200.0, user.weight, 0.5)

    if st.form_submit_button("Guardar"):
        Db.updateUser(user)

st.subheader("Aplicação")
with st.container(border=True):
    if st.button("Logout"):
        st.logout()
    if st.button("Remover dados utilizador"):
        st.logout()
        Db.deleteAllData()
