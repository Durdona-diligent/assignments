print('='*4, "UNIVERSITY BOOKSTORE CHECKOUT", '='*4,")
print()
customer_name = input("Enter you name: ")
is_faculty_staff = 'no'
is_textbook_order = 'yes'

book1_title = input("Enter title for Book 1: ")
book1_price = float(input("Enter price for Book 1: "))
book1_qty = int(input("Enter quantity for Book 1: "))

book2_title = input("Enter title for Book 2: ")
book2_price = float(input("Enter price for Book 2: "))
book2_qty = int(input("Enter quantity for Book 2: "))

book3_title = input("Enter title for Book 3: ")
book3_price = float(input("Enter price for Book 3: "))
book3_qty = int(input("Enter quantity for Book 3: "))

subtotal = book1_price * book1_qty + book2_price * book2_qty + book3_price * book3_qty

number_of_books = book1_qty + book2_qty + book3_qty

faculty_staff_eligibility = is_faculty_staff == 'yes'
faculty_staff_discount = faculty_staff_eligibility * subtotal * 0.20 

textbook_discount_eligibility = is_textbook_order == 'yes'
textbook_discount = textbook_discount_eligibility * subtotal * 0.25 

bulk_book_discount_eligibility = number_of_books >= 10
bulk_discount = bulk_book_discount_eligibility * subtotal * 0.08

main_discount = faculty_staff_eligibility * (faculty_staff_discount >= textbook_discount) + textbook_discount_eligibility * (textbook_discount > faculty_staff_discount)
subtotal_after_main_discounts = subtotal - main_discount
small_order_fee = (number_of_books < 3) * 10000
subtotal_after_discounts = subtotal - bulk_discount - main_discount
total_before_tax = subtotal_after_discounts + small_order_fee
tax = (is_textbook_order == 'no') * 0.05 * subtotal_after_discounts
shipping = (total_before_tax < 200000) * 20000
subtotal_after_discounts_and_fees = subtotal - main_discount + small_order_fee + shipping
final_total = total_before_tax + tax + shipping
net_savings = subtotal - final_total

print("Customer name:", customer_name)
print("Faculty status:", is_faculty_staff)
print("Textbook order status:", is_textbook_order)
print("items: {}, {} sum, {} pieces; {}, {} sum, {} pieces; {}, {} sum, {} pieces".format(book1_title,
                                                                                          book1_price,
                                                                                          book1_qty,
                                                                                          book2_title,
                                                                                          book2_price,
                                                                                          book2_qty,
                                                                                          book3_title,
                                                                                          book3_price,
                                                                                          book3_qty)) 
print("Subtotal before discounts:", subtotal)
print("Faculty discount eligibility: {} and {}".format(faculty_staff_eligibility, faculty_staff_discount))
print("Textbook discount eligibility: {} and {}".format(textbook_discount_eligibility, textbook_discount))
print("Which discount was applied:", main_discount)
print("Bulk discount eligibility: {} and {}".format(bulk_book_discount_eligibility, bulk_discount))
print("Total discounts: {}".format(main_discount + bulk_discount))
print(f"Small order fee: {small_order_fee * (small_order_fee > 0)}")
print("Subtotal after discounts and fees: {}".format(subtotal_after_discounts_and_fees))
print("Tax amount:", tax)
print("Textbook tax exemption:", is_textbook_order == 'yes')
print("Shipping cost:", shipping)
print("Free shipping:", total_before_tax >= 200000)
print("Final Total:", final_total)

print("Net savings or extra fees: {}".format(net_savings))
