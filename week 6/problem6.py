#Repeat Decorator & All Three Method Types
def repeat(n):
    def decorator(func):
        def wrapper(self):
            for _ in range(n):
                result = func(self)
            return result
        return wrapper
    return decorator


class GymMember:
    _total = 0
    def __init__(self, name: str, membership: str):
        self.name = name
        self.membership = membership
        GymMember._total += 1
    
    @staticmethod
    def is_valid_membership(membership):
        return membership in ["basic", "standard", "premium"]
    
    @classmethod
    def get_total(cls):
        return cls._total
    
    @repeat(2)
    def greet(self):
        print(f"Welcome, {self.name}! ({self.membership} member)")

print(GymMember.is_valid_membership("premium"))
print(GymMember.is_valid_membership("vip"))

m1 = GymMember("Dilshod", "basic")
m2 = GymMember("Malika", "premium")

m1.greet()
m2.greet()

print(f"Total members: {GymMember.get_total()}")