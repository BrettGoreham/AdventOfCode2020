with open('dayTwoInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

partOneValidPasswordsCount = 0
partTwoValidPasswordsCount = 0

for line in content:
    components = line.split(' ')
    bounds = components[0].split('-')
    minBound = int(bounds[0])
    maxBound = int(bounds[1])
    letter = components[1][0:1]
    password = components[2]

    if minBound <= password.count(letter) <= maxBound:
        partOneValidPasswordsCount += 1

    if (password[minBound-1] == letter) ^ (password[maxBound-1] == letter):
        partTwoValidPasswordsCount += 1

print('Part One Valid Password Count:', partOneValidPasswordsCount)
print('Part Two Valid Password Count:', partTwoValidPasswordsCount)
