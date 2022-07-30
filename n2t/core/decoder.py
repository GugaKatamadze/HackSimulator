from n2t.core.writer import Writer
from n2t.core import registers


class Decoder:

    @staticmethod
    def is_addressing(command: str) -> bool:
        return command.startswith("0")

    @staticmethod
    def process_addressing(command: str) -> None:
        registers.A = int(command[1:], 2)
        print("A was set to " + str(registers.A))

    @staticmethod
    def process_command(command: str) -> None:
        Decoder.process_comp(command[3:10])
        Decoder.process_dest(command[10:13])
        Decoder.process_jmp(command[13:16])

    @staticmethod
    def process_comp(command: str) -> None:
        if command == "0101010":
            registers.C = 0
        elif command == "0111111":
            registers.C = 1
        elif command == "0111010":
            registers.C = -1
        elif command == "0001100":
            registers.C = registers.D
        elif command == "0110000":
            registers.C = registers.A
        elif command == "1110000":
            registers.C = Writer.get_ram_value(registers.A)
        elif command == "0001101":
            registers.C = not registers.D
        elif command == "0110001":
            registers.C = not registers.A
        elif command == "1110001":
            registers.C = not Writer.get_ram_value(registers.A)
        elif command == "0001111":
            registers.C = -registers.D
        elif command == "0110011":
            registers.C = -registers.A
        elif command == "1110011":
            registers.C = -Writer.get_ram_value(registers.A)
        elif command == "0011111":
            registers.C = registers.D + 1
        elif command == "0110111":
            registers.C = registers.A + 1
        elif command == "1110111":
            registers.C = Writer.get_ram_value(registers.A) + 1
        elif command == "0001110":
            registers.C = registers.D - 1
        elif command == "0110010":
            registers.C = registers.A - 1
        elif command == "1110010":
            registers.C = Writer.get_ram_value(registers.A) - 1
        elif command == "0000010":
            registers.C = registers.D + registers.A
        elif command == "1000010":
            registers.C = registers.D + Writer.get_ram_value(registers.A)
        elif command == "0010011":
            registers.C = registers.D - registers.A
        elif command == "0000111":
            registers.C = registers.A - registers.D
        elif command == "1010011":
            registers.C = registers.D - Writer.get_ram_value(registers.A)
        elif command == "1000111":
            registers.C = Writer.get_ram_value(registers.A) - registers.D
        elif command == "0000000":
            registers.C = registers.D & registers.A
        elif command == "1000000":
            registers.C = registers.D & Writer.get_ram_value(registers.A)
        elif command == "0010101":
            registers.C = registers.D | registers.A
        elif command == "1010101":
            registers.C = registers.D | Writer.get_ram_value(registers.A)

    @staticmethod
    def process_dest(command: str) -> None:
        if command == "001":
            Writer.write_to_ram(registers.A, registers.C)
        elif command == "010":
            registers.D = registers.C
        elif command == "011":
            Writer.write_to_ram(registers.A, registers.C)
            registers.D = registers.C
        elif command == "100":
            registers.A = registers.C
        elif command == "101":
            Writer.write_to_ram(registers.A, registers.C)
            registers.A = registers.C
        elif command == "110":
            registers.A = registers.C
            registers.D = registers.C
        elif command == "111":
            Writer.write_to_ram(registers.A, registers.C)
            registers.A = registers.C
            registers.D = registers.C

    @staticmethod
    def process_jmp(command: str) -> None:
        c = registers.C
        if (
                (command == "001" and c > 0) or
                (command == "010" and c == 0) or
                (command == "011" and c >= 0) or
                (command == "100" and c < 0) or
                (command == "101" and c != 0) or
                (command == "110" and c <= 0) or
                (command == "111")
        ):
            registers.PC = registers.A - 1
            print(f'jumping to {registers.A}')
