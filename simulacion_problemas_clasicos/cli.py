from typing import Optional

import typer

from simulacion_problemas_clasicos import __app_name__, __version__
from simulacion_problemas_clasicos.modules import dekker, filosofos_comensales

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


@app.command(name="dekker")
def algoritmo_dekker():
    dekker.ejecutar_dekker()


@app.command(name="filosofos_comensales")
def algoritmo_filosofos_comensales():
    filosofos_comensales.ejecutar_filosofos_comensales()
