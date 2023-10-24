def rounding(numbers: list, rounded_numbers: list):
    for elem in numbers:
        rounded_numbers.append(round(float(elem)))

    return rounded_numbers

numbers = input().split(" ")
rounded_numbers = []

print(rounding(numbers,rounded_numbers))
