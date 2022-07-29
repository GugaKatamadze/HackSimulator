import argparse
from pathlib import Path
from simulator import Simulator

parser = argparse.ArgumentParser(description='Hack Simulator')
parser.add_argument('path', type=str, metavar='path', help="absolute or relative path to the hack file")
parser.add_argument('cycles', type=int, metavar='cycles', help="a number of CPU cycles to execute")

args = parser.parse_args()

if __name__ == '__main__':
    path = Path(args.path)
    str_path = str(path.absolute())
    output_path = str_path[: len(str_path) - 4] + "out"
    file = open(str_path, "r")
    instructions = file.readlines()
    simulator = Simulator(instructions, output_path, args.cycles)
