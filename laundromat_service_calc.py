<<<<<<< HEAD
print('='*3, "Laundromat Service Calculator", '='*3)
print("Enter machine size: small, medium, or large")
print("Type 'done' when finished selecting loads\n")

price_small = 4.50
price_medium = 6.50
price_large = 9.00
subtotal = 0.0

while True:
    size = input("Enter machine size: ")
    if size == 'done':
        break
    if size == "small":
        subtotal = subtotal + price_small
        print(f"Price: ${price_small:.2f}")
    elif size == "medium":
        subtotal = subtotal + price_medium
        print(f"Price: ${price_medium:.2f}")
    elif size == "large":
        subtotal = subtotal + price_large
        print(f"Price: ${price_large:.2f}")
    print(f"Current total: ${subtotal:.2f}")
    print()
if subtotal >= 30:
    discount = 4.00
else:
    discount = 0.00

final_total = subtotal - discount
print()
print('='*3 + " Service Summary " + '='*3)
print(f"Current total: ${subtotal:.2f}")
print(f"Frequent Customer Discount: -${discount:.2f}")
print(f"Final total: ${final_total:.2f}")
print("Thank you for your business!")
=======
print('='*3, "Laundromat Service Calculator", '='*3)
print("Enter machine size: small, medium, or large")
print("Type 'done' when finished selecting loads\n")

price_small = 4.50
price_medium = 6.50
price_large = 9.00
subtotal = 0.0

while True:
    size = input("Enter machine size: ")
    if size == 'done':
        break
    if size == "small":
        subtotal = subtotal + price_small
        print(f"Price: ${price_small:.2f}")
    elif size == "medium":
        subtotal = subtotal + price_medium
        print(f"Price: ${price_medium:.2f}")
    elif size == "large":
        subtotal = subtotal + price_large
        print(f"Price: ${price_large:.2f}")
    print(f"Current total: ${subtotal:.2f}")
    print()
if subtotal >= 30:
    discount = 4.00
else:
    discount = 0.00

final_total = subtotal - discount
print()
print('='*3 + " Service Summary " + '='*3)
print(f"Current total: ${subtotal:.2f}")
print(f"Frequent Customer Discount: -${discount:.2f}")
print(f"Final total: ${final_total:.2f}")
print("Thank you for your business!")
>>>>>>> 5345afa9507b7bbe13b3120f2e8fd61b8d0ae582
