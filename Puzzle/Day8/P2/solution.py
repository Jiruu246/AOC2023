import sys

lines = iter(sys.stdin.read().strip().splitlines())

instructions = next(lines).strip()
next(lines)

nodes = {}
startNodes = []

def NodesEndWith(nodes, char):
    for node in nodes:
        if not NodeEndWith(node, char):
            return False
    return True

def NodeEndWith(node, char):
    return node[-1] == char

for line in lines:
    x = line.split(" = ")
    node = x[0]
    if NodeEndWith(node, 'A'):
        startNodes.append(node)

    neighboor = x[1][1:-1].split(', ')

    nodes[node] = neighboor

# result = GetNumSteps(startNodes, 'Z')
# print(result)

def GetNumSteps(startNode, EndChar):
    steps = 0

    while not NodeEndWith(startNode, EndChar):
        instruction = instructions[steps % len(instructions)]
        steps += 1

        if instruction == 'L':
            startNode = nodes[startNode][0]
        if instruction == 'R':
            startNode = nodes[startNode][1]

    return steps

result = GetNumSteps(startNodes[0])
print(result)