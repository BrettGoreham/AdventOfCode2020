from InstructionComputer import InstructionComputer
with open('dayEightTestInput.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

x = InstructionComputer(content)
acc, isLooped, isTerminated = x.run()
print('Part one accumulator when looped: ', acc)

instructionToInstructionMap = {'jmp': 'nop', 'nop': 'jmp'}
for i in range(len(content)):
    originalInstruction, originalNumber = content[i].split(' ')
    if originalInstruction == 'jmp' or originalInstruction == 'nop':
        content[i] = instructionToInstructionMap[originalInstruction] + ' ' + originalNumber

        computer = InstructionComputer(content)
        acc, looped, terminated = computer.run()

        if terminated:
            print('partTwo: ', acc, '\tinstruction changed:', i)

        content[i] = originalInstruction + ' ' + originalNumber
