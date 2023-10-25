numbers_inp = input().split(", ")
beggars_n = int(input())

numbers_list = []

for n in numbers_inp:
    numbers_list.append(int(n))

beggars = []

for i in range(beggars_n):
    beggars.append(0)

index = 0

for el in numbers_list:
    beggars[index] += el

    index += 1

    if index == beggars_n:
        index = 0

print(beggars)
