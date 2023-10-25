number_of_wagons = int(input())

train = [0] * number_of_wagons

while True:
    command = input()

    if command == "End":
        break

    action = command.split()[0]

    if action == "add":
        people_to_add = int(command.split()[1])
        train[-1] += people_to_add
    elif action == "insert":
        given_wagon = int(command.split()[1])
        people_to_add = int(command.split()[2])
        train[given_wagon] += people_to_add
    elif action == "leave":
        given_wagon = int(command.split()[1])
        people_to_leave = int(command.split()[2])
        train[given_wagon] -= people_to_leave

print(train)
