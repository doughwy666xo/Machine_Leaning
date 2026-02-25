#
# Clay, 2026/2/25
# Clay_Hello.py
# Print Hello
#

price= 250
units_sold= 1200

total_Sales= price*units_sold
discount = total_Sales * 0.05       
net_sales  = total_Sales - discount

print(f"total Sales : ${total_Sales:,}")
print(f"Discount    : ${discount:,.2f}")
print(f"Net Sales   : ${net_sales:,.2f}")



