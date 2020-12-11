
def add_greet(func):
    name = func()
    print(f"hey {name}!")

def get_name():
    return "Terry"

add_greet(get_name)

@add_greet
def get_name():
    return "Terry"