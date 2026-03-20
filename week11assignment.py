def book_session(members_db, schedule_db, member_id, class_name, spots):
    if member_id not in members_db:
        raise KeyError("Member ID not found")
    if class_name not in schedule_db:
        raise KeyError ("Class not found") 
    if not isinstance(spots, int) or spots < 1:
        raise ValueError ("Spots must be positive integer")
    cost_per_spot = schedule_db[class_name]["cost"]
    total_cost = spots * cost_per_spot 
    if members_db[member_id]["pass_type"] == "Premium":
        total_cost = 0
    if members_db[member_id]["credits"] < total_cost:
        raise ValueError("Insufficient credits")
    members_db[member_id]["credits"] -= total_cost
    return total_cost
def process_gym_bookings(members_db, schedule_db, booking_queue):
    credits_used = 0
    declined_bookings = 0
    d = {}
    for member_id,class_name,spots in booking_queue:
        try:
            cost = book_session(members_db, schedule_db, member_id, class_name, spots)
            credits_used += cost
        except (KeyError,ValueError) as message:
            print(f"Booking Error for {member_id}: {message}")
            declined_bookings  +=1
    d['credits_used']= credits_used
    d['declined_bookings'] = declined_bookings
    return d
    

# Format: {Class: {"cost": int}}
schedule = {
    "Yoga":   {"cost": 5},
    "Boxing": {"cost": 10}
}

# Format: {ID: {"credits": int, "pass_type": str}}
members = {
    "M1": {"credits": 20, "pass_type": "Standard"},
    "M2": {"credits": 5,  "pass_type": "Premium"} # Free classes
}

queue = [
    ("M1", "Yoga", 2),      # Valid. Cost: 10. Rem: 10.
    ("M2", "Boxing", 10),   # Valid. Cost: 0 (Premium). Rem: 5.
    ("M1", "Boxing", 2),    # Error: Cost 20 > 10.
    ("M9", "Zumba", 1),     # Error: Member ID not found.
    ("M1", "Pilates", 1),   # Error: Class not found.
    ("M2", "Yoga", 0)       # Error: Spots must be positive integer.
]
print(process_gym_bookings(members, schedule, queue))

             
             

            