# Gift Card Manager
class GiftCard:
    def __init__(self, code, balance):
        self._code = code
        self.balance = balance

    @property
    def code(self):
        return self._code
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def spend(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

card = GiftCard("AMZ-123", 50.0)
print(card.code)
print(card.balance)

card.spend(20.0)
print(card.balance)

try:
    card.spend(100.0)
except ValueError as e:
    print(e)

try:
    card.balance = -10.0
except ValueError as e:
    print(e)

try:
    card.code = "NEW-CODE"
except AttributeError:
    print("Cannot change code")
