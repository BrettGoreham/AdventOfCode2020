import math
with open('dayThreeInput.txt') as f:
    treeMap = []
    for line in f:
        treeMap.append(list(line.strip()))

slopeList = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

treesHitList = []
for slope in slopeList:
    pos = [0, 0]
    countTreesHit = 0

    while pos[1] < len(treeMap):
        if treeMap[pos[1]][pos[0] % len(treeMap[0])] == '#':
            countTreesHit += 1
        pos[0] += slope[0]
        pos[1] += slope[1]

    treesHitList.append(countTreesHit)

print('part 1 trees hit: ', treesHitList[1])
print('part 2 trees hit: ', math.prod(treesHitList))
