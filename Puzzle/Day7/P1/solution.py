import sys
import math

lines = sys.stdin.read().strip().splitlines()

Strength = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

typeGroups = [[] for _ in range(7)]
Bets = {}

def AddtoTypeGroups(hand):
    repeat = {}

    for card in hand:
        if card in repeat:
            repeat[card] += 1
        else:
            repeat[card] = 1

    sortedHand = sorted(list(repeat.values()), reverse=True)

    if sortedHand == [5]:
        typeGroups[6].append(hand)
    elif sortedHand == [4, 1]:
        typeGroups[5].append(hand)
    elif sortedHand == [3,2]:
        typeGroups[4].append(hand)
    elif sortedHand == [3,1,1]:
        typeGroups[3].append(hand)
    elif sortedHand == [2,2,1]:
        typeGroups[2].append(hand)
    elif sortedHand == [2,1,1,1]:
        typeGroups[1].append(hand)
    elif sortedHand == [1,1,1,1,1]:
        typeGroups[0].append(hand)
    else:
        print('Error!')

#First need to separate it into types, so we will have 7 groups
for line in lines:
  hand = line.split()
  Bets[hand[0]] = int(hand[1])
  AddtoTypeGroups(hand[0])

#Then for each type group we will sort them in order
for typeGroup in typeGroups:
    typeGroup.sort(key=lambda x: [Strength[c] for c in x])

rank = 1
Score = 0
for group in typeGroups:
    for hand in group:
        Score += Bets[hand] * rank
        rank += 1

print(Score)
