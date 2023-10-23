voldemort = False

while True:
    name = input()

    if name == "Welcome!":
        break

    if name == "Voldemort":
        voldemort = True
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")

    if len(name) == 5:
        print(f"{name} goes to Slytherin.")

    if len(name) == 6:
        print(f"{name} goes to Ravenclaw.")

    if len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

if not voldemort:
    print("Welcome to Hogwarts.")
else:
    print("You must not speak of that name!")
