from datetime import date


class MealPlan:
    def __init__(self, id: int, startDate: date, endDate: date, name: str = None):
        """Initializes a MealPlan object

        Args:
            id (int): MealPlan id
            startDate (date): Day the plan starts
            endDate (date): Day the plan ends
            name (str, optional): Optional description/plan name. Defaults to None.
        """
        self.id = id
        self.startDate = startDate
        self.endDate = endDate
        self.name = name
