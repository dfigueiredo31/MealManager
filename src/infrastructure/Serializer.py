import json


class Serializer[T]:
    def serialize(self, o):
        genericType = self.__orig_class__.__args__[0]
        fileName = f"{genericType.__name__}.json"

        with open(fileName, "w") as file:
            json.dump(o.__dict__, file, default=lambda o: o.__dict__, indent=3)

    def deserialize(self):
        genericType = self.__orig_class__.__args__[0]
        fileName = f"{genericType.__name__}.json"

        with open(fileName, "r") as file:
            data = json.load(file)
            return genericType(**data)
