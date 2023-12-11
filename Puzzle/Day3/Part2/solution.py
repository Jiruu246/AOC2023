import sys
import re

lines = sys.stdin.read().strip().splitlines()
Sum = 0

PrevBuffer = ""
NextBuffer = ""

def IsPartNumber(number, prevB, currentLine, nextB):
    StartSearchIndex = number.start() - 1 if number.start() > 0 else 0
    EndSearchIndex = number.end() if number.end() < len(currentLine) else len(currentLine) - 1

    print(number.group())
    print(number.start(), ' and ', number.end())

    if (StartSearchIndex > 0 and currentLine[StartSearchIndex] != ".") or (EndSearchIndex < len(currentLine) - 1 and currentLine[EndSearchIndex] != "."):
        print("found in current line")
        return True
    if prevB and re.search(r'[^.|\d]', prevB[StartSearchIndex:EndSearchIndex + 1]):
        print("found in previous line")
        return True
    if nextB and re.search(r'[^.|\d]', nextB[StartSearchIndex:EndSearchIndex + 1]):
        print("found in next line")
        return True

for index, line in enumerate(lines):

    if index == len(lines) - 1:
        NextBuffer = ""
    else:
        NextBuffer = lines[index + 1]
 
    #Find number that is not surrounded by "."
    numbers = re.finditer(r'\d+', line)
    for number in numbers:
        if IsPartNumber(number, PrevBuffer, line, NextBuffer):
            # print(number.group())
            Sum += int(number.group())
    
    PrevBuffer = line
        

print("Sum", Sum)
