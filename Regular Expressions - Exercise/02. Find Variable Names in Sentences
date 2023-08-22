import re

text = input()

pattern = r"\b\_[A-Za-z0-9]+\b"

words = re.findall(pattern, text)

result = []

for el in words:
    result.append(el[1:])

print(",".join(result))
