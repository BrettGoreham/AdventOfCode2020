with open('dayThirteenInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
myTime = int(content[0])

busToOffSet = []
offSet = 0
busToTimeArriveAfterMe = dict()
for x in content[1].split(','):
    if x == 'x':
        offSet += 1
        continue
    else:
        num = int(x)
        busToOffSet.append([num, offSet])
        offSet += 1
        count = 0
        while count < myTime:
            count += num
        busToTimeArriveAfterMe[num] = count

busId = 0
timeArriveAfterMe = float("inf")
for key in busToTimeArriveAfterMe.keys():
    if busToTimeArriveAfterMe[key] < timeArriveAfterMe:
        busId = key
        timeArriveAfterMe = busToTimeArriveAfterMe[key]

print('part 1: ', (timeArriveAfterMe - myTime) * busId)


step = busToOffSet[0][0]  # assuming 0 offset here
first = 0
for bus in busToOffSet[1:]:
    notFound = True
    count = first
    firstFound = -1
    while notFound:
        count += step
        if (count % bus[0] + bus[1]) % bus[0] == 0:
            if firstFound < 0:
                first = firstFound = count
            else:
                step = count - firstFound
                notFound = False

print('Part two, minutes till busses come in order: ', first)
