text = input()
parts = text.split(">")

prev = 0

result = [parts[0]]

for p in parts[1:]:
    number = int(p[0])
    prev += number
    
    form_part = p[prev:]
    
    prev = max(prev - len(p), 0)
    result.append(form_part)
    
print('>'.join(result))
