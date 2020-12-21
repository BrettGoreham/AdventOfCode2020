from collections import defaultdict
import time
start = time.time()

class Tile:
    def __init__(self, tile_list, tile_id):
        self.tile_id = tile_id
        self.tile_list = tile_list
        self.tile_sides = self.get_all_possible_sides()
        self.above = None
        self.below = None
        self.left = None
        self.right = None
        self.x = None
        self.y = None

    def flip_tile_vertically(self):
        self.tile_list = self.tile_list[::-1]
        temp = self.above
        self.above = self.below
        self.below = temp

    def flip_tile_horizontally(self):
        for j in range(len(self.tile_list)):
            self.tile_list[j] = self.tile_list[j][::-1]
        temp = self.left
        self.left = self.right
        self.right = temp

    def rotate_clock_wise(self):
        self.tile_list = list(map(list, zip(*self.tile_list[::-1])))
        temp = self.above
        self.above = self.left
        self.left = self.below
        self.below = self.right
        self.right = temp

    def get_left_side(self):
        left_side = []
        for j in range(len(self.tile_list)):
            left_side.append(self.tile_list[j][0])

        return left_side

    def get_right_side(self):
        right_side = []
        for j in range(len(self.tile_list)):
            right_side.append(self.tile_list[j][len(self.tile_list[j]) - 1])
        return right_side

    def get_top(self):
        return self.tile_list[0]

    def get_bottom(self):
        return self.tile_list[len(self.tile_list) - 1]

    def strip_border(self):
        self.tile_list.pop(0)
        self.tile_list.pop(len(self.tile_list) - 1)

        for tile_row in self.tile_list:
            tile_row.pop(0)
            tile_row.pop(len(tile_row)-1)

    def get_all_possible_sides(self):
        sides_possible = []
        sides_possible.append(self.tile_list[0])
        sides_possible.append(self.tile_list[0][::-1])
        sides_possible.append(self.tile_list[len(self.tile_list) - 1])
        sides_possible.append(sides_possible[2][::-1])

        left_side = []
        right_side = []
        for j in range(len(self.tile_list)):
            left_side.append(self.tile_list[j][0])
            right_side.append(self.tile_list[j][len(self.tile_list[j]) - 1])

        sides_possible.append(left_side)
        sides_possible.append(left_side[::-1])
        sides_possible.append(right_side)
        sides_possible.append(right_side[::-1])

        return sides_possible


