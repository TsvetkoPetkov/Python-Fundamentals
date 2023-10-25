import re
tel_numbers = input()

patterns = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"

result = re.findall(patterns, tel_numbers)

print(", ".join(result))
