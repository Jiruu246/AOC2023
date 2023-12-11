import sys
import re

lines = sys.stdin.read().strip().splitlines()

origin_RGB = [12, 13, 14]

Sum = 0
Id = 1
for line in lines:
    rgb = [0, 0, 0]
    #trim out the "Game id:" part
    game = line[(6+len(str(Id))):].strip()
    #split the rounds
    picks = re.split(";|,", game)
    for pick in picks:
        cube = pick.strip().split(" ")
        if cube[1] == 'red' and rgb[0] < int(cube[0]):
            rgb[0] = int(cube[0])
        elif cube[1] == 'green' and rgb[1] < int(cube[0]):
            rgb[1] = int(cube[0])
        elif cube[1] == 'blue' and rgb[2] < int(cube[0]):
            rgb[2] = int(cube[0])

    if rgb[0] <= origin_RGB[0] and rgb[1] <= origin_RGB[1] and rgb[2] <= origin_RGB[2]:
        Sum += Id
        print(Id)

    Id += 1

print("Sum", Sum)
