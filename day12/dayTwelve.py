with open('dayTwelveInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

directionDict = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
orig = [0, 0]
facing = 90

for line in content:
    instruction = line[0]
    num = int(line[1:])

    if instruction == 'F':
        instruction = directionDict[facing]

    if instruction == 'N':
        orig[1] += num
    elif instruction == 'S':
        orig[1] -= num
    elif instruction == 'W':
        orig[0] -= num
    elif instruction == 'E':
        orig[0] += num
    elif instruction == 'L':
        facing = (facing - num) % 360
    elif instruction == 'R':
        facing = (facing + num) % 360

print('Part one Manhattan distance:', abs(orig[0]) + abs(orig[1]))

#  start part 2
orig = [0, 0]
wayPoint = [10, 1]
facing = 90


def rotate_way_point(way_point, deg_facing, deg_to_rotate):
    to = (deg_facing + deg_to_rotate) % 360
    number_of_turns = int((to - deg_facing) / 90)
    if number_of_turns > 0:
        for turn in range(number_of_turns):
            way_point = [way_point[1], -1 * way_point[0]]
    elif number_of_turns < 0:
        for turn in range(abs(number_of_turns)):
            way_point = [-1 * way_point[1], way_point[0]]

    return way_point


for line in content:
    instruction = line[0]
    num = int(line[1:])

    if instruction == 'F':
        orig[0] = orig[0] + wayPoint[0] * num
        orig[1] = orig[1] + wayPoint[1] * num

    if instruction == 'N':
        wayPoint[1] += num
    elif instruction == 'S':
        wayPoint[1] -= num
    elif instruction == 'W':
        wayPoint[0] -= num
    elif instruction == 'E':
        wayPoint[0] += num
    elif instruction == 'L':
        wayPoint = rotate_way_point(wayPoint, facing, -1 * num)
        facing = (facing - num) % 360
    elif instruction == 'R':
        wayPoint = rotate_way_point(wayPoint, facing, num)
        facing = (facing + num) % 360

print('Part one Manhattan distance:', abs(orig[0]) + abs(orig[1]))
