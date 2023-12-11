import sys
import re

lines = sys.stdin.read().strip().splitlines()

Sum = 0;
for line in lines:
    firstNum = re.search(r'\d', line)
    if firstNum == None:
        print("cant find number in line: ", line)
        break
    reverseLine = line[::-1]
    secondNum = re.search(r'\d', reverseLine)
   
print("Sum: ", Sum)