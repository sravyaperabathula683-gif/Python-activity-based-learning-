# Case Study 8: Manufacturing Cost and Profitability Analysis
units = 500
material_cost = 20000
wastage_percent = 5
labour_cost = 8000
machine_cost = 4000
selling_price = 75
target_profit_percent = 20
inputs = [material_cost, wastage_percent, labour_cost, machine_cost, selling_price, target_profit_percent]

if units <= 0 or min(inputs) < 0:
    print("Invalid production data")
else:
    wastage_cost = material_cost * wastage_percent / 100
    total_cost = material_cost + wastage_cost + labour_cost + machine_cost
    revenue = units * selling_price
    profit = revenue - total_cost
    unit_cost = total_cost / units
    profit_percent = (profit / total_cost) * 100 if total_cost > 0 else 0
    print("Units produced:", units)
    print("Wastage cost: Rs.", round(wastage_cost, 2))
    print("Total production cost: Rs.", round(total_cost, 2))
    print("Revenue: Rs.", round(revenue, 2))
    print("Profit: Rs.", round(profit, 2))
    print("Cost per unit: Rs.", round(unit_cost, 2))
    print("Profit percentage:", round(profit_percent, 2), "%")
    if profit_percent >= target_profit_percent:
        print("Target profit achieved")
    else:
        print("Target profit not achieved")
