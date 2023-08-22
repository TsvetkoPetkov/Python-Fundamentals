text = [word.lower() for word in input().split(" ")]

dictionary = {}

for word in text:
    if word not in dictionary:
        dictionary[word] = 0

    dictionary[word] += 1


for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
