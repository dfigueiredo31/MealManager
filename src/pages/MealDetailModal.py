import streamlit as st
import datetime as dt


@st.dialog("Detalhe")
def mealDetailModal(recipe):
    st.subheader(recipe["title"])
    st.json(recipe, expanded=False)
    st.image(recipe["image"], use_container_width=True)
    st.html(
        recipe["summary"],
    )
    with st.expander("Ingredientes"):
        for ingrediente in recipe["nutrition"]["ingredients"]:
            st.caption(ingrediente["name"])

    with st.expander("Declaração nutricional"):
        declaracaoNutricional = list(
            recipe["nutrition"]["nutrients"][i] for i in [0, 1, 3, 7, 10]
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
                    st.progress(
                        (
                            infoNutricional["percentOfDailyNeeds"]
                            if infoNutricional["percentOfDailyNeeds"] <= 100
                            else 100
                        )
                        / 100
                    )

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
            # refeicao = MealPlanItem.MealPlanItem(
            #     timestamp,
            #     slot,
            #     position,
            #     "RECIPE",
            #     {
            #         "id": receita["id"],
            #         "servings": receita["servings"],
            #         "title": receita["title"],
            #         "imageType": receita["imageType"],
            #     },
            # )
            # st.form_submit_button(
            #     "Adicionar",
            #     on_click=Api.postAddToMealPlan,
            #     args=[st.session_state["user"], refeicao],
            # )
