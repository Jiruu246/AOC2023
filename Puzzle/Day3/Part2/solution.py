import sys
import re

lines = sys.stdin.read().strip().splitlines()
Sum = 0

PrevBuffer = ""
NextBuffer = ""

def getEntireNumber(line, pos, lookLeft, lookRight):
    if not line[pos].isdigit():
        return ''
    elif pos == 0 or pos == len(line) - 1:
        return line[pos]
    
    result = line[pos]
    if lookLeft:
        result = getEntireNumber(line, pos - 1, True, False) + result
    if lookRight:
        result = result + getEntireNumber(line, pos + 1, False, True)

    return result 

def findUp(pos, prevBuf):
    result = []
    if prevBuf[pos].isdigit():
        return [getEntireNumber(prevBuf, pos, True, True)]
    
    if prevBuf[pos-1].isdigit():
        result.append(getEntireNumber(prevBuf, pos-1, True, False))
    if prevBuf[pos+1].isdigit():
        result.append(getEntireNumber(prevBuf, pos+1, False, True))


    return result

def findHorizontal(pos, line):
    result = []
    if line[pos-1].isdigit():
        result.append(getEntireNumber(line, pos-1, True, False))
    if line[pos+1].isdigit():
        result.append(getEntireNumber(line, pos+1, False, True))
    return result

def findDown(pos, nextBuf):
    result = []
    if nextBuf[pos].isdigit():
        return [getEntireNumber(nextBuf, pos, True, True)]

    if nextBuf[pos-1].isdigit():
        result.append(getEntireNumber(nextBuf, pos-1, True, False))
    if nextBuf[pos+1].isdigit():
        result.append(getEntireNumber(nextBuf, pos+1, False, True))
    return result

def IsGearValid(horizontal, upLine, downLine):
    return len(horizontal + upLine + downLine) == 2

for index, line in enumerate(lines):

    if index == len(lines) - 1:
        NextBuffer = ""
    else:
        NextBuffer = lines[index + 1]
 
    #Find gears that in the line
    gears = re.finditer(r'\*', line)
    for gear in gears:
        print(gear.start())
        pos = gear.start()
        upLine = findUp(pos, PrevBuffer)
        print(upLine)
        downLine = findDown(pos, NextBuffer)
        print(downLine)
        horizontal = findHorizontal(pos, line)
        print(horizontal)

        if IsGearValid(horizontal, upLine, downLine):
            gearRatios = horizontal + upLine + downLine
            ratio = int(gearRatios[0]) * int(gearRatios[1])
            Sum += ratio
    
    PrevBuffer = line
        
print("Sum", Sum)
