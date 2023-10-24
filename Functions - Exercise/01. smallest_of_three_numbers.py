def smallest_num(num_one, num_two, num_three):
    smallest = 0

    if num_one < num_two and num_one < num_three:
        smallest = num_one
    elif num_two < num_one and num_two < num_three:
        smallest = num_two
    elif num_three < num_one and num_three < num_two:
        smallest = num_three

    return smallest

print(smallest_num(num_one=int(input()), num_two = int(input()), num_three = int(input())))
