import sys

lines = iter(sys.stdin.read().strip().splitlines())

instructions = next(lines).strip()
next(lines)

nodes = {}

def GetNumSteps(startNode, EndNode):
    steps = 0

    while startNode != EndNode:
        instruction = instructions[steps % len(instructions)]
        steps += 1

        if instruction == 'L':
            startNode = nodes[startNode][0]
        if instruction == 'R':
            startNode = nodes[startNode][1]

    return steps



for line in lines:
    x = line.split(" = ")
    node = x[0]
    neighboor = x[1][1:-1].split(', ')

    nodes[node] = neighboor

result = GetNumSteps('AAA', 'ZZZ')
print(result)
