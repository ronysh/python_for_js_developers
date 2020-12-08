"""
* lists may be modiefied
* tuples are leaner and immutable
"""

names = ["Ronnie", "Mona", "Jack"]

names[2] = "Fred"

print(names)

result = 1 in [1, 2, 3, 4, 5] # True

print(result)

print("==========")

names_tuple = (
    "Ronnie",
    "Mona",
    "Jack",
)
print("==========")
names_age_dictionary = {"Jack": 20, "Jill": 21, "Hill": 1000}

print('{"Jack": 20, "Jill": 21, "Hill": 1000}')
print(names_age_dictionary["Jack"])

print(names_age_dictionary["Jill"])
# print(names_age_dictionary.Hill)

print("==========")

# this will result in an error
names_tuple[2] = "Fred"

