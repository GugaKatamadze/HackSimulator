import typer
from typer import Typer

from n2t.infra.hack_simulator import HackSimulator

cli = Typer(
    name="Hack Simulator",
    no_args_is_help=True,
    add_completion=False,
)


@cli.command("execute", no_args_is_help=True)
def simulate(
    path_to_hack_file: str, cycles: int = typer.Option(-1, "--cycles")
) -> None:
    HackSimulator.simulate(path_to_hack_file, cycles)


@cli.callback()
def callback() -> None:
    pass
