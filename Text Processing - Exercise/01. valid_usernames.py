from string import ascii_letters, digits

words = input().split(", ")

symbols = ascii_letters + digits + '-' + '_'

for word in words:
    if len(word) < 3 or len(word) > 16:
        continue

    not_good_word = False
    for ch in word:
        if ch not in symbols:
            not_good_word = True
            break

    if not_good_word:
        continue

    print(word)
