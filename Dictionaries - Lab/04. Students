last_command = ''
students = {}

while True:
    command = input()

    if not ":" in command:
        last_command = command
        break

    name, ID, course = command.split(":")
    if course not in students:
        students[course] = {name: ID}
    else:
        students[course][name] = ID

formatted_last_command = " ".join(last_command.split("_"))

for key, value in students.items():
    if key == formatted_last_command:
        for st_name, st_id in value.items():
            print(f"{st_name} - {int(st_id)}")
