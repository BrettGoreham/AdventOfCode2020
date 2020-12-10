with open('dayTenInput.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

content.sort()
content.append(content[len(content) - 1] + 3)
highestVal = content[len(content) - 2] + 3
change = dict()
start = 0
for num in range(0, len(content)):
    curr = content[num]

    diff = curr - start
    change[diff] = change.get(diff, 0) + 1
    start = curr

print('part 1:', change[1] * change[3])

previouslyCalculated = dict()

def calculateNumberAvailable(numbersAvailable, last):
    if last in previouslyCalculated:
        return previouslyCalculated[last]
    countNumbersback = []
    for i in range(0, min(3, len(numbersAvailable))):
        if last - numbersAvailable[len(numbersAvailable) - 1 - i] < 4:
            countNumbersback.append(i)

    if len(numbersAvailable) <= 1:
        return 1
    else:
        product = 0
        for i in countNumbersback:
            value = calculateNumberAvailable(
                    numbersAvailable[0:-(i+1)],
                    numbersAvailable[len(numbersAvailable)-1 - i])
            product += value
            previouslyCalculated[numbersAvailable[len(numbersAvailable) - 1 - i]] = value
        return product


with open('dayTenInput.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

content.sort()
content.append(content[len(content) - 1] + 3)
content.insert(0, 0)
newContent=content[:]
print('part 2', calculateNumberAvailable(newContent[0:-1], newContent[len(content) - 1]))
