#Simple Decorator
def announce(func):
    def wrapper():
        print("🍽️ NOW SERVING 🍽️")
        func()
        print("─" * 20)
    return wrapper

@announce
def dish():
    print("Go'mma")
    print("Baliq")
    print("Lag'mon")
    print("Sezar")
    print("Sushi")


dish()
print("Do you wanna eat for Iftar and study together after that?\n")