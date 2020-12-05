MY_NAME = "Ronnie"


def say_hi(name):
    return f"Hi {name} 👋!"


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


mona = Pet("Mona", 6)

print(say_hi(MY_NAME))
