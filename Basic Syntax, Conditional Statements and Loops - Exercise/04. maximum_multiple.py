number = int(input())
boundary = int(input())

largest = 0

for i in range(1, boundary + 1):
    if i % number == 0:
        largest = i

print(largest)
