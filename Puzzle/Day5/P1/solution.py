import sys

lines = iter(sys.stdin.read().strip().splitlines())

line1 = next(lines)
seeds = line1.split(":")[1].split()
seeds = [int(x) for x in seeds]

SourceRanges = []
Maps = []

Index = -1

#Contruct a list of source ranges and maps from source to destination
for line in lines:
    if line == '': continue
    if not line[0].isdigit():
        Index += 1
        continue
    register = line.split()
    register = [int(x) for x in register]
    if Index > len(SourceRanges) - 1:
        SourceRanges.append([register[1]])
        Maps.append({register[1]: [register[0], register[2]]})
    else:
        SourceRanges[Index].append(register[1])
        SourceRanges[Index].sort()
        Maps[Index][register[1]] = [register[0], register[2]]

def findSource(seed, sources, offsets):
  for index, source in enumerate(sources):
      if index == len(sources) - 1 or seed in range(source, sources[index + 1]):
          if seed in range(source, source + offsets.get(source)[1]):
              return [source, seed - source]
  
  return False

def findDestinations(seed, level, depth):
    result = 0
    sourcePair = findSource(seed, SourceRanges[level], Maps[level]) 
    if sourcePair:
      result = Maps[level].get(sourcePair[0])[0] + sourcePair[1]
    else:
      result = seed

    if level == depth:
       return result
    else:
       return findDestinations(result, level+1, depth)
    
destinations = [0] * len(seeds)
for index, seed in enumerate(seeds):
  destinations[index] = findDestinations(seed, 0, len(SourceRanges) - 1)

part1 = min(destinations)
print(part1)