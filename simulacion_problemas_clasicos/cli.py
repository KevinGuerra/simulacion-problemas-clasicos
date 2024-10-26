from typing import Optional

import typer

from simulacion_problemas_clasicos import __app_name__, __version__
from simulacion_problemas_clasicos.modules import dekker, filosofos_comensales

app = typer.Typer(add_completion=False)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True, no_args_is_help=True)
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Muestra la versión actual del proyecto.",
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
