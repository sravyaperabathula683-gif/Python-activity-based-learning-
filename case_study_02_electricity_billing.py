# Case Study 2: Progressive Electricity Billing
def calculate_bill(units):
    if units < 0:
        return None
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
    fixed = 50
    subtotal = energy + fixed
    surcharge = subtotal * 0.05
    total = subtotal + surcharge
    rebate = 20 if units <= 100 else 0
    total = max(0, total - rebate)
    return energy, fixed, surcharge, rebate, total

previous_units = 120
current_units = 260
previous = calculate_bill(previous_units)
current = calculate_bill(current_units)

if previous is None or current is None:
    print("Invalid units entered")
else:
    print("Previous bill: Rs.", round(previous[4], 2))
    print("Current bill: Rs.", round(current[4], 2))
    print("Energy charge: Rs.", round(current[0], 2))
    print("Fixed charge: Rs.", current[1])
    print("Surcharge: Rs.", round(current[2], 2))
    print("Rebate: Rs.", current[3])
    increase = ((current[4] - previous[4]) / previous[4]) * 100
    print("Increase:", round(increase, 2), "%")
    if increase > 30:
        print("Alert: unusual increase in bill")
    else:
        print("No unusual increase")
