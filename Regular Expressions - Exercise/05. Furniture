import re

names = []
total_sum = 0

pattern = r">>([A-z]+)<<(\d+\.?\d+)!([0-9]+)"

while True:
    text = input()

    if text == "Purchase":
        break

    matches = re.finditer(pattern, text)

    for match in matches:
        name = match.group(1)
        names.append(name)
        price = float(match.group(2))
        quantity = int(match.group(3))

        total_sum += price * quantity

print("Bought furniture:")

for name in names:
    print(name)

print(f"Total money spend: {total_sum:.2f}")
