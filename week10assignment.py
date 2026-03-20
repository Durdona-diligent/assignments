def group_expenses(transaction_list):
    expense_dict = {}
    for transaction in transaction_list:
        date, category, cost = transaction.split("/")
        cost = float(cost)
        if category not in expense_dict:
            expense_dict[category] = []
        expense_dict[category].append((date, cost))
    return expense_dict 

def summarize_budget(expense_dict):
    for category in expense_dict:
        total_cost = 0
        for date, cost in expense_dict[category]:
            total_cost += cost
        print(f"{category}: ${total_cost:.2f} total")
        
transaction_list = [
    "01-Oct/Food/15.50",
    "02-Oct/Gas/40.00",
    "03-Oct/Food/12.25",
    "04-Oct/Rent/800.00",
    "05-Oct/Gas/35.00",
    "05-Oct/Food/8.75"
]
expenses = group_expenses(transaction_list)
summarize_budget(expenses)
