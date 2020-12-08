NAME = "Ronnie"

greet = f"Hi {NAME}!"

formal_greet = greet.replace("Hi", "Greetings")

string_contains_name = NAME in greet  # True

string_starts_with_hi = greet.startswith("Hi")  # True

string_ends_with_hi = greet.endswith("Hi")  # False

print("greet                 :", greet)
print("formal_greet          :", formal_greet)
print("string_contains_name  :", string_contains_name)
print("string_starts_with_hi :", string_starts_with_hi)
print("string_ends_with_hi   :", string_ends_with_hi)
