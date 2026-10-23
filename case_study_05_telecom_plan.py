# Case Study 5: Multi-Plan Telecommunications Cost Optimization
data_used = 18
minutes_used = 450
budget = 500
plans = [
    ["Basic", 249, 10, 300, 28],
    ["Value", 399, 20, 500, 56],
    ["Plus", 449, 25, 600, 28],
    ["Short", 199, 15, 400, 14],
]
eligible = []
for plan in plans:
    name, price, data_allowance, call_allowance, validity = plan
    extra_data = max(0, data_used - data_allowance)
    extra_calls = max(0, minutes_used - call_allowance)
    total = price + extra_data * 20 + extra_calls * 0.50
    print(name, "- estimated cost: Rs.", round(total, 2))
    if validity >= 28 and total <= budget:
        eligible.append([name, total, validity])
if not eligible:
    print("No plan meets the validity and budget requirements")
else:
    eligible.sort(key=lambda item: item[1])
    best = eligible[0]
    print("Recommended plan:", best[0])
    print("Estimated total cost: Rs.", round(best[1], 2))
    print("Validity:", best[2], "days")
