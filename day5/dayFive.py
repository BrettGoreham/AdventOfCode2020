import math
with open('dayFiveInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

maxSeatID = 0
seatIdSets = []
for boardingPass in content:
    rowMin, rowMax = 0, 127
    columnMin, columnMax = 0, 7
    midRow = math.floor((rowMax + rowMin) / 2)
    midColumn = math.floor((columnMax + columnMin) / 2)
    for letter in boardingPass:
        if letter == 'B' or letter == 'F':
            if letter == 'B':
                rowMin = midRow + 1
            elif letter == 'F':
                rowMax = midRow

            midRow = math.floor((rowMax + rowMin) / 2)

        elif letter == 'R' or letter == 'L':
            if letter == 'R':
                columnMin = midColumn + 1
            elif letter == 'L':
                columnMax = midColumn

            midColumn = math.floor((columnMax + columnMin) / 2)

    seatIdSets.append(midRow * 8 + midColumn)
    if midRow * 8 + midColumn > maxSeatID:
        maxSeatID = midRow * 8 + midColumn

seatIdSets.sort()
mySeat = 0
for i in range(len(seatIdSets) - 1):
    if seatIdSets[i] + 2 == seatIdSets[i+1]:
        mySeat = seatIdSets[i] + 1

print('part one highest seat id: ', maxSeatID)
print('part two my seat', mySeat)
