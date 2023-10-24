number_of_electrons = int(input())

shells_list = []
n = 1

while True:
    result = 2 * n**2

    if number_of_electrons - result > 0:
        shells_list.append(result)
        number_of_electrons -= result
    else:
        shells_list.append(number_of_electrons)
        break

    n += 1

print(shells_list)
