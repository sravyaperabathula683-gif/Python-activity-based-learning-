# Case Study 9: Multi-Currency Travel Budget Analysis
# Sample rates only: INR per one unit of foreign currency
expenses = [
    ["Hotel", 120, "USD", 83.0],
    ["Meals", 80, "EUR", 90.0],
    ["Transport", 5000, "JPY", 0.56],
    ["Museum", 40, "USD", 83.0],
]
budget = 20000
fee_rate = 0.02
total = 0
largest_category = ""
largest_amount = -1
valid = True

for expense in expenses:
    category, amount, currency, rate = expense
    if amount < 0 or rate <= 0:
        print("Invalid expense:", category)
        valid = False
        break
    converted = amount * rate
    fee = converted * fee_rate
    adjusted = converted + fee
    total += adjusted
    print(category, "(" + currency + "): Rs.", round(adjusted, 2))
    if adjusted > largest_amount:
        largest_amount = adjusted
        largest_category = category

if valid:
    print("Total spending: Rs.", round(total, 2))
    print("Largest category:", largest_category, "- Rs.", round(largest_amount, 2))
    if total <= budget:
        print("Within budget. Balance: Rs.", round(budget - total, 2))
    else:
        print("Over budget by: Rs.", round(total - budget, 2))
