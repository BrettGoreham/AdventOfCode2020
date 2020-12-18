with open('dayEighteenInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


def solve_equation_left_to_right(equation_part):
    tokens = equation_part.split(' ')
    result = int(tokens[0])
    count = 1
    while count + 1 < len(tokens):
        if tokens[count] == '+':
            result += int(tokens[count + 1])
        else:
            result *= int(tokens[count + 1])
        count += 2
    return result


def solve_equation_with_addition_preference(equation_part):
    tokens = equation_part.split(' ')

    while '+' in tokens:
        index = tokens.index('+')
        solution = int(tokens[index - 1]) + int(tokens[index + 1])
        del tokens[index - 1: index + 2]  # delete the num + num and replace with solution
        tokens.insert(index - 1, solution)

    result = int(tokens[0])
    count = 1
    while count + 1 < len(tokens):
        result *= int(tokens[count + 1])
        count += 2
    return result


def solve_equation(equation_part, addition_preference):
    if addition_preference:
        return solve_equation_with_addition_preference(equation_part)
    else:
        return solve_equation_left_to_right(equation_part)


def find_solution_sum(addition_precedence):
    solution_sum = 0
    for equation in content:
        brackets_left_to_solve = True

        while brackets_left_to_solve:
            open_brackets = [i for i, ltr in enumerate(equation) if ltr == '(']
            if len(open_brackets) > 0:
                close_to_solve = equation.index(')')  # you can always solve the first closing bracket.
                open_to_solve = open_brackets[len(open_brackets) - 1]
                count = 1
                while open_to_solve > close_to_solve:
                    open_to_solve = open_brackets[len(open_brackets) - 1 - count]
                    count += 1

                solution = solve_equation(equation[open_to_solve + 1: close_to_solve], addition_precedence)

                equation = equation.replace(
                    equation[open_to_solve: close_to_solve + 1],
                    str(solution)
                )
            else:
                brackets_left_to_solve = False

        solution_sum += solve_equation(equation, addition_precedence)
    return solution_sum


print('part 1:', find_solution_sum(False))
print('part 2:', find_solution_sum(True))
