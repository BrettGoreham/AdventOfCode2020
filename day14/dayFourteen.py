with open('dayFourteenInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

memory = dict()
mask = []
for line in content:
    if line[0:3] == 'mas':
        mask = []
        for i, x in enumerate(line[7:]):
            mask.append(x)
    else:
        memAddress = int(line[line.index('[')+1:line.index(']')])
        value = int(line[line.index('=')+2:])
        string = "{0:b}".format(value).zfill(36)

        result = ""
        for i in range(0, len(string)):
            if mask[i] == 'X':
                result += string[i]
            else:
                result += mask[i]

        intVal = int(result, 2)
        memory[memAddress] = intVal

total = 0
for key in memory.keys():
    total += memory[key]

print(total)


def get_all_binary_strings(s, set_of_strings, index):
    if len(s) <= index:
        return set_of_strings

    new_strings = []
    if s[index] != 'X':
        for stringToAdd in set_of_strings:
            stringToAdd += s[index]
            new_strings.append(stringToAdd)
        return get_all_binary_strings(s, new_strings, index + 1)
    else:
        for stringToAdd in set_of_strings:
            stringToAdd += '1'
            new_strings.append(stringToAdd)
        for stringToAdd in set_of_strings:
            stringToAdd += '0'
            new_strings.append(stringToAdd)

        return get_all_binary_strings(s, new_strings, index + 1)


# part 2

memory = dict()
mask = []
for line in content:
    if line[0:3] == 'mas':
        mask = []
        for i, x in enumerate(line[7:]):
            mask.append(x)
    else:
        memAddress = int(line[line.index('[')+1:line.index(']')])
        value = int(line[line.index('=')+2:])

        string = "{0:b}".format(memAddress).zfill(36)
        result = ""
        xCount = 0
        for i in range(0, len(string)):
            if mask[i] == '0':
                result += string[i]
            else:
                if mask[i] == 'X':
                    xCount += 1
                result += mask[i]

        for maskedMemoryAddress in get_all_binary_strings(result, [''], 0):
            memory[int(maskedMemoryAddress, 2)] = value


total = 0
for key in memory.keys():
    total += memory[key]

print(total)
