words = input().split(" ")

word_one = words[0]
word_two = words[1]

min_len = min(len(word_one), len(word_two))

result = 0

for i in range(min_len):
    result += ord(word_one[i]) * ord(word_two[i])

if len(word_one) > len(word_two):
    for _ in range(min_len, len(word_one)):
        result += ord(word_one[_])

if len(word_two) > len(word_one):
    for _ in range(min_len, len(word_two)):
        result += ord(word_two[_])

print(result)
