import re
with open('daySevenInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

childrenToListOfPossibleParents = {}
parentToListOfChildren = {}

for i, line in enumerate(content):
    if line != '':
        lineSplit = line.split(' bags contain ')
        outer = lineSplit[0]
        innerBags = []
        if lineSplit[1][0:2] != 'no':
            for inner in lineSplit[1].split(', '):
                x = inner.strip().split(' ')
                bagName = x[1] + ' ' + x[2]
                parentList = childrenToListOfPossibleParents.get(bagName)
                if not parentList:
                    childrenToListOfPossibleParents[bagName] = [outer]
                else:
                    childrenToListOfPossibleParents[bagName].append(outer)

                innerBags.append([x[1] + ' ' + x[2], int(x[0])])
        parentToListOfChildren[outer] = innerBags


numBags = 0
duplicate = 0
search = 'shiny gold'
searchResults = []
toSearch = childrenToListOfPossibleParents[search]
while len(toSearch) > 0:
    nextBag = toSearch.pop(0)
    if nextBag not in searchResults:
        searchResults.append(nextBag)
        if nextBag in childrenToListOfPossibleParents:
            for bag in childrenToListOfPossibleParents[nextBag]:
                toSearch.append(bag)

print('part one, number of bags that can hold at least one shiny gold', len(searchResults))


#recursion with base case being 0 children
def get_number_of_children(bag_name, parent_to_list_of_children):
    return_val= 0
    for childIn in parent_to_list_of_children[bag_name]:
        return_val += childIn[1] + childIn[1] * (get_number_of_children(childIn[0], parent_to_list_of_children))
    return return_val


sumBagInGold = get_number_of_children('shiny gold', parentToListOfChildren)
print('Number of bags that must be in shiny gold', sumBagInGold)
