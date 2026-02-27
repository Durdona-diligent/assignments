def calculate_bid(bid_text):
    lines = bid_text.split('\n')
    subtotal = 0
    deposit = 0
    fee = 0
    for line in lines:
        if "hrs at" in line:
            parts_t = line.split()
            hours = float(parts_t[2])
            rate = float(parts_t[5].replace("$", "").replace("/hr", ""))
            subtotal += hours * rate
        elif "FEE:" in line:
            parts_f = line.split()
            fee = float(parts_f[1].replace("%", "")) / 100
        elif "DEPOSIT:" in line:
            parts_d = line.split()
            deposit = float(parts_d[1].replace("$", ""))
    total = (subtotal - deposit) * (1 + fee)
    return f"${total:.2f}"




# Test Case 1: Standard bid
bid1 = """Framing -> 10 hrs at $50.00/hr
Wiring -> 5 hrs at $80.00/hr
FEE: 10%
DEPOSIT: $100.00"""
print(calculate_bid(bid1))

# Test Case 2: No deposit
bid2 = """Plumbing -> 2 hrs at $100.00/hr
Cleanup -> 1 hrs at $20.00/hr
FEE: 5%"""
print(calculate_bid(bid2))

# Test Case 3: Deposit, no fee
bid3 = """Painting -> 4 hrs at $25.00/hr
Sanding -> 2 hrs at $15.00/hr
DEPOSIT: $30.00
FEE: 0%"""
print(calculate_bid(bid3))