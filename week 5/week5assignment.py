#Event Ticket Pricing
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

    # @property
    # def discount(self):
    #     return self._discount

    # @discount.setter
    # def discount(self, value):
    #     if 0 <= value <= 1:
    #         self._discount = value
    #     else:
    #         raise ValueError('Discount must be between 0 and 1')
        
    def final_price(self):
        return round(self.price * (1 - self.discount), 2)
    
    def service_fee(self):
        return round(self.final_price() * 0.12, 2)
    
    def format_ticket(self):
        f_discount = int(self.discount * 100)
        return f"{self.event}: ${self.price:.2f} -> ${self.final_price():.2f} (-{f_discount}%)"

class PremiumTicket(Ticket):
    def __init__(self, event, price, vip_surcharge: float):
        super().__init__(event, price)
        self.vip_surcharge = vip_surcharge

    def service_fee(self):
        return round(self.price * 0.12 + self.price * self.vip_surcharge, 2)
    
    def format_ticket(self):
        return f"{self.event}: ${self.price:.2f} (premium, sucharge int({self.vip_surcharge}%)"

class CompPass:
    def __init__(self, event, price: 0):
        self.event = event
        self.price = price
    
    def service_fee(self):
        return 0.0
    
    def format_ticket(self):
        return f"{self.event}: $0.00 (complimentary)"
    
class Invoice: #that stores a list of lines
    def __init__(self):
        self.lines = [] # [(x,y),(x,y),(),()...]
    
    def add_line(self, description, fee):
        self.lines.append((description, fee))

    def print_invoice(self):
        for line in self.lines:
            print(f"{line[0]} | fee: ${line[1]}")
        
class TicketOrder:
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.tickets = []
        self.invoice = Invoice()

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def finalize(self):
        print(f"Order for {self.buyer_name}")

        subtotal = 0.0
        total_fees = 0.0

        for ticket in self.tickets:
            desc = ticket.format_ticket()
            print(f'  {desc}')
            #print("  "+desc) 
            current_fee = ticket.service_fee()
            self.invoice.add_line(desc, current_fee)
            subtotal += ticket.price
            total_fees += ticket.service_fee()
        self.invoice.print_invoice
        grand_total = subtotal + total_fees
        print(f"Subtotal: ${subtotal:.2f}", f"\nTotal Fees: ${total_fees:.2f}", f"\nGrand Total: ${grand_total:.2f}")

order = TicketOrder('Nodira')

order.add_ticket(Ticket('Rock Concert', 80))
order.add_ticket(EarlyBirdTicket('Jazz Night', 120, 0.20))
order.add_ticket(PremiumTicket('Opera Gala', 200, 0.30))
order.add_ticket(CompPass('Staff Meeting', 0))

try:
    order.add_ticket(Ticket('Bad Event', -10))
except ValueError as e:
    print(f'Skipped: {e}')

order.finalize()

try:
    p = Priceable()
except TypeError:
    print('Cannot instantiate abstract class')