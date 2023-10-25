import re

result = []

while True:
    text = input()

    if not text:
        break

    pattern = r"\d+"

    numbers = re.findall(pattern, text)
    result.extend(numbers)

print(" ".join(result))