with open('dayTwentyInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

listOfTilesToBePlaced = []

currTile = ""
tile_list_for_curr_tile = []
for line in content:
    if line.startswith("Tile "):
        currTile = int(line[5:line.index(':')])
    elif line != '':
        tile_list_for_curr_tile.append(list(line))
    elif currTile != "":
        listOfTilesToBePlaced.append(Tile(tile_list_for_curr_tile, currTile))
        currTile = ""
        tile_list_for_curr_tile = []


tilesWithOnly2MatchingSides = []

# Took a gamble that there would only be one match for each side per tile, and that the first one i found was correct
for tile in listOfTilesToBePlaced:
    isTopMatched = False
    isBottomMatched = False
    isLeftMatched = False
    isRightMatched = False

    matchedCount = 0

    tileTop = tile.tile_list[0]
    tileBottom = tile.tile_list[len(tile.tile_list) - 1]
    tileLeft = []
    tileRight = []
    for i in range(len(tile.tile_list)):
        tileLeft.append(tile.tile_list[i][0])
        tileRight.append(tile.tile_list[i][len(tile.tile_list[i]) - 1])

    for tile2 in listOfTilesToBePlaced:
        if tile.tile_id != tile2.tile_id:

            if tileTop in tile2.tile_sides:
                isTopMatched = True
                tile.above = tile2
                matchedCount += 1

            if tileBottom in tile2.tile_sides:
                isBottomMatched = True
                tile.below = tile2
                matchedCount += 1

            if tileLeft in tile2.tile_sides:
                isTopMatched = True
                tile.left = tile2
                matchedCount += 1

            if tileRight in tile2.tile_sides:
                isBottomMatched = True
                tile.right = tile2
                matchedCount += 1

    # if only two matches that means this is a corner
    if matchedCount == 2:
        tilesWithOnly2MatchingSides.append(tile)

# print this and hope it is 4
print(len(tilesWithOnly2MatchingSides))
product = 1
for tile in tilesWithOnly2MatchingSides:
    product *= tile.tile_id

print('part 1', product)


# start to make board
topLeft = tilesWithOnly2MatchingSides[0]

if topLeft.right is None:
    topLeft.flip_tile_horizontally()
if topLeft.below is None:
    topLeft.flip_tile_vertically()

topLeft.x = 0
topLeft.y = 0

tilesToFindFriends = [topLeft]
results = defaultdict(list)  # result dict where key is y value in the map

# here from above we know which tiles from where connect to each other.
# so we start with a corner which has only 2 matches, and place its partners right and down.
# and then go through them all matching down and right sides (making sure the are matched up and flipped correctly)
# until we get to bottom right corner which has no matches down or right
while len(tilesToFindFriends) > 0:
    tileAlreadyPlaced = tilesToFindFriends.pop(0)
    results[tileAlreadyPlaced.y].append(tileAlreadyPlaced)

    if tileAlreadyPlaced.right is not None:
        toRight = tileAlreadyPlaced.right
        if toRight.x is None:
            while toRight.left != tileAlreadyPlaced:
                toRight.rotate_clock_wise()

            if tileAlreadyPlaced.get_right_side() != toRight.get_left_side():
                toRight.flip_tile_vertically()

            toRight.x = tileAlreadyPlaced.x + 1
            toRight.y = tileAlreadyPlaced.y
            tilesToFindFriends.append(toRight)

    if tileAlreadyPlaced.below is not None:
        toBelow = tileAlreadyPlaced.below
        if toBelow.x is None:
            while toBelow.above != tileAlreadyPlaced:
                toBelow.rotate_clock_wise()

            if tileAlreadyPlaced.get_bottom() != toBelow.get_top():
                toBelow.flip_tile_horizontally()

            toBelow.x = tileAlreadyPlaced.x
            toBelow.y = tileAlreadyPlaced.y + 1
            tilesToFindFriends.append(toBelow)


# start making the total rows
# made function strip border for this as that was required to find actual map.
totalRows = []

for yValue in sorted(results.keys()):
    tiles_at_y = results[yValue]
    tiles_at_y = sorted(tiles_at_y,  key=lambda z: z.x)
    firstInRow = tiles_at_y[0]
    firstInRow.strip_border()

    base = firstInRow.tile_list

    for remainingTileInRow in tiles_at_y[1:]:
        remainingTileInRow.strip_border()
        for i in range(len(remainingTileInRow.tile_list)):
            base[i].extend(remainingTileInRow.tile_list[i])

    totalRows.extend(base)

# Open the mask i created from the sea monster to find them.
with open('seaMonsterMask.txt') as f:
    seaMonster = f.readlines()
seaMonster = [list(x.strip()) for x in seaMonster]

seaMonsterCount = 0

attemptsToFind = 0  # every 5th one we need to flip it vertically. this should find it after max 10 iterations.
while seaMonsterCount == 0:
    if attemptsToFind % 5 == 0 and attemptsToFind != 0:
        totalRows = totalRows[::-1]
    else:
        totalRows = list(map(list, zip(*totalRows[::-1])))

    yStart = 0
    xStart = 0

    while yStart + len(seaMonster) <= len(totalRows):
        while xStart + len(seaMonster[0]) <= len(totalRows[0]):
            isSeaMonsterHere = True
            for yIndex in range(len(seaMonster)):
                for xIndex in range(len(seaMonster[0])):
                    # using ? in sea monster to mean wildcard
                    if seaMonster[yIndex][xIndex] != '?':
                        if seaMonster[yIndex][xIndex] != totalRows[yStart + yIndex][xStart + xIndex]:
                            isSeaMonsterHere = False

            if isSeaMonsterHere:
                seaMonsterCount += 1

            xStart += 1

        yStart += 1
        xStart = 0

    attemptsToFind += 1

print('seaMonsterCount', seaMonsterCount)
seaMonsterNumOfHashtags = 15
countHashTags = 0
for row in totalRows:
    for x in row:
        if x == '#':
            countHashTags += 1

print('HashTags minus sea monsters ', countHashTags - (seaMonsterCount * seaMonsterNumOfHashtags))
print('It took', time.time()-start, 'seconds.')
