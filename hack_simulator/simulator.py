from decoder import Decoder
from writer import Writer
import registers


class Simulator:

    def __init__(self, instructions: list[str], output_path: str, cycles: int) -> None:
        self.writer = Writer(output_path)
        self.instructions = instructions
        self.cycles = cycles
        self.simulate()
        self.writer.write_out()

    def simulate(self) -> None:
        cycle_counter = 0
        while True:
            print(f'current pc: {registers.PC}')
            instruction = self.instructions[registers.PC]
            if Decoder.is_addressing(instruction):
                Decoder.process_addressing(instruction)
            else:
                Decoder.process_command(instruction)

            registers.PC += 1
            cycle_counter += 1

            if registers.PC >= len(self.instructions) or cycle_counter == self.cycles:
                break




