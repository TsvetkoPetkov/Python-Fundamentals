text = input()

for i in range(len(text)):
    ch = text[i]
    if ch == ':' and i + 1 < len(text):
        symbol = text[i+1]
        print(f":{symbol}")
