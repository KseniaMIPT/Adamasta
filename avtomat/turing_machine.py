class TuringMachine:
    def __init__(self, instructions, data):
        with open(instructions, 'r') as file_with_instructions:
            text_with_instructions = file_with_instructions.readlines()

        with  open(data, 'r') as file_with_data:
            text_with_data = file_with_data.readline()

        self.instructions = {}
        for instruction in text_with_instructions:
            current_line = instruction.split()
            self.instructions[current_line[0]] = current_line[1]

        self.tape = ['B']
        for symbol in text_with_data:
            self.tape.append(symbol)
        self.tape.append('B')

        self.state = None

    def action(self):
        self.state = 'q1'
        current_number = 1
        while self.state != 'qZ':  # Пока автомат не пришел в конечное состояние
            current_symbol = self.tape[current_number]
            current_state = str(current_symbol) + self.state
            current_instruction = self.instructions[current_state]
            if current_instruction[0] != 'N':  # Изменяем или не изменяем текущий символ
                self.tape[current_number] = current_instruction[0]
            self.state = current_instruction[1:3]  # Измением состояние
            if current_instruction[3:] == 'R':  # Двигаемся в заданную клетку
                current_number += 1
            elif current_instruction[3:] == 'L':
                current_number -= 1
        print(self.tape)


Turing = TuringMachine('test3_instructions', 'test_data')
#Turing = TuringMachine('mult_instruction', 'mult_data')
Turing.action()





