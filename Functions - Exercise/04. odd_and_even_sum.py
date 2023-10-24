def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for i in number:
        digit = int(i)

        if digit % 2 == 0:
            even_sum += digit
        elif digit % 2 == 1:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

string_number = input()

print(odd_and_even_sum(string_number))
