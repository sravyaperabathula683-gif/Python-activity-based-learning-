# Case Study 4: Employee Payroll and Deduction Analysis
basic = 30000
overtime_hours = 6
incentive = 2500

if min(basic, overtime_hours, incentive) < 0:
    print("Invalid salary input")
else:
    hra = basic * 0.20
    other_allowance = basic * 0.10
    overtime_pay = overtime_hours * 200
    gross = basic + hra + other_allowance + overtime_pay + incentive
    if gross <= 20000:
        deduction = 0
    elif gross <= 40000:
        deduction = (gross - 20000) * 0.05
    else:
        deduction = 20000 * 0.05 + (gross - 40000) * 0.10
    net = gross - deduction
    print("SALARY STATEMENT")
    print("Basic pay: Rs.", round(basic, 2))
    print("HRA: Rs.", round(hra, 2))
    print("Other allowance: Rs.", round(other_allowance, 2))
    print("Overtime pay: Rs.", round(overtime_pay, 2))
    print("Incentive: Rs.", round(incentive, 2))
    print("Gross salary: Rs.", round(gross, 2))
    print("Deduction: Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net, 2))
