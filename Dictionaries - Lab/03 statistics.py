products = {}

while True:
    command = input()

    if command == 'statistics':
        break

    product_info = command.split(": ")

    key = product_info[0]
    value = int(product_info[1])

    if key not in products:
        products[key] = value
    else:
        products[key] += value

print("Products in stock:")

for pr, quantity in products.items():
    print(f"- {pr}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
