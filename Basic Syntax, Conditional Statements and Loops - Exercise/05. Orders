number_of_orders = int(input())

total_price = 0
for i in range(number_of_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    
    if price < 0.01 or price > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue
    
    per_one_order = price * days * capsules
    total_price += per_one_order
    print(f"The price for the coffee is: ${per_one_order:.2f}")

print(f"Total: ${total_price:.2f}")
