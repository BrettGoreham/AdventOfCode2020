with open('dayOneInput.txt') as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

print('partOne')
for i in range(len(content) - 2):
    for j in range(i+1, len(content) - 1):
        if content[i] + content[j] == 2020:
            print(content[i], 'x', content[j], '=', content[i]*content[j])
            break

print("partTwo")
for i in range(len(content) - 2):
    for j in range(i+1, len(content) - 1):
        for z in range(j+1, len(content)):
            if content[i] + content[j] + content[z] == 2020:
                print(content[i], 'x', content[j], 'x', content[z], '=', content[i]*content[j]*content[z])
                break
