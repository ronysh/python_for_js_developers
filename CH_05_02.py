
print("=====iterating zip(NAMES, AGES)=====")

NAMES = ["Jake", "Jay", "Jim", "Jill"]
AGES = [34, 25, 55, 42]

for name, age in zip(NAMES, AGES):
    print(f"{name} is {age} years old.")

print("=====iterating index, name with enumerate=====")

for i, name in enumerate(NAMES):
    print(i, name)

print("=====reversed([0 ,1, 2, 3, 4])=====")

for num in reversed([0 ,1, 2, 3, 4):
    print(num)

print("=====sorted(AGES)=====")

for num in sorted(AGES): # returns list
    print(num)

