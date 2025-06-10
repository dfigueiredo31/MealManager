import streamlit as st
from entities import *
from infrastructure import *


## operações update user ##
def updateUserStatus(user: User.User):
    userSerializer = Serializer.Serializer[User.User]()
    userSerializer.serialize(user)
    st.session_state["user"] = user


def updateUserApiStatus(user: User.User):
    response = Api.postUser(user)
    if response.status_code == 200:
        responseAux = response.json()
        user.username = responseAux["username"]
        user.spoonacularPassword = responseAux["spoonacularPassword"]
        user.hash = responseAux["hash"]
        updateUserStatus(user)


## forms user ##
def userForm(isCreateUserForm: bool, user: User.User = None):

    if isCreateUserForm:
        user = User.User()

    with st.form("dados user", enter_to_submit=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            user.firstname = st.text_input("Primeiro nome", value=user.firstname)
            user.lastname = st.text_input("Apelido", value=user.lastname)
            user.email = st.text_input("E-mail", value=user.email)
            st.form_submit_button(
                "Atualizar",
                on_click=st.toast,
                args=["Dados do utilizador atualizados"],
            )

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

    updateUserStatus(user)


def userApiDisplay(user: User.User):
    with st.container(border=True):
        if user.hash is not None:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.text_input("Username", value=user.username)
            with col2:
                st.text_input(
                    "Spoonacular password",
                    value=user.spoonacularPassword,
                    type="password",
                )
            with col3:
                st.text_input("Hash", value=user.hash, disabled=True)
        else:
            with st.spinner("A carregar dados da API"):
                updateUserApiStatus(user)
                st.toast("Dados do utilizador atualizados")
                st.rerun()


## pagina ##
st.title("Perfil")

if st.session_state["user"] is None:
    userForm(True)
else:
    userForm(False, st.session_state["user"])
    userApiDisplay(st.session_state["user"])
