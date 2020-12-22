from collections import defaultdict

with open('dayTwentyOneInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


class Food:
    def __init__(self, ingredients_list, allergen_list):
        self.ingredients_list = ingredients_list
        self.allergen_list = allergen_list


foods = []
allergenToListsOfIngredients = defaultdict(list)
for line in content:
    ingredientList = set(line[0: line.index('(')].strip().split(' '))
    allergenList = line[line.index('(') + 9: line.index(')')].strip().split(', ')

    for allergen in allergenList:
        allergenToListsOfIngredients[allergen].append(ingredientList)

    foods.append(Food(ingredientList, allergenList))


allergenPossibleIngredients = []
for key in allergenToListsOfIngredients.keys():
    lists = allergenToListsOfIngredients[key]

    intersection = lists[0]
    for ingredientList in lists[1:]:
        intersection = set(intersection).intersection(set(ingredientList))

    allergenPossibleIngredients.append((key, intersection))

allergenPossibleIngredients.sort(key=lambda a: len(a[1]))
knownAllergensMap = {}
while len(allergenPossibleIngredients):
    allergenAndIngredient = allergenPossibleIngredients.pop(0)
    for other in allergenPossibleIngredients:
        if next(iter(allergenAndIngredient[1])) in other[1]:
            other[1].remove(next(iter(allergenAndIngredient[1])))

    allergenPossibleIngredients.sort(key=lambda a: len(a[1]))

    knownAllergensMap[allergenAndIngredient[0]] = allergenAndIngredient[1].pop()

count = 0
for food in foods:
    for ingredient in food.ingredients_list:
        if ingredient not in knownAllergensMap.values():
            count += 1

print('part one :', count)

part2Answer = ""
for i, key in enumerate(sorted(knownAllergensMap.keys())):
    part2Answer += knownAllergensMap[key]

    if i != len(knownAllergensMap.keys()) - 1:
        part2Answer += ','

print('part two:', part2Answer)

