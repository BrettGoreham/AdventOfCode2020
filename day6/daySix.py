with open('daySixInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

firstPartSumOfYes = secondPartSumOfYes = numPeople = 0
questionToNumberOfYes = {}
for i, line in enumerate(content):
    if line != '':
        numPeople += 1
        for part in line:
            questionToNumberOfYes[part] = questionToNumberOfYes.get(part, 0) + 1

    if line == '' or i == len(content) - 1:
        for key in questionToNumberOfYes.keys():
            firstPartSumOfYes += 1
            if questionToNumberOfYes[key] == numPeople:
                secondPartSumOfYes += 1
        questionToNumberOfYes.clear()
        numPeople = 0

print(firstPartSumOfYes)
print(secondPartSumOfYes)

# saw some things on the subreddit about using set functions to find answers quicker. recreated it here to learn
with open('daySixInput.txt') as f:
    inputText = f.read().strip()
groups = inputText.split('\n\n')

part1 = 0
part2 = 0

for group in groups:
    part1 += len(set(group.replace('\n', '')))
    people = group.split('\n')
    setOfAllYes = set(people[0])
    for person in people[1:]:
        setOfAllYes = setOfAllYes.intersection(set(person))
    part2 += len(setOfAllYes)


print('part1part2', part1)
print('part2part2', part2)





