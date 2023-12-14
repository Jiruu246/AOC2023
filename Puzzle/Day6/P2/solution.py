import sys
import math

lines = sys.stdin.read().strip().splitlines()

time = int(lines[0].strip().split(':')[1].strip().replace(' ', ''))
distance = int(lines[1].strip().split(':')[1].strip().replace(' ', ''))

delta = time**2 - 4*distance
result = len(range(
    int(math.floor((time-math.sqrt(delta))/2) + 1), 
    int(math.ceil((time+math.sqrt(delta))/2))))

print(result)