import time
start = time.time()

with open('dayTwentyThreeInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

cups = []
for char in content[0]:
    cups.append(int(char))

roundsPlayed = 0
crabCupIndex = 0

while roundsPlayed < 100:
    
    crabCup = cups[crabCupIndex]
    poppedCups = []
    for i in range(3):
        crabCupIndex = cups.index(crabCup)
        poppedCups.append(cups.pop((crabCupIndex + 1) % len(cups)))

    destination = None
    destinationVal = abs((crabCup - 1) % 10)
    while destination is None:
        try:
            destination = cups.index(destinationVal)
        except ValueError:
            destinationVal = abs((destinationVal - 1) % 10)

    for cup in reversed(poppedCups):
        cups.insert((destination + 1), cup)

    roundsPlayed += 1
    crabCupIndex = (cups.index(crabCup) + 1) % len(cups)

print(cups)


class Node:
    def __init__(self, val, previous, next_node=None):
        self.val = val
        self.next = None
        self.previous = previous
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def set_previous(self, previous_node):
        self.previous = previous_node

    def insert_after(self, node):
        temp = self.next
        self.set_next(node)
        node.set_next(temp)
        node.set_previous(self)
        temp.set_previous(node)


nodeMap = {}
firstNode = Node(int(content[0][0]), None)

nodeMap[firstNode.val] = firstNode

previousNode = firstNode
cups = []
for char in content[0][1:]:
    current = Node(int(char), previousNode)
    nodeMap[current.val] = current
    previousNode.next = current
    previousNode = current

for i in range(10, 1000001):
    current = Node(i, previousNode)
    nodeMap[current.val] = current
    previousNode.next = current
    previousNode = current

previousNode.set_next(firstNode)
firstNode.set_previous(previousNode)

roundsPlayed = 0
nextCrabCupNode = firstNode

while roundsPlayed < 10000000:

    crabCup = nextCrabCupNode
    toPop = nextCrabCupNode
    poppedCups = []
    poppedCupsVals = []
    for i in range(3):
        toPop = toPop.next
        poppedCups.append(toPop)
        poppedCupsVals.append(toPop.val)
    crabCup.set_next(toPop.next)
    toPop.next.set_previous(crabCup)

    destination = None
    destinationVal = abs((crabCup.val - 1) % (len(nodeMap) + 1))
    while destination is None:
        if destinationVal not in poppedCupsVals and destinationVal != 0:
            destination = nodeMap[destinationVal]
        else:
            destinationVal = abs((destinationVal - 1) % (len(nodeMap) + 1))

    for cup in reversed(poppedCups):
        destination.insert_after(cup)

    roundsPlayed += 1
    nextCrabCupNode = crabCup.next

indexOf1 = nodeMap[1]
print(indexOf1.next.val, indexOf1.next.next.val)
output = indexOf1.next.val * indexOf1.next.next.val
print(output)
print('It took', time.time()-start, 'seconds.')

