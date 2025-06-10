import json


class MealPlanItem:
    def __init__(
        self,
        timestamp: int,
        slot: int,
        position: int,
        itemType: str,
        value: dict,
        mealPlanId: int = None,
    ):
        self.timestamp = timestamp
        self.slot = slot
        self.position = position
        self.mealPlanId = mealPlanId
        self.itemType = itemType
        self.value = value
