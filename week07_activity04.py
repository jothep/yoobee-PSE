from abc import ABC, abstractmethod

class logistics(ABC):
   @abstractmethod
   def logistics(self, transit):
      pass
   
class RoadLogistics(logistics):
   def logistics(self, transit):
      return f"{transit} transited by road."
   
class SeaLogistics(logistics):
   def logistics(self, transit):
      return f"{transit} transited by sea."

class transitFactory:
    _transitType = {
        "vehicle": RoadLogistics,
        "ship": SeaLogistics
    }

    @classmethod
    def create_transit(cls, transit_type: str):

        transit_class = cls._transitType.get(transit_type.lower())

        if not transit_class:
            raise ValueError(f"Unknown transit method: {transit_type}.")
        return transit_class()

class CustomsInspection:
    _instance = None
   
    def __new__(cls):
        if cls._instance is None:
            print("Create CustomsInspection new instance...")
            cls._instance = super().__new__(cls)
        else:
            print("Instance exists，return...")
        return cls._instance

    def inspect(self, transitType: str, logistics):
        inspection = transitFactory.create_transit(transitType)
        return inspection.logistics(logistics)

if __name__ == "__main__":
    transit1 = CustomsInspection()
    print(transit1.inspect("vehicle", "truck"))
    print(transit1.inspect("ship", "boat"))