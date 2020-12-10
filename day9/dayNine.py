with open('dayNineInput.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

length = 25
preamble = content[0:length]
numberThatCantBeAddedTo = -1
for nex in range(length, len(content)):
    num = content[nex]

    found = False
    for i in range(0, len(preamble)-1):
        for j in range(1, len(preamble)):
            if num == preamble[i] + preamble[j]:
                found = True

    if not found:
        print('part one: found no pair for:', num)
        numberThatCantBeAddedTo = num
        break
    preamble.pop(0)
    preamble.append(num)


findContig = numberThatCantBeAddedTo
for i in range(0, len(content)-1):
    sumOfContig = content[i]
    minInContig = sumOfContig
    maxInContig = sumOfContig
    for j in range(i+1, len(content)):
        if content[j] > maxInContig:
            maxInContig = content[j]
        elif content[j] < minInContig:
            minInContig = content[j]

        sumOfContig += content[j]
        if sumOfContig == findContig:
            print('part two sum of min max of contiguous indexs that add up to part 1:', maxInContig + minInContig)
        if sumOfContig > findContig:
            # sum only goes up so we can quit
            break
