num_seq = [int(x) for x in input().split(", ")]

max_num = max(num_seq)

for num in range(10, max_num+10, 10):
    curr_list = []

    for n in num_seq:
        if n <= num:
            curr_list.append(n)

    print(f"Group of {num}'s: {curr_list}")

    for el in curr_list:
        for i in num_seq:
            if el == i:
                num_seq.remove(el)

    curr_list.clear()
