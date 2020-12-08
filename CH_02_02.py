from decimal import Decimal

print(type(1))
print(type(0.5))
unexpected = 0.2 + 0.1
expected = Decimal("0.2") + Decimal("0.1")
print(type(Decimal(0.5)))
print(f"Outcome using float 0.2 + 0.1 = {unexpected}")
print(f"Outcome using decimal Decimal('0.2') + Decimal('0.1') = {expected}")
