def calculate_average_sales(sales_list):
    if not sales_list:
        return 0.0
    else:
        average = sum(sales_list) / len(sales_list)
        return average
        
def find_top_salesperson(sales_data):
    best_average = -1
    best_id = None
    for employee in sales_data:
        employee_id = employee[0]
        region = employee[1]
        quarterly_sales_list = employee[2]
        average = calculate_average_sales(quarterly_sales_list)
        if average > best_average:
            best_average = average
            best_id = employee_id
        elif average == best_average:
            if employee_id < best_id:
                best_id = employee_id
    return best_id

def get_employees_in_region(sales_data, region_name):
    employees_in_region = []
    for employee in sales_data:
        employee_id = employee[0]
        region = employee[1]
        if region == region_name:
            employees_in_region.append(employee_id)
    employees_in_region.sort()
    return employees_in_region

def get_regional_sales_total(sales_data):
    regions = []
    for employee in sales_data:
        region = employee[1]
        if region not in regions:
            regions.append(region)

    regional_totals = []
    for region in regions:
        total_sales = 0
        for employee in sales_data:
            if employee[1] == region:
                sales_list = employee[2]
                for sale in sales_list:
                    total_sales += sale
        regional_totals.append((region, total_sales))
    regional_totals.sort()
    return regional_totals

def analyze_sales_data(sales_data):
    top_salesperson = find_top_salesperson(sales_data)
    north_region_employees = get_employees_in_region(sales_data, 'North')
    regional_summary = get_regional_sales_total(sales_data)
    
    return (top_salesperson, north_region_employees, regional_summary)

sales_data = [
    ('E101', 'North', [50000, 60000, 55000]), # Avg: 55000
    ('E201', 'South', [70000, 75000, 80000]), # Avg: 75000
    ('E102', 'North', [85000, 90000, 95000]), # Avg: 90000
    ('E301', 'West', [65000, 60000, 58000])  # Avg: 61000
]

result = analyze_sales_data(sales_data)
print(result)
