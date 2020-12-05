from decimal import Decimal

user_name = "Jake"
credits = Decimal("2.2")
items_in_cart = ["Jeans", "Shoes", "Socks"]


def get_first_item(user, credits, items):
    return f"first item: {items[0]} user: {user} credits left: {credits}"


print(get_first_item(user_name, credits, items_in_cart))
