class Toppings:
    def __init__(self):
        self.items = ["tomatoe sauce", "peppers", "olives"]

    def __len__(self):
        return len(self.items)


class Dough:
    def __add__(self, other):
        if type(other) == Toppings:
            print("Did someone say pizza 🍕🍕🍕")


dough = Dough()
toppings = Toppings()
print(f"There are {len(toppings)} toppings.")
dough + toppings
