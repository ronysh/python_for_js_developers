import time


class ShoppingCart:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)


class ClassRoom:
    def __init__(self):
        self.data = []


class VeggieMixin:
    veggies = ["tomatoes", "onions", "carrots", "brocholi"]


class SoupMixin:
    temprature = "199.4°F"
    water_percentage = 50
    cooking_time = 5


class SaladMixin:
    temprature = "41.0°F"
    water_percentage = 0
    cooking_time = 0


class FoodMixin:
    def make_food(self):
        time.sleep(self.cooking_time)
        print("Lunch's ready!")
        print(self.water_percentage, " percent water")
        print(self.temprature)


class VeggieSoup(VeggieMixin, SoupMixin, FoodMixin):
    pass


class VeggieSalad(VeggieMixin, SaladMixin, FoodMixin):
    pass


VeggieSoup().make_food()

VeggieSalad().make_food()
