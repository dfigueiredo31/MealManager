from datetime import date


class MealPlanItem:
    def __init__(
        self,
        id: int,
        title: str,
        date: date,
        externalId: str = None,
        image: str = None,
    ):
        self.id = id
        self.title = title
        self.date = date
        self.externalId = externalId
        self.image = image
