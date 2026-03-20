#Decorator with Arguments
def log_purchase(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Purchase recorded.")
        result = func(*args, **kwargs)
        return result
    return wrapper
    
@log_purchase
def buy(item, price):
    return f"Bought {item} for ${price}"


print(buy("Laptop", 999))
print(buy("Mouse", 25))