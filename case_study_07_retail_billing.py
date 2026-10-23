# Case Study 7: Retail Billing with Multiple Discount Rules
products = [
    ["Notebook", 80, 5, 5],
    ["Backpack", 900, 2, 12],
    ["Pen Pack", 120, 3, 5],
]
subtotal = 0
valid = True
for product in products:
    name, price, quantity, tax_rate = product
    if price < 0 or quantity < 0 or tax_rate < 0:
        print("Invalid product record:", name)
        valid = False
        break
    subtotal += price * quantity

if valid:
    discount = min(subtotal * 0.10, 500) if subtotal >= 2000 else 0
    total_tax = 0
    print("ITEMIZED INVOICE")
    for product in products:
        name, price, quantity, tax_rate = product
        line = price * quantity
        line_discount = discount * line / subtotal if subtotal > 0 else 0
        taxable = line - line_discount
        tax = taxable * tax_rate / 100
        total_tax += tax
        print(name, "Qty:", quantity, "Line: Rs.", round(line, 2), "Tax: Rs.", round(tax, 2))
    final_total = subtotal - discount + total_tax
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Tax total: Rs.", round(total_tax, 2))
    print("Amount due: Rs.", round(final_total, 2))
