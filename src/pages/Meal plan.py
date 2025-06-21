from threading import currentThread
import streamlit as st
import datetime as dt
from infrastructure import Db
from entities.MealPlan import MealPlan
from pages import SearchForm

## Meal plan page ##
user = Db.getUser(st.user["email"])


@st.dialog("Novo plano")
def newPlan():
    name = st.text_input("Nome do plano")
    startDate = st.date_input("Data inicio")
    endDate = st.date_input("Data fim")

    if st.button("Criar"):
        Db.addUserMealPlan(user, MealPlan(0, startDate, endDate, {}, name))
        st.rerun()


st.title("Plano alimentar")

if len(user.mealPlans) != 0:

    for mealPlan in user.mealPlans:
        st.subheader(f"{mealPlan.name}: {mealPlan.startDate} a {mealPlan.endDate}")

        startDate = dt.datetime.strptime(mealPlan.startDate, "%Y-%m-%d").date()
        endDate = dt.datetime.strptime(mealPlan.endDate, "%Y-%m-%d").date()
        numOfDays = (endDate - startDate).days + 1

        # numOfMealsInPlan = len(mealPlan.mealPlanItems)

        cols = st.columns(numOfDays)
        for item in range(numOfDays):
            timeDelta = dt.timedelta(days=item)
            with cols[item]:
                thisDate = startDate + timeDelta
                st.write(f"{dt.datetime.strftime(thisDate, "%A, %m/%d")}")
                # st.write(f"{thisDate}")

                currentDayItems = mealPlan.mealPlanItems.get(
                    thisDate.strftime("%Y-%m-%d")
                )

                if currentDayItems:
                    for item in currentDayItems:
                        st.image(item.image)
                        st.caption(item.title)

        # if numOfMealsInPlan > 0:

        #     for i in range(numOfMealsInPlan):
        #         st.write(mealPlan.mealPlanItems[i].title)
        # for mealPlanItem in mealPlan.mealPlanItems:
        #     st.write(mealPlanItem.title)
        #     st.write(mealPlanItem.date)
        #     st.write(mealPlanItem.image)
else:
    st.info("Não há nenhum plano criado para o utilizador.")

if st.button("Novo plano"):
    newPlan()
