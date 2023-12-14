import sys
import math

lines = sys.stdin.read().strip().splitlines()

times = lines[0].strip().split(':')[1].strip().split()
distances = lines[1].strip().split(':')[1].strip().split()

races = []
for i in range(len(times)):
    races.append([int(times[i]), int(distances[i])])

result = 1
for race in races:
    delta = race[0]**2 - 4*race[1]
    result *= len(range(
        int(math.floor((race[0]-math.sqrt(delta))/2) + 1), 
        int(math.ceil((race[0]+math.sqrt(delta))/2))))

print(result)