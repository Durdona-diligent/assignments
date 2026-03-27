#Recipe Ingredient Combiner
class Ingredient:
    def __init__(self, name: str, amount: int, unit: str):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return f"{self.amount}{self.unit} of {self.name}"
    
    def __add__(self, other):
        if isinstance(other, Ingredient):
            if self.name == other.name and self.unit == other.unit:
                added_amount = self.amount + other.amount
                return (self.name, added_amount, self.unit)
            return NotImplemented
        return NotImplemented
    
class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []