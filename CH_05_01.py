def make_range(num):
    if num < 0:
        raise Exception("number is too small.")
    count = 0
    while count < num:
        yield count
        count += 1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for num, letter in zip(numbers, letters):
    print(num, letter)

for i, letter in enumerate(letters):
    print(i, letter)

for letter in reversed(letters):
    print(letter)

for letter in sorted([2, 3, 9, 1]):
    print(letter)
