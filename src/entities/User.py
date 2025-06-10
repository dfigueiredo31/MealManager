from entities import MealPlan


class User:

    def __init__(
        self,
        username: str = None,
        firstname: str = None,
        lastname: str = None,
        email: str = None,
        age: int = None,
        height: float = None,
        weight: float = None,
        preferedDiet: str = None,
        intolerances: list = None,
        spoonacularPassword: str = None,
        hash: str = None,
        mealPlan: MealPlan.MealPlan = None,
    ):
        """Initializes a User obj

        Args:
            username (str): username
            firstname (str): first name
            lastname (str): last name
            email (str): user email
            spoonacularPassword (str): spoonacular password
            hash (str): user hash
        """
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age
        self.height = height
        self.weight = weight
        self.preferedDiet = preferedDiet
        self.intolerances = intolerances
        self.spoonacularPassword = spoonacularPassword
        self.hash = hash
        self.mealPlan = mealPlan

    def __str__(self):
        return (
            f"username: {self.username}\n"
            f"firstname: {self.firstname}\n"
            f"lastname: {self.lastname}\n"
            f"email: {self.email}\n"
            f"age: {self.age}\n"
            f"height: {self.height}\n"
            f"weight: {self.weight}\n"
            f"preferedDiet: {self.preferedDiet}\n"
            f"intolerances: {self.intolerances}\n"
            f"spoonacularPassword: {self.spoonacularPassword}\n"
            f"hash: {self.hash}\n"
        )
