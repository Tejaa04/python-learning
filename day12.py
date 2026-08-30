# Raw Data
item_name = "Wireless Gaming Mouse"
quantity = 2
unit_price = 49.99
tax_rate = 0.085

# Calculations
subtotal = quantity * unit_price
grand_total = subtotal + (subtotal * tax_rate)

# Formatting using F-Strings
# 1. Left-align item_name in a width of 25 (<25)
# 2. Format subtotal to 2 decimal places (.2f)
# 3. Right-align grand total in a width of 10 (>10) with 2 decimal places (.2f)

line_1 = f"Item: {item_name:<25} | Qty: {quantity}"
line_2 = f"Subtotal: {'$' + f'{subtotal:.2f}':>22}"
line_3 = f"Grand Total (inc. tax): {'$' + f'{grand_total:.2f}':>9}"

print(line_1)
print(line_2)
print(line_3)