from datetime import date
from entities.MealPlanItem import MealPlanItem


class MealPlan:
    def __init__(
        self,
        id: int,
        startDate: date,
        endDate: date,
        mealPlanItems: dict[str, list[MealPlanItem]],
        name: str = None,
    ):
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
        self.mealPlanItems = mealPlanItems
        self.name = name
