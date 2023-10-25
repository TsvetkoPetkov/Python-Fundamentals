numbers_input = input().split(" ")
to_remove = int(input())

numbers_list = []

for el in numbers_input:
    numbers_list.append(int(el))

for j in range(to_remove):
    numbers_list.remove(min(numbers_list))


output = ""

for i in numbers_list:
    output = output + str(i) + ", "

output_two = output[:-2]
print(output_two)
