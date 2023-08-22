to_do_list = [0] * 10

while True:
    to_do_notes  = input()

    if to_do_notes == "End":
        break

    importance = int(to_do_notes.split("-")[0])
    action = to_do_notes.split("-")[1]

    to_do_list[importance - 1] = action


print([a for a in to_do_list if a != 0])
