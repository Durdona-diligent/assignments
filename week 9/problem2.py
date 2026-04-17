from dataclasses import dataclass

"""Create a CoffeeOrder dataclass with four fields: drink (str), customer (str), size (str) with a default of "Medium", and price (float) with a default of 3.5."""

@dataclass
class CoffeeOrder:
    drink: str
    customer: str
    size: str = "Medium"
    price: float = 3.5

"""Create one order with all four values: "Latte", "Paul", "Large", 4.75."""

order1 = CoffeeOrder("Latte", "Paul", "Large", 4.75)

"""Create another order with only the required fields: "Espresso", "Chani"."""

order2 = CoffeeOrder("Espresso", "Chani")

print(order1)
print(order2)