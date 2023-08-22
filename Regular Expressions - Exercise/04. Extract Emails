import re

text = input()

pattern = r"\s([A-Za-z0-9][\w\_\.\-]*[A-Za-z]@[A-Za-z][A-za-z\-]*[A-Za-z](\.[A-Za-z][A-za-z\-]*[A-Za-z])+)"

result = re.findall(pattern, text)

print('\n'.join([group[0] for group in result]))
