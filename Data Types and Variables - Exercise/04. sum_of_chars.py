number_of_lines = int(input())

total_sum = 0
for i in range(number_of_lines):
    ch = input()

    total_sum += ord(ch)

print(f"The sum equals: {total_sum}")
