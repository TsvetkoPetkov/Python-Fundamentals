happiness = input().split(" ")
factor = int(input())

int_happiness = list(map(lambda x: int(x) * factor, happiness))

average = sum(int_happiness) / len(int_happiness)

happy = [person for person in int_happiness if person >= average]

if len(happy) < len(int_happiness) / 2:
    print(f"Score: {len(happy)}/{len(int_happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(happy)}/{len(int_happiness)}. Employees are happy!")
