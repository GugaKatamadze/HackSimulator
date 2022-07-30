from n2t.core import registers
from n2t.core.decoder import Decoder
from n2t.core.writer import Writer


class Simulator:

    @staticmethod
    def simulate(instructions: list[str], output_path: str, cycles: int) -> None:
        cycle_counter = 0
        while True:
            print(f'current pc: {registers.PC}')
            instruction = instructions[registers.PC]
            if Decoder.is_addressing(instruction):
                Decoder.process_addressing(instruction)
            else:
                Decoder.process_command(instruction)

            registers.PC += 1
            cycle_counter += 1

            if registers.PC >= len(instructions) or cycle_counter == cycles:
                break

        Writer.write_out(output_path)





