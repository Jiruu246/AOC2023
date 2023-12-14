import sys

lines = iter(sys.stdin.read().strip().splitlines())

line1 = next(lines)
seeds = line1.split(":")[1].split()
seeds = [int(x) for x in seeds]
comSeeds = []
for i in range(int(len(seeds)/2)):
  comSeeds.append([seeds[i*2], [0, seeds[i*2 + 1]]])

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

def findSources(compositSeed, SortedSources, offsets):
  seed = compositSeed[0]
  #Range is start from 0 and alway not including the end
  seedRange = compositSeed[1]
  if seedRange[0] != 0:
     raise Exception("Index must start from 0")
  result = []
  for index, source in enumerate(SortedSources):
    endSource = source + offsets.get(source)[1]
    endSeed = seed + seedRange[1]

    if seed < source:
      if endSeed < source:
        result.append([seed, seedRange])
        return result
      else:
        result.append([seed, [0, source - seed]])
        seed = source
        seedRange = [0, endSeed - source]

    if seed >= source and (index == len(SortedSources) - 1 or seed < SortedSources[index +1]):
      if seed < endSource:
        if endSeed <= endSource:
          result.append([source, [seed - source, endSeed - source]])
          return result
        else:
            result.append([source, [seed - source, offsets.get(source)[1]]])
            seed = endSource
            seedRange = [0, endSeed - endSource] 

      if seed >= endSource and index == len(SortedSources) - 1:
         result.append([seed, seedRange])

  return result

def convertDestToSeed(compoDests):
  compoDests.sort(key=lambda x: x[0])
  compoSeeds = []
  for index, dest in enumerate(compoDests):
    if index > 1 and dest[0] + dest[1][0] == compoSeeds[index - 1][0] + compoSeeds[index - 1][1][1]:
        compoSeeds[index - 1][1][1] == dest[0] + dest[1][1] - compoSeeds[index - 1][0]
        continue
          
    seed = dest[0] + dest[1][0]
    range = [0, dest[0]+ dest[1][1] - seed]
    compoSeeds.append([seed, range])

  return compoSeeds 

def findDestinations(compositeSeeds, level, depth):
    
    shortestDestinations = []

    for compoSeed in compositeSeeds:
      sourcePairs = findSources(compoSeed, SourceRanges[level], Maps[level])
      
      compoDestinations = []
      for sourcePair in sourcePairs:
        destination = Maps[level].get(sourcePair[0], sourcePair)[0]
        compoDestinations.append([destination, sourcePair[1]])

      if level == depth:
        destinations = []
        for compoDes in compoDestinations:
          destinations.append(compoDes[0] + compoDes[1][0])
        shortestDestinations.append(min(destinations))
      else:
          comS = convertDestToSeed(compoDestinations)
          shortestDestinations.append(findDestinations(comS, level+1, depth))
    
    return min(shortestDestinations)


print(comSeeds)
part2 = findDestinations(comSeeds, 0, len(SourceRanges) - 1)

print(part2)