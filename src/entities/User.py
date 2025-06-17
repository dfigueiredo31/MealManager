class User:
    """User class"""

    def __init__(
        self,
        id: int,
        firstname: str = None,
        lastname: str = None,
        email: str = None,
        birthday: str = None,
        height: float = None,
        weight: float = None,
        preferedDiets: list = None,
        intolerances: list = None,
        mealPlans: list = None,
    ):
        """Initializes a User object

        Args:
            id (int): User id.
            firstname (str, optional): User's first name. Defaults to None.
            lastname (str, optional): User's last name. Defaults to None.
            email (str, optional): User's email. Defaults to None.
            age (int, optional): User's ages. Defaults to None.
            height (float, optional): User's height in meters. Defaults to None.
            weight (float, optional): User's weight in kilograms. Defaults to None.
            preferedDiet (list, optional): A list of the user's prefered diets. Defaults to None.
            intolerances (list, optional): A list of the user's food intolerances. Defaults to None.
        """
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.birthday = birthday
        self.height = height
        self.weight = weight
        self.preferedDiets = preferedDiets
        self.intolerances = intolerances
        self.mealPlans = mealPlans
