import requests
from typing import Literal

## Request header ##

headers = {
    "x-rapidapi-key": "",  # ToDo API secret
    "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "Content-Type": "application/json",
}

## POST ##


def postUser(user):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/users/connect"

    payload = {
        # "username": user.username,
        "firstName": user.firstname,
        "lastName": user.lastname,
        "email": user.email,
    }

    return requests.post(url, json=payload, headers=headers)


def postAddToMealPlan(user, mealPlanItem):
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/{user.username}/items"

    querystring = {"hash": user.hash}

    payload = {
        "date": mealPlanItem.timestamp,
        "slot": mealPlanItem.slot,
        "position": mealPlanItem.position,
        "type": mealPlanItem.itemType,
        "value": mealPlanItem.value,
    }

    return requests.post(url, json=payload, headers=headers, params=querystring)


## GET ##


def getRecipes(
    query: str,
    diet: str,
    intolerances: list,
    includeIngredients: list,
    excludeIngredients: list,
    instructionsRequired: bool,
    fillIngredients: bool,
    addRecipeInformation: bool,
    addRecipeInstructions: bool,
    addRecipeNutrition: bool,
    maxReadyTime: int,
    number: int,
    sort="max-used-ingredients",
):
    """Obtem receitas/pratos de acordo com os parametros dados

    Args:
        query (str): _description_
        diet (str): _description_
        intolerances (list): _description_
        includeIngredients (list): _description_
        excludeIngredients (list): _description_
        instructionsRequired (bool): _description_
        fillIngredients (bool): _description_
        addRecipeInformation (bool): _description_
        addRecipeInstructions (bool): _description_
        addRecipeNutrition (bool): _description_
        maxReadyTime (int): _description_
        number (int): _description_
        sort (str, optional): _description_. Defaults to "max-used-ingredients".

    Returns:
        response: _description_
    """
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    querystring = {
        "query": query,
        "diet": diet,
        "intolerances": intolerances,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "instructionsRequired": instructionsRequired,
        "fillIngredients": fillIngredients,
        "addRecipeInformation": addRecipeInformation,
        "addRecipeInstructions": addRecipeInstructions,
        "addRecipeNutrition": addRecipeNutrition,
        "maxReadyTime": maxReadyTime,
        # "ignorePantry": "true",
        "sort": sort,
        "number": number,
    }

    return requests.get(url, headers=headers, params=querystring)


def getRecipeInformation(id):
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"

    return requests.get(url, headers=headers)


# def getGenerateMealPlan(
#     timeFrame: Literal["day", "week"],
#     targetCalories: int,
#     diet: str,
#     exclude: list,
# ):
#     url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

#     querystring = {
#         "timeFrame": timeFrame,
#         "targetCalories": targetCalories,
#         "diet": diet,
#         "exclude": exclude,
#     }

#     return requests.get(url, headers=headers, params=querystring)
