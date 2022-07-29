class Writer:

    ram = {}
    for i in range(32768):
        ram[i] = ""

    def __init__(self, output_path: str) -> None:
        self.output_path = output_path

    @classmethod
    def write_to_ram(cls, index: int, value: int) -> None:
        cls.ram[index] = str(value)

    @classmethod
    def get_ram_value(cls, index: int) -> int:
        return int(cls.ram[index])

    def write_out(self) -> None:
        file = open(self.output_path, "w")
        for i in range(32768):
            file.write(f'RAM[{i}] : {self.ram[i]}\n')
