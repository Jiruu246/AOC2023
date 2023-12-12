import sys

lines = sys.stdin.read().strip().splitlines()
Sum = 0
cards = [0] * len(lines)

for index, line in enumerate(lines):
  scratchCard = line[7:].strip().split("|")
  winningNumbers = set(scratchCard[0].strip().split())
  currentNumbers = set(scratchCard[1].strip().split())
  matches = winningNumbers.intersection(currentNumbers)

  cards[index] += 1
  for y in range(len(matches)):
    cards[index + y + 1] += cards[index]

print('Sum', sum(cards))