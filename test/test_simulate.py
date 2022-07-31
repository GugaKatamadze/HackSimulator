import filecmp
from pathlib import Path

from n2t.core import registers
from n2t.core.writer import Writer
from n2t.runner.cli import simulate

hacks = ["Add", "Jump", "SimpleAdd", "StackTest", "StaticTest"]


def test_should_simulate() -> None:
    for i in hacks:
        path = Path("hacks").joinpath(i + ".hack")
        simulate_hack(str(path))
        reset()

    simulate_basic_loop()
    simulate_fibonacci_series()
    simulate_fibonacci_element()
    simulate_nested_call()
    simulate_statics_test()


def simulate_hack(path_to_hack_file: str, cycles: int = -1) -> None:
    simulate(path_to_hack_file, cycles)

    start_index = 6
    end_index = len(path_to_hack_file) - 5
    file_name = path_to_hack_file[start_index:end_index]
    output_path = Path("hacks").joinpath(file_name + ".out")
    cmp_path = Path("cmps").joinpath(file_name + ".cmp")

    assert filecmp.cmp(shallow=False, f1=output_path, f2=cmp_path)


def simulate_basic_loop() -> None:
    Writer.write_to_ram(0, 256)
    Writer.write_to_ram(1, 300)
    Writer.write_to_ram(2, 400)
    Writer.write_to_ram(400, 3)

    simulate_hack(str(Path("hacks").joinpath("BasicLoop.hack")))
    reset()


def simulate_fibonacci_series() -> None:
    Writer.write_to_ram(0, 256)
    Writer.write_to_ram(1, 300)
    Writer.write_to_ram(2, 400)
    Writer.write_to_ram(400, 6)
    Writer.write_to_ram(401, 3000)

    simulate_hack(str(Path("hacks").joinpath("FibonacciSeries.hack")))
    reset()


def simulate_fibonacci_element() -> None:
    Writer.write_to_ram(1, 0)
    Writer.write_to_ram(2, 0)
    Writer.write_to_ram(3, 0)
    Writer.write_to_ram(4, 0)

    simulate_hack(str(Path("hacks").joinpath("FibonacciElement.hack")), 6000)
    reset()


def simulate_nested_call() -> None:
    Writer.write_to_ram(0, 261)
    Writer.write_to_ram(1, 261)
    Writer.write_to_ram(2, 256)
    Writer.write_to_ram(3, -3)
    Writer.write_to_ram(4, -4)

    for i in range(261, 300):
        Writer.write_to_ram(i, -1)

    simulate_hack(str(Path("hacks").joinpath("NestedCall.hack")), 4000)
    reset()


def simulate_statics_test() -> None:
    Writer.write_to_ram(1, 0)
    Writer.write_to_ram(2, 0)
    Writer.write_to_ram(3, 0)
    Writer.write_to_ram(4, 0)

    simulate_hack(str(Path("hacks").joinpath("StaticsTest.hack")), 2500)
    reset()


def reset() -> None:
    Writer.reset()
    registers.A = 0
    registers.D = 0
    registers.C = 0
    registers.PC = 0
