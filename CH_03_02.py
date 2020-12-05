number = int(input("Pick any number:"))

if number < 0:
    print("Don't be so negative...")
elif number < 10:
    print("Between 0-10. Fair enough.")
elif number < 1_000_001:
    print("Good attitude.")
else:
    print("Don't be greedy.")
