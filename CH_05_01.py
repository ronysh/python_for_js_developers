zero_to_nine = [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print("=====iterating [0, ..., 9]=====")

for num in zero_to_nine:
    print(num)

print("=====using make_range=====")

def make_range(num):
    if num < 0:
        raise Exception("number is too small.")
    count = 0
    while count < num:
        yield count
        count += 1


for num in make_range(9):
    print(num)

print("=====using range=====")

for num in range(9):
    print(num)

print("=====iterating zip(NAMES, AGES)=====")

NAMES = ["Jake", "Jay", "Jim", "Jill"]
AGES = [34, 25, 55, 42]

for name, age in zip(NAMES, AGES):
    print(f"{name} is {age} years old.")

print("=====iterating index, name with enumerate=====")

for i, name in enumerate(NAMES):
    print(i, name)

print("=====reversed(zero_to_nine)=====")

for num in reversed(zero_to_nine):
    print(num)

print("=====sorted(AGES)=====")

for num in sorted(AGES):
    print(num)
