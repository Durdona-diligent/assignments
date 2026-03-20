from abc import ABC, abstractmethod

class Priceable(ABC):
    @abstractmethod
    def service_fee(self):
        pass

class Formattable(ABC):
    @abstractmethod
    def format_ticket(self):
        pass

class Ticket(Priceable, Formattable):
    def __init__(self, event, price):
        super().__init__()
        self.event = event
        self.price = price

        if self.price < 0:
            raise ValueError(f"Invalid price: {self.price}")
        
    def service_fee(self):
        return round(self.price * 0.12, 2)
        
    def format_ticket(self):
        return f"{self.event}: ${self.price:.2f}"
        
class EarlyBirdTicket(Ticket):
    def __init__(self, event, price, discount): #(a float between 0 and 1)
        super().__init__(event, price)
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 1:
            self._discount = value
        else:
            raise ValueError('Discount must be between 0 and 1')
        
    def final_price(self):
        return round(self.price * (1 - self.discount), 2)
    
    def service_fee(self):
        return round(self.final_price() * 0.12, 2)
    
    def format_ticket(self):
        f_discount = int(self.discount * 100)
        return f"{self.event}: ${self.price:.2f} -> ${self.final_price():.2f} (-{f_discount})"
    
t = Ticket("Concert", 120.00)
print("Ticket service fee :", t.service_fee())          # expect 120 * .12 = 14.40
print("Ticket format      :", t.format_ticket())        # "Concert: $120.00"

# 2️⃣  Early‑bird ticket (20 % discount)
e = EarlyBirdTicket("Concert", 120.00, 0.20)   # 20 % off → final price 96.00
print("EarlyBird final price :", e.final_price())      # expect 96.00
print("EarlyBird service fee :", e.service_fee())      # 12 % of 96 → 11.52
print("EarlyBird format      :", e.format_ticket())    # "Concert: $120.00 -> $96.00 (-20%)"