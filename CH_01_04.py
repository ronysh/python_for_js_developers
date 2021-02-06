MY_NAME = "Ronnie"

def say_hi(name):
    "returns a string with a greeting"
    import ipdb; ipdb.set_trace()
    return f"Hi {name} 👋!"

import ipdb; ipdb.set_trace()

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age


mona = Pet("Mona", 6)

print(say_hi(MY_NAME))
