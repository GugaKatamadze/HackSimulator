from pathlib import Path

from n2t.core.simulator import Simulator


class HackSimulator:

    @staticmethod
    def simulate(path_to_hack_file: str, cpu_cycles: int) -> None:
        path = Path(path_to_hack_file)
        output_path = str(path.absolute())[: len(str(path.absolute())) - 4] + "out"
        instructions = open(path.absolute(), "r").readlines()
        Simulator.simulate(instructions, output_path, cpu_cycles)
