# Case Study 6: Railway Fare and Reservation Calculator
distance = 350
travel_class = "AC3"
age = 65
cancelled = False
class_rates = [["Sleeper", 1.0], ["AC3", 1.8], ["AC2", 2.5]]
class_factor = 0
for item in class_rates:
    if item[0] == travel_class:
        class_factor = item[1]

if distance <= 0 or age < 0 or class_factor == 0:
    print("Invalid journey details")
else:
    if distance <= 100:
        base = distance * 1.00
    elif distance <= 300:
        base = 100 * 1.00 + (distance - 100) * 0.80
    else:
        base = 100 * 1.00 + 200 * 0.80 + (distance - 300) * 0.60
    fare = base * class_factor
    concession = 0
    if 5 <= age <= 11:
        concession = 0.50
    elif age >= 60:
        concession = 0.25
    fare = fare * (1 - concession)
    reservation = 40
    amount = fare + reservation
    print("Base fare: Rs.", round(base, 2))
    print("Class:", travel_class, "Multiplier:", class_factor)
    print("Age concession:", int(concession * 100), "%")
    print("Fare with reservation: Rs.", round(amount, 2))
    if cancelled:
        penalty = amount * 0.20
        print("Cancellation penalty: Rs.", round(penalty, 2))
        print("Refund: Rs.", round(max(0, amount - penalty), 2))
    else:
        print("Fare payable: Rs.", round(amount, 2))
