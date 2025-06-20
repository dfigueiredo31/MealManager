import streamlit as st
from pages import MealDetail
from infrastructure import *
from entities import *

## Home page ##
user = Db.getUser(st.user["email"])


def sugestaoDoDia():
    receita = Api.getRecipes(
        "main dish",
        list(map(lambda x: x.description, user.preferedDiets)),
        list(map(lambda x: x.description, user.intolerances)),
        [],
        [],
        False,
        False,
        False,
        False,
        True,
        45,
        1,
        "",
    ).json()["results"][0]

    st.header("Sugestão do dia")
    st.subheader(receita["title"])
    st.image(
        receita["image"],
        use_container_width=True,
    )

    st.text(f"🏷️ {", ".join(receita["dishTypes"])}")
    st.text(
        f"🌍 {", ".join(receita["cuisines"])}" if len(receita["cuisines"]) > 0 else ""
    )
    st.text(f"👍 {receita["aggregateLikes"]}")
    st.button(
        "Ver mais",
        on_click=MealDetail.displayMealDetail,
        args=[receita, "modal", True, False, False, True, True, False, True],
    )


## pagina ##
col1, col2, col3 = st.columns(3, border=True)

with col1:
    sugestaoDoDia()
with col2:
    st.user
with col3:
    # st.session_state["user"]
    pass
