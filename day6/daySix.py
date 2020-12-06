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

    if line == '' or i == len(content)-1:
        for key in questionToNumberOfYes.keys():
            firstPartSumOfYes += 1
            if questionToNumberOfYes[key] == numPeople:
                secondPartSumOfYes += 1
        questionToNumberOfYes.clear()
        numPeople = 0

print(firstPartSumOfYes)
print(secondPartSumOfYes)
