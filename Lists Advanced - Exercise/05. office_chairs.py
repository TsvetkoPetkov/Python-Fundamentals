number_of_rooms = int(input())

counter = 0

sum_chairs = 0
sum_visitors = 0

for room in range(1, number_of_rooms+1):
    info = input().split(" ")

    chairs = info[0]
    visitors = int(info[1])

    sum_chairs += len(chairs)
    sum_visitors += visitors

    if visitors > len(chairs):
        counter += 1
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")

if counter == 0:
    print(f"Game On, {sum_chairs - sum_visitors} free chairs left")
