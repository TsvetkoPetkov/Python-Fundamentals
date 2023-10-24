year = int(input())
start = year + 1
count_list = []
good_number = True

while True:
    string_year = str(start)

    for digit in string_year:
        count_list.append(string_year.count(digit))

    for num in count_list:
        if num > 1:
            good_number = False
            break
        else:
            good_number = True

    if not good_number:
        start += 1
        count_list.clear()
    else:
        print(string_year)
        break
