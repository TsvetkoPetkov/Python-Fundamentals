bakery_input = input().split(" ")

bakery = {}

for el in range(0, len(bakery_input),2):
    key = bakery_input[el]
    value = int(bakery_input[el+1])

    bakery[key] = value

print(bakery)
