text = input()

result = ""
for i in range(len(text)):
    if i + 1 < len(text):
        if text[i] == text[i + 1]:
            continue
    result += text[i]

print(result)
