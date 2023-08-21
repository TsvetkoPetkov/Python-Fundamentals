cards = input().split()
num_shuffles = int(input())

deck_size = len(cards)
half_size = deck_size // 2

for i in range(num_shuffles):
    left_half = cards[:half_size]
    right_half = cards[half_size:]
    cards.clear()

    for el in range(half_size):
        cards.append(left_half[el])
        cards.append(right_half[el])

print(cards)
