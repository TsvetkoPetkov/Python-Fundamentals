n = int(input())

positive_list = list()
negative_list = list()

count_positives = 0
sum_of_negatives = 0

for i in range(n):
    number = int(input())

    if number >= 0:
        positive_list.append(number)
        count_positives += 1
    elif number < 0:
        negative_list.append(number)
        sum_of_negatives += number


print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
