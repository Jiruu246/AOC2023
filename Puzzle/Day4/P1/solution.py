import sys

lines = sys.stdin.read().strip().splitlines()
Sum = 0

for line in lines:
  scratchCard = line[9:].strip().split("|")
  winningNumbers = set(scratchCard[0].strip().split())
  currentNumbers = set(scratchCard[1].strip().split())
  matches = winningNumbers.intersection(currentNumbers)
  if len(matches) > 0:
    Sum += 2**(len(matches)-1)

print('Sum', Sum)