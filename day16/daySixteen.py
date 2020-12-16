with open('daySixteenInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

rules = {}
myTicket = []
otherTickets = []
rulesDone = False
myTicketDone = False
for line in content:
    if line == '':
        if not rulesDone:
            rulesDone = True
        else:
            myTicketDone = True
    elif not rulesDone:
        name, values = line.split(':')
        pairs = []
        for value in values.strip().split(' or '):
            pair = [int(x) for x in value.split('-')]
            pairs.append(pair)

        rules[name] = pairs

    elif rulesDone and not myTicketDone:
        if line != 'your ticket:':
            myTicket = [int(x) for x in line.split(',')]
    else:
        if line != 'nearby tickets:':
            otherTickets.append([int(x) for x in line.split(',')])

ticketsToPurge = []
invalidFieldTotal = 0
for i, ticket in enumerate(otherTickets):
    isInvalid = False
    for value in ticket:
        found = False
        for key in rules:
            for pair in rules[key]:
                if pair[0] <= value <= pair[1]:
                    found = True
        if not found:
            invalidFieldTotal += value
            isInvalid = True

    if isInvalid:
        ticketsToPurge.insert(0, i)  # make list backwards so its in right order to delete

for i in ticketsToPurge:
    del otherTickets[i]

print('part one sum of invalid fields: ', invalidFieldTotal)

fieldDeclarations = {}
notFoundIndexesYet = list(range(0, len(otherTickets[0])))
indexInListToCheck = 0
rulesNotFound = list(rules.keys())

while len(notFoundIndexesYet) != 0:
    index = notFoundIndexesYet[indexInListToCheck]
    possibleFields = rulesNotFound
    for ticket in otherTickets:
        newPossibleFields = []
        for rule in possibleFields:
            validForField = False
            for pair in rules[rule]:
                if pair[0] <= ticket[index] <= pair[1]:
                    validForField = True

            if validForField:
                newPossibleFields.append(rule)

        possibleFields = newPossibleFields

    if len(possibleFields) == 1:
        fieldDeclarations[possibleFields[0]] = index
        notFoundIndexesYet.pop(indexInListToCheck)
        rulesNotFound.remove(possibleFields[0])
        indexInListToCheck = 0
    else:
        indexInListToCheck += 1


multipleOfDepartureFields = 1
for key in fieldDeclarations.keys():
    if key.startswith('departure'):
        multipleOfDepartureFields *= myTicket[fieldDeclarations[key]]

print('part two Multiple of departure fields:', multipleOfDepartureFields)
