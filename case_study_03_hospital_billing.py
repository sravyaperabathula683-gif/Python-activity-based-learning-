# Case Study 3: Hospital Billing and Patient Classification
name = "Ravi"
age = 65
consultation = 500
diagnostics = 1200
treatment = 2500
has_card = False
paid = 3000

values = [age, consultation, diagnostics, treatment, paid]
if min(values) < 0:
    print("Invalid input: values cannot be negative")
else:
    subtotal = consultation + diagnostics + treatment
    discount = 0
    if age >= 60 or has_card:
        discount = subtotal * 0.10
    final_bill = subtotal - discount
    balance = final_bill - paid
    if paid >= final_bill:
        status = "Paid"
    elif paid > 0:
        status = "Partially Paid"
    else:
        status = "Unpaid"
    print("Patient:", name)
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Concession: Rs.", round(discount, 2))
    print("Final bill: Rs.", round(final_bill, 2))
    print("Amount paid: Rs.", round(paid, 2))
    print("Balance due: Rs.", round(max(0, balance), 2))
    print("Payment status:", status)
