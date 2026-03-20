def process_donations(filename):
    cause_totals = {}
    top_donors = []
    
    with open(filename, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(',')
                donor = parts[0]
                cause = parts[1]
                cash = float(parts[2])
                check = float(parts[3])
            except ValueError:
                continue
            total = cash + check
            if cause not in cause_totals:
                cause_totals[cause] = 0
            cause_totals[cause] = cause_totals[cause] + total

            if total > 500:
                top_donors.append((donor, total))
    return cause_totals, top_donors

def write_fundraising_report(cause_totals, top_donors):
    with open("fundraising_summary.txt", "w") as file:
        file.write("FUNDS RAISED PER CAUSE\n")
        file.write("----------------------\n")
        for cause in cause_totals:
            file.write(f"{cause}: ${cause_totals[cause]:.2f}\n")
        file.write("\nGOLD TIER DONORS (> $500)\n")
        file.write("----------------------\n")
        for donor, amount in top_donors:
            file.write(f"{donor} (${amount:.2f})\n")

cause_totals, top_donors = process_donations("donations.txt")
write_fundraising_report(cause_totals, top_donors)