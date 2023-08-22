count_of_words = int(input())
dictionary = {}

for i in range(count_of_words):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = synonym
    else:
        dictionary[word] += ", " + synonym

for key, value in dictionary.items():
    print(f"{key} - {value}")
