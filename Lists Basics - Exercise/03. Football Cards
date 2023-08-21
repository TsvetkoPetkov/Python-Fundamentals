ref_inp = input().split(" ")

teamA = []
teamB = []

for player in range(1, 12):
    teamA.append(player)
    teamB.append(player)

ref_setA = set()
ref_setB = set()

stopped_game = False

for card in ref_inp:
    splitted_card = card.split("-")
    alpha = splitted_card[0]
    num = splitted_card[1]

    if alpha == "A":
        ref_setA.add(num)
        if (11 - len(ref_setA)) < 7:
            stopped_game = True
            break
    else:
        if (11 - len(ref_setB)) < 7:
            stopped_game = True
            break
        ref_setB.add(num)

print(f"Team A - {11 - len(ref_setA)}; Team B - {11 - len(ref_setB)}")

if stopped_game:
    print("Game was terminated")
