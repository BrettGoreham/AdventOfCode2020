class InstructionComputer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.instructionCount = 0
        self.accumulator = 0
        self.setOfInstructionsRun = set()
        self.isLooped = False
        self.isTerminated = False

    def run(self):
        while not self.isLooped and not self.isTerminated:
            if self.instructionCount in self.setOfInstructionsRun:
                self.isLooped = True
            else:
                self.setOfInstructionsRun.add(self.instructionCount)
                if self.instructionCount >= len(self.instructions):
                    self.isTerminated = True
                else:
                    instruction, number = self.instructions[self.instructionCount].split(' ')
                    if instruction == 'jmp':
                        self.instructionCount += int(number)
                    elif instruction == 'acc':
                        self.accumulator += int(number)
                        self.instructionCount += 1
                    elif instruction == 'nop':
                        self.instructionCount += 1

        return self.accumulator, self.isLooped, self.isTerminated
