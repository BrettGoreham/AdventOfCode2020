with open('dayElevenInput.txt') as f:
    seatMap = []
    for line in f:
        seatMap.append(list(line.strip()))

copyOfSeatMap = seatMap  # for part 2

seatsToCheck = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]


def is_point_in_map(seat_map, seat_x, seat_y):
    return 0 <= seat_x <= (len(seat_map) - 1) and 0 <= seat_y <= (len(seat_map[0]) - 1)


def becomes_free(seat_map, seat_x, seat_y):
    count_taken_adjacent = 0
    for seatToCheck in seatsToCheck:
        if is_point_in_map(seat_map, seat_x + seatToCheck[0], seat_y + seatToCheck[1]):
            value = seat_map[seat_x + seatToCheck[0]][seat_y + seatToCheck[1]]
            if value == '#':
                count_taken_adjacent += 1

    if count_taken_adjacent >= 4:
        return True
    else:
        return False


def becomes_taken(seat_map, seat_x, seat_y):
    for seatToCheck in seatsToCheck:
        if is_point_in_map(seat_map, seat_x + seatToCheck[0], seat_y + seatToCheck[1]):
            value = seat_map[seat_x + seatToCheck[0]][seat_y + seatToCheck[1]]
            if value == '#':
                return False

    return True


notStable = True

while notStable:
    hasChanged = False
    newSeatMap = []
    for row in range(0, len(seatMap)):
        newRow = []
        for column in range(0, len(seatMap[0])):
            spaceValue = seatMap[row][column]
            if spaceValue == '#':
                if becomes_free(seatMap, row, column):
                    hasChanged = True
                    newRow.append("L")
                else:
                    newRow.append("#")

            elif spaceValue == 'L':
                if becomes_taken(seatMap, row, column):
                    hasChanged = True
                    newRow.append("#")
                else:
                    newRow.append("L")
            else:
                newRow.append(spaceValue)

        newSeatMap.append(newRow)

    seatMap = newSeatMap
    notStable = hasChanged

countFree = 0
for row in range(0, len(seatMap[0])):
    for column in range(0, len(seatMap)):
        spaceValue = seatMap[column][row]
        if spaceValue == '#':
            countFree += 1

print('Part 1 Seats Taken:',  countFree)


def becomes_free_2(seat_map, seat_x, seat_y):
    count_taken_adjacent = 0
    for seatToCheck in seatsToCheck:
        orig = [0, 0]
        seat_found = False
        while not seat_found:
            orig[0] += seatToCheck[0]
            orig[1] += seatToCheck[1]
            if is_point_in_map(seat_map, seat_x + orig[0], seat_y + orig[1]):
                value = seat_map[seat_x + orig[0]][seat_y + orig[1]]
                if value == '#':
                    count_taken_adjacent += 1
                    seat_found = True
                elif value == 'L':
                    seat_found = True

            else:
                seat_found = True

    if count_taken_adjacent >= 5:
        return True
    else:
        return False


def becomes_taken2(seat_map, seat_x, seat_y):
    for seatToCheck in seatsToCheck:
        orig = [0, 0]
        while True:
            orig[0] += seatToCheck[0]
            orig[1] += seatToCheck[1]
            if is_point_in_map(seat_map, seat_x + orig[0], seat_y + orig[1]):
                value = seat_map[seat_x + orig[0]][seat_y + orig[1]]
                if value == '#':
                    return False
                elif value == 'L':
                    break

            else:
                break

    return True


seatMap = copyOfSeatMap
notStable = True

while notStable:
    hasChanged = False
    newSeatMap = []
    for row in range(0, len(seatMap)):
        newRow = []
        for column in range(0, len(seatMap[0])):
            spaceValue = seatMap[row][column]
            if spaceValue == '#':
                if becomes_free_2(seatMap, row, column):
                    hasChanged = True
                    newRow.append("L")
                else:
                    newRow.append("#")

            elif spaceValue == 'L':
                if becomes_taken2(seatMap, row, column):
                    hasChanged = True
                    newRow.append("#")
                else:
                    newRow.append("L")
            else:
                newRow.append(spaceValue)

        newSeatMap.append(newRow)

    seatMap = newSeatMap
    notStable = hasChanged

countFree = 0
for row in range(0, len(seatMap[0])):
    for column in range(0, len(seatMap)):
        spaceValue = seatMap[column][row]
        if spaceValue == '#':
            countFree += 1

print('Part 2 Seats Taken', countFree)
