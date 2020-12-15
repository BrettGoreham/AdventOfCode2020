import time
start = time.time()
with open('dayFifteenInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

nums = content[0].split(',')
numberToLastSpoken = dict()
toSpeak = 0
spokenCount = 0
for num in nums:
    spokenCount += 1
    if num in numberToLastSpoken.keys():
        toSpeak = spokenCount - numberToLastSpoken[int(num)]
    else:
        toSpeak = 0
    numberToLastSpoken[int(num)] = spokenCount


for i in range(spokenCount + 1, 30000001):
    if i == 2020:
        print('Part 1:', toSpeak)
    if i % 30000000 == 0:
        print('Part 2:', toSpeak)
    lastSpoke = toSpeak
    if toSpeak in numberToLastSpoken.keys():
        toSpeak = i - numberToLastSpoken[toSpeak]
    else:
        toSpeak = 0
    numberToLastSpoken[lastSpoke] = i

print('It took', time.time()-start, 'seconds.')