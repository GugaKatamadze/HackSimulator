class Writer:

    ram = {}
    for i in range(32768):
        ram[i] = ""

    @classmethod
    def write_to_ram(cls, index: int, value: int) -> None:
        cls.ram[index] = str(value)

    @classmethod
    def get_ram_value(cls, index: int) -> int:
        return int(cls.ram[index])

    @classmethod
    def write_out(cls, output_path: str) -> None:
        file = open(output_path, "w")
        for i in range(32768):
            file.write(f'RAM[{i}] : {cls.ram[i]}\n')
