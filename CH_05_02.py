NAMES = ["Jake", "Jay", "Jim", "Jill"]
AGES = [34, 25, 55, 42]

print("=====reversed(AGES:[34, 25, 55, 42])=====")

for num in reversed(AGES):
    print(num)

print("=====sorted(AGES)=====")

for num in sorted(AGES):
    print(num)

print("=====iterating zip(NAMES, AGES)=====")

for name, age in zip(NAMES, AGES):
    print(f"{name} is {age} years old.")

print("=====iterating index, name with enumerate=====")

for i, name in enumerate(NAMES):
    print(i, name)
