import streamlit as st
from entities import *
from infrastructure import *


## operaçoes plano alimentar ##
# def updateMealPlan():
#     result = Api.getGenerateMealPlan(
#         "week",
#         2500,
#         st.session_state["user"].preferedDiet,
#         st.session_state["user"].intolerances,
#     ).json()
#     mealPlanItemList = []
#     for item in result["items"]:
#         print(item)
#         mpi = MealPlanItem.MealPlanItem(
#             item["slot"],
#             item["position"],
#             item["mealPlanId"],
#             item["type"],
#             item["day"],
#             item["value"],
#         )
#         mealPlanItemList.append(mpi)
#     st.session_state["user"].mealPlan = MealPlan.MealPlan("plano", mealPlanItemList)
#     userSerializer = Serializer.Serializer[User.User]()
#     userSerializer.serialize(st.session_state["user"])

st.title("Plano alimentar")

# if st.session_state["user"].mealPlan is None:
#     st.warning("Não há plano alimentar para este utilizador. Criar?")
#     st.button("Criar plano", on_click=updateMealPlan)
# else:
#     st.info("Plano OK")
