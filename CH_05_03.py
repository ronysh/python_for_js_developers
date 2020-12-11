FRIENDS = [
    {"name": "Graham"},
    {"name": "John"}, 
    {"name": "Terry"}, 
    {"name": "Eric"}, 
    {"name": "Michael"}
]

NAME_STRINGS = [friend["name"] for friend in FRIENDS]

NAMES_WITH_E = [string for string in NAME_STRINGS if "e" in string]

print("          =====NAME_STRINGS=====")
print(NAME_STRINGS)


print("          =====NAMES_WITH_E=====")
print(NAMES_WITH_E)