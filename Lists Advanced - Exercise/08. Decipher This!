secret_mess = input().split(" ")

for word in secret_mess:
    digits = ""
    alphas = ""

    for ch in word:
        if ch.isdigit():
            digits += ch
        if ch.isalpha():
            alphas += ch

    if len(alphas) > 1:
        first_alpha = alphas[-1]
        last_alpha = alphas[0]
        print(f"{chr(int(digits))}{first_alpha}{alphas[1:-1]}{last_alpha}", end=" ")
    else:
        last_alpha = alphas[0]
        print(f"{chr(int(digits))}{last_alpha}", end=" ")
