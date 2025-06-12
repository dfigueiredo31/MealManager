import socket
import streamlit as st
import datetime as dt
from infrastructure import *
from entities import *


@st.dialog("Sugestão do dia")
def receitaModal(receita):
    st.subheader(receita["title"])
    st.json(receita, expanded=False)
    st.image(receita["image"], use_container_width=True)
    st.html(
        receita["summary"],
    )
    with st.expander("Ingredientes"):
        for ingrediente in receita["nutrition"]["ingredients"]:
            st.caption(ingrediente["name"])

    with st.expander("Declaração nutricional"):
        declaracaoNutricional = list(
            receita["nutrition"]["nutrients"][i] for i in [0, 1, 3, 7, 10]
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
                    st.progress(infoNutricional["percentOfDailyNeeds"] / 100)

    with st.expander("Adicionar ao plano"):
        with st.form("adicionar ao plano", border=False):
            # YYYY/MM/DD
            timestamp = int(
                dt.datetime.combine(st.date_input("Dia"), dt.time()).timestamp()
            )

            slot = ["Pequeno-almoço", "Almoço", "Jantar"].index(
                st.selectbox(
                    "Refeição",
                    ["Pequeno-almoço", "Almoço", "Jantar"],
                )
            )
            position = st.number_input("Posição", 0, step=1)

            # "value": {
            #     "id": 296213,
            #     "servings": 2,
            #     "title": "Spinach Salad with Roasted Vegetables and Spiced Chickpea",
            #     "imageType": "jpg",
            # }
            refeicao = MealPlanItem.MealPlanItem(
                timestamp,
                slot,
                position,
                "RECIPE",
                {
                    "id": receita["id"],
                    "servings": receita["servings"],
                    "title": receita["title"],
                    "imageType": receita["imageType"],
                },
            )
            st.form_submit_button(
                "Adicionar",
                on_click=Api.postAddToMealPlan,
                args=[st.session_state["user"], refeicao],
            )


def meusDados():
    # bmi = massa (kg) / altura^2
    bmi = round(
        st.session_state["user"].weight / pow(st.session_state["user"].height, 2), 2
    )

    st.header("Os meus dados")
    st.text(f"Idade: {st.session_state["user"].age}")
    st.text(f"Peso: {st.session_state["user"].weight} kg")
    st.text(f"Altura: {st.session_state["user"].height} m")
    st.text(f"BMI: {bmi}")


def sugestaoDoDia():
    receita = Api.getRecipes(
        "main dish",
        st.session_state["user"].preferedDiet,
        st.session_state["user"].intolerances,
        [],
        [],
        False,
        False,
        False,
        False,
        True,
        45,
        1,
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
    st.button("Ver mais", on_click=receitaModal, args=[receita])


## pagina ##
col1, col2, col3 = st.columns(3, border=True)

with col1:
    sugestaoDoDia()
with col2:
    st.user
with col3:
    st.session_state["user"]
