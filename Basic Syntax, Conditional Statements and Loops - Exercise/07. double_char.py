while True:
    text = input()

    if text == "End":
        break

    if text == "SoftUni":
        continue

    output = ""
    for ch in text:
        output+= ch*2

    print(output)
