from decimal import Decimal

USER_NAME = "Jake"
CREDITS = Decimal("2.2")
ITEMS_IN_CART = ["Jeans", "Shoes", "Socks"]

def get_first_item(user, credits, items):
    return f"first item: {items[0]} user: {user} credits left: {credits}"

print(get_first_item(USER_NAME, CREDITS, ITEMS_IN_CART))
