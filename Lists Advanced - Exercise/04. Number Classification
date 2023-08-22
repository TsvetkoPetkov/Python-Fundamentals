text_numbers = input().split(", ")

int_numbers = list(map(lambda x: int(x), text_numbers))

positive = [num for num in int_numbers if num >= 0]
negative = [num for num in int_numbers if num < 0]
even = [num for num in int_numbers if num % 2 == 0]
odd = [num for num in int_numbers if num % 2 == 1]

positive_output = ''
negative_output = ''
even_output = ''
odd_output = ''

for num in positive:
    positive_output += str(num) + ", "

for num in negative:
    negative_output += str(num) + ", "

for num in even:
    even_output += str(num) + ", "

for num in odd:
    odd_output += str(num) + ", "

print(f"Positive: {positive_output[:-2]}")
print(f"Negative: {negative_output[:-2]}")
print(f"Even: {even_output[:-2]}")
print(f"Odd: {odd_output[:-2]}")
