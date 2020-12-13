zero_to_nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=====iterating [0, ..., 9]=====")

for num in zero_to_nine:
    print(num)


print("=====using range=====")

for num in range(9):
    print(num)

print("=====iterating zip(NAMES, AGES)=====")

NAMES = ["Jake", "Jay", "Jim", "Jill"]
AGES = [34, 25, 55, 42]

for name, age in zip(NAMES, AGES):
    print(f"{name} is {age} years old.")
