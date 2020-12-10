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

# globally available calculation list i guess so i could avoid passing it around.
# important because without it we calculate the same thing over and over again.
previouslyCalculated = dict()


# If i went from start to finish instead of finish to start the above dict isnt necessary....
# as    x =  (x-1) + (x-2) + (x-3)  (if they exist)
def calculate_number_combinations(numbers_available, last):
    if last in previouslyCalculated:
        return previouslyCalculated[last]
    if len(numbers_available) <= 1:
        return 1
    else:
        numbers_in_range_of_last = []
        for i in range(1, min(4, len(numbers_available) + 1)):
            if last - numbers_available[len(numbers_available) - i] < 4:
                numbers_in_range_of_last.append(i)

        sum_of_solutions = 0
        for i in numbers_in_range_of_last:
            value = calculate_number_combinations(
                numbers_available[0:-i],
                numbers_available[len(numbers_available) - i]
            )
            sum_of_solutions += value
            previouslyCalculated[numbers_available[len(numbers_available) - i]] = value
        return sum_of_solutions


with open('dayTenInput.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

content.sort()
content.append(content[len(content) - 1] + 3)
content.insert(0, 0)
newContent = content[:]
print('part 2:', calculate_number_combinations(newContent[0:-1], newContent[len(content) - 1]))
