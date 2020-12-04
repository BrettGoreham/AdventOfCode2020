from functools import partial

validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_not_valid_int(min_val, max_val, val):
    if val.isdigit():
        return int(val) < min_val or int(val) > max_val
    else:
        return True


def check_not_valid_height(val):
    measurement = val[-2:]
    if measurement == 'in':
        return int(val[0:-2]) < 59 or int(val[0:-2]) > 76
    elif measurement == 'cm':
        return int(val[0:-2]) < 150 or int(val[0:-2]) > 193
    return True


def check_hair_color(val): return val[0] != '#' or len(val) != 7


def check_eye_color(val): return val not in validEyeColors


def check_person_id(val): return not val.isdigit() or len(val) != 9


byrCheck = partial(check_not_valid_int, 1920, 2002)
iyrCheck = partial(check_not_valid_int, 2010, 2020)
eyrCheck = partial(check_not_valid_int, 2020, 2030)
hgtCheck = partial(check_not_valid_height)
hclCheck = partial(check_hair_color)
eclCheck = partial(check_eye_color)
pidCheck = partial(check_person_id)

requiredFieldsAndCheckLambda = (('byr', byrCheck), ('iyr', iyrCheck),
                                ('eyr', eyrCheck), ('hgt', hgtCheck),
                                ('hcl', hclCheck), ('ecl', eclCheck),
                                ('pid', pidCheck))


def check_passport_field_validity(field_to_value_dict):
    for fieldNameAndCheckTuple in requiredFieldsAndCheckLambda:
        if fieldNameAndCheckTuple[1](field_to_value_dict[fieldNameAndCheckTuple[0]]):
            return 0
    return 1


def check_valid_field_set(field_to_value_dict):
    for field in requiredFieldsAndCheckLambda:
        if field[0] not in field_to_value_dict:
            return 0
    return 1


fieldToValueDict = dict()
validFieldCombinations = 0
validPassports = 0

with open('dayFourInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for i, line in enumerate(content):
    if line != '':
        parts = line.split(' ')
        for part in parts:
            nameValuePair = part.split(':')
            fieldToValueDict[nameValuePair[0]] = nameValuePair[1]

    if line == '' or i == len(content)-1:
        isValidFieldCombo = check_valid_field_set(fieldToValueDict)
        if isValidFieldCombo:
            validFieldCombinations += 1
            validPassports += check_passport_field_validity(fieldToValueDict)
        fieldToValueDict.clear()

print('Part one passports with correct fields: ', validFieldCombinations)
print('Part two passports with correct and valid fields', validPassports)
