number_of_people = int(input())
capacity  = int(input())

output = 0

output = number_of_people // capacity

de = number_of_people % capacity

if de <= capacity and de != 0:
    output += 1

print(output)
