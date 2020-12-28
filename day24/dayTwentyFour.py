from collections import defaultdict
import time
start = time.time()

class Moves:
    def __init__(self):
        self.nw = 0
        self.sw = 0
        self.w = 0
        self.e = 0
        self.se = 0
        self.ne = 0

    def __eq__(self, other):
        if self.e == other.e:
            if self.w == other.w:
                if self.nw == other.nw:
                    if self.se == other.se:
                        if self.sw == other.sw:
                            if self.ne == other.ne:
                                return True
        return False

    def __hash__(self):
        return hash((self.e, self.w, self.ne, self.nw, self.se, self.sw))

    def get_neighbours(self):
        neighbours = []
        ne = self.create_copy()
        ne.ne += 1
        ne.simplify()
        neighbours.append(ne)

        nw = self.create_copy()
        nw.nw += 1
        nw.simplify()
        neighbours.append(nw)

        se = self.create_copy()
        se.se += 1
        se.simplify()
        neighbours.append(se)

        sw = self.create_copy()
        sw.sw += 1
        sw.simplify()
        neighbours.append(sw)

        e = self.create_copy()
        e.e += 1
        e.simplify()
        neighbours.append(e)

        w = self.create_copy()
        w.w += 1
        w.simplify()
        neighbours.append(w)

        return neighbours

    def create_copy(self):
        copy = Moves()
        copy.se = self.se
        copy.sw = self.sw
        copy.e = self.e
        copy.w = self.w
        copy.ne = self.ne
        copy.nw = self.nw
        return copy

    def simplify(self):

        changed = True
        while changed:
            changed = False
            while self.nw > 0 and self.sw > 0:
                self.nw -= 1
                self.sw -= 1
                self.w += 1
                changed = True

            while self.ne > 0 and self.se > 0:
                self.ne -= 1
                self.se -= 1
                self.e += 1
                changed = True

            while self.ne > 0 and self.sw > 0:
                self.ne -= 1
                self.sw -= 1
                changed = True

            while self.nw > 0 and self.se > 0:
                self.nw -= 1
                self.se -= 1
                changed = True

            while self.w > 0 and self.e > 0:
                self.w -= 1
                self.e -= 1
                changed = True

            while self.w > 0 and self.ne > 0:
                self.w -= 1
                self.ne -= 1
                self.nw += 1
                changed = True

            while self.w > 0 and self.se > 0:
                self.w -= 1
                self.se -= 1
                self.sw += 1
                changed = True

            while self.e > 0 and self.nw > 0:
                self.e -= 1
                self.nw -= 1
                self.ne += 1
                changed = True

            while self.e > 0 and self.sw > 0:
                self.e -= 1
                self.sw -= 1
                self.se += 1
                changed = True


with open('dayTwentyFourInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

list_of_moves = []

for line in content:
    move = Moves()
    top = len(line)
    i = 0
    while i < top:
        if line[i] == 'w':
            move.w += 1
            i += 1
        elif line[i] == 'e':
            move.e += 1
            i += 1
        elif line[i] == 's':
            if line[i+1] == 'e':
                move.se += 1
            else:
                move.sw += 1
            i += 2
        elif line[i] == 'n':
            if line[i+1] == 'e':
                move.ne += 1
            else:
                move.nw += 1
            i += 2
    move.simplify()
    list_of_moves.append(move)

blackTiles = []

for move in list_of_moves:
    if move not in blackTiles:
        blackTiles.append(move)
    else:
        blackTiles.remove(move)

print(len(blackTiles))


for i in range(0, 100):
    whiteNeighbours = defaultdict(int)
    nextBlack = []
    for blackTile in blackTiles:
        neighbours = blackTile.get_neighbours()
        countBlackNeighbours = 0
        for neighbour in neighbours:
            if neighbour in blackTiles:
                countBlackNeighbours += 1
            else:
                whiteNeighbours[neighbour] += 1

        if 0 < countBlackNeighbours <= 2:
            nextBlack.append(blackTile)

    for key in whiteNeighbours.keys():
        if whiteNeighbours[key] == 2:
            nextBlack.append(key)

    print('day ',i + 1, 'number of blacks', len(nextBlack))
    blackTiles = nextBlack

print('It took', time.time()-start, 'seconds.')
