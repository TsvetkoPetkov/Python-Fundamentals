n = int(input())
word = input()

text_list = []
filtered_list = []

for i in range(n):
    text = input()
    text_list.append(text)

    if word in text:
        filtered_list.append(text)

print(text_list)
print(filtered_list)
