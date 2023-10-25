numbers = input().split(", ")
int_numbers = list(map(lambda num: int(num), numbers))

even_numbers_ind = [x for x in range(len(int_numbers)) if int_numbers[x] % 2 == 0]

print(even_numbers_ind)
