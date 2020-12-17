import time
start = time.time()
with open('daySeventeenInput.txt') as f:
    layer = []
    for line in f:
        layer.append(list(line.strip()))

layers = [layer]


def create_new_layer(x_width, y_width):
    return [['.' for x in range(x_width)] for y in range(y_width)]


def increase_width_and_height_of_existing_layers(layers_to_increase):
    for existing_layer in layers_to_increase:
        for row_in_layer in range(len(existing_layer)):
            existing_layer[row_in_layer].append('.')
            existing_layer[row_in_layer].insert(0, '.')

        existing_layer.insert(0, ['.' for x in range(len(existing_layer[0]))])
        existing_layer.append(['.' for x in range(len(existing_layer[0]))])


def is_in_layers(curr_z, curr_y, curr_x, curr_layers):
    if 0 <= curr_z < len(curr_layers):
        if 0 <= curr_y < len(curr_layers[0]):
            if 0 <= curr_x < len(curr_layers[0][0]):
                return True

    return False


def get_active_neighbours(curr_z, curr_y, curr_x, curr_layers):
    count = 0
    for zDiff in range(-1, 2):
        for yDiff in range(-1, 2):
            for xDiff in range(-1, 2):
                if zDiff != 0 or yDiff != 0 or xDiff != 0:
                    if is_in_layers(curr_z + zDiff, curr_y + yDiff, curr_x + xDiff, curr_layers):
                        if curr_layers[curr_z + zDiff][curr_y + yDiff][curr_x + xDiff] == '#':
                            count += 1

    return count


for i in range(0, 6):
    yWidth = len(layers[0])
    xWidth = len(layers[0][0])

    increase_width_and_height_of_existing_layers(layers)
    layers.insert(0, create_new_layer(xWidth + 2, yWidth + 2))
    layers.append(create_new_layer(xWidth + 2, yWidth + 2))

    newLayers = []
    for z in range(len(layers)):
        rows = []
        for y in range(len(layers[z])):
            row = []
            for x in range(len(layers[z][y])):
                char = layers[z][y][x]
                numActiveNeighbours = get_active_neighbours(z, y, x, layers)
                if char == '.':
                    if numActiveNeighbours == 3:
                        row.append('#')
                    else:
                        row.append('.')
                else:
                    if numActiveNeighbours == 3 or numActiveNeighbours == 2:
                        row.append('#')
                    else:
                        row.append('.')
            rows.append(row)

        newLayers.append(rows)

    layers = newLayers


countCubes = 0
for z in range(len(layers)):
    for y in range(len(layers[z])):
        for x in range(len(layers[z][y])):
            if layers[z][y][x] == '#':
                countCubes += 1

print('part one 3d space:', countCubes)

# Part 2 now in 4d
with open('daySeventeenInput.txt') as f:
    layer = []
    for line in f:
        layer.append(list(line.strip()))

layers = [layer]
fourthD = [layers]


def create_new_fourth_d(curr_x, curr_y, num_layers):
    layer_list = []
    for toCreate in range(num_layers):
        layer_list.append(create_new_layer(curr_x, curr_y))
    return layer_list


def is_in_fourth_d(curr_w, curr_z, curr_y, curr_x, curr_fourth_d):
    if 0 <= curr_w < len(curr_fourth_d):
        if 0 <= curr_z < len(curr_fourth_d[0]):
            if 0 <= curr_y < len(curr_fourth_d[0][0]):
                if 0 <= curr_x < len(curr_fourth_d[0][0][0]):
                    return True

    return False


def get_active_neighbours_4d(curr_w, curr_z, curr_y, curr_x, curr_fourth_d):
    count = 0
    for wDiff in range(-1, 2):
        for zDiff in range(-1, 2):
            for yDiff in range(-1, 2):
                for xDiff in range(-1, 2):
                    if wDiff != 0 or zDiff != 0 or yDiff != 0 or xDiff != 0:
                        if is_in_fourth_d(curr_w + wDiff, curr_z + zDiff, curr_y + yDiff, curr_x + xDiff, curr_fourth_d):
                            if curr_fourth_d[curr_w + wDiff][curr_z + zDiff][curr_y + yDiff][curr_x + xDiff] == '#':
                                count += 1

    return count


for i in range(0, 6):
    yWidth = len(fourthD[0][0])
    xWidth = len(fourthD[0][0][0])

    for value in fourthD:
        increase_width_and_height_of_existing_layers(value)
        value.insert(0, create_new_layer(xWidth + 2, yWidth + 2))
        value.append(create_new_layer(xWidth + 2, yWidth + 2))

    fourthD.insert(0, create_new_fourth_d(xWidth + 2, yWidth + 2, len(fourthD[0])))
    fourthD.append(create_new_fourth_d(xWidth + 2, yWidth + 2, len(fourthD[0])))

    newFourthDs = []
    for w in range(len(fourthD)):
        newLayers = []
        for z in range(len(fourthD[w])):
            rows = []
            for y in range(len(fourthD[w][z])):
                row = []
                for x in range(len(fourthD[w][z][y])):
                    char = fourthD[w][z][y][x]
                    numActiveNeighbours = get_active_neighbours_4d(w, z, y, x, fourthD)
                    if char == '.':
                        if numActiveNeighbours == 3:
                            row.append('#')
                        else:
                            row.append('.')
                    else:
                        if numActiveNeighbours == 3 or numActiveNeighbours == 2:
                            row.append('#')
                        else:
                            row.append('.')
                rows.append(row)

            newLayers.append(rows)
        newFourthDs.append(newLayers)

    fourthD = newFourthDs

countCubes = 0
for w in range(len(fourthD)):
    for z in range(len(fourthD[w])):
        for y in range(len(fourthD[w][z])):
            for x in range(len(fourthD[w][z][y])):
                if fourthD[w][z][y][x] == '#':
                    countCubes += 1

print('part 2 count in 4d space', countCubes)
print('It took', time.time()-start, 'seconds.')
