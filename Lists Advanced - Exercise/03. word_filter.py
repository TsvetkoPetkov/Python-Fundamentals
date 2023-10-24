fruits = input().split(" ")

even_length = [fruit for fruit in fruits if len(fruit) % 2 == 0]

for i in even_length:
    print(i)
