from collections import defaultdict
import copy
import time
start = time.time()


def read_content_into_rules_and_strings(lines):
    rules = defaultdict(list)
    strings_to_attempt_to_match = []
    rules_done = False
    for line in lines:
        if rules_done:
            strings_to_attempt_to_match.append(line)
        elif line == '':
            rules_done = True
        else:
            rule_num, instructions = line.split(':')

            for match in instructions.split('|'):
                rules[rule_num].append(match.strip().split(' '))

    return rules, strings_to_attempt_to_match


def rewrite_index_and_save_for_later_searching(rule_values, list_of_rules_to_follow, index, strings_that_can_be_made):
    for ruleValue in rule_values:
        copy_of_list = list_of_rules_to_follow[:]
        del copy_of_list[index]
        count = len(ruleValue) - 1
        while count >= 0:
            copy_of_list.insert(index, ruleValue[count])
            count -= 1
        strings_that_can_be_made.insert(0, [copy_of_list, index])
        # everything before index is already set so start there when we come back to these strings


def replace_index_with_list_of_elements(index, elements_to_replace_with, list_to_replace_in):
    increase_index = False

    del list_to_replace_in[index]
    count = len(elements_to_replace_with) - 1
    while count >= 0:
        value = elements_to_replace_with[count]
        if value == '"a"' or value == '"b"':
            increase_index = True
            value = value[1]
        list_to_replace_in.insert(index, value)
        count -= 1

    return increase_index


def find_count_possible_strings(rules_to_follow, list_strings_to_match):
    found_count = 0

    for string in list_strings_to_match:

        strings_that_can_be_made = [[copy.deepcopy(rules_to_follow['0'][0]), 0]]  # list of rules and index to start at
        while 0 < len(strings_that_can_be_made):

            list_of_rules_to_follow, index = strings_that_can_be_made.pop(0)
            while index < len(list_of_rules_to_follow) <= len(string):

                rule_values = rules_to_follow[list_of_rules_to_follow[index]]

                # going to keep track of one list at a time
                # so the ors get sent to the strings that can be made list for later work
                rewrite_index_and_save_for_later_searching(
                    rule_values[1:],
                    list_of_rules_to_follow,
                    index,
                    strings_that_can_be_made
                )

                increase_index = replace_index_with_list_of_elements(index, rule_values[0], list_of_rules_to_follow)

                if increase_index:
                    index += 1

                # break if what we have so far is wrong
                if string[0:index] != "".join(list_of_rules_to_follow[0:index]):
                    break

            # if found just break and move on to next string since we already created it
            if string == "".join(list_of_rules_to_follow):
                found_count += 1
                break

    return found_count


with open('dayNineteenInput.txt') as f:
    part1Lines = f.readlines()
part1Lines = [x.strip() for x in part1Lines]

with open('dayNineteenInputPart2.txt') as f:
    part2Lines = f.readlines()
part2Lines = [x.strip() for x in part2Lines]

part1rules, part1StringsToMatch = read_content_into_rules_and_strings(part1Lines)
part2rules, part2StringsToMatch = read_content_into_rules_and_strings(part2Lines)

print('part one:', find_count_possible_strings(part1rules, part1StringsToMatch))
print('part two:', find_count_possible_strings(part2rules, part2StringsToMatch))
print('It took', time.time()-start, 'seconds.')
