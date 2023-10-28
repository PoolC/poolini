import click


@click.group()
def seminar() -> None:
    pass


@seminar.command("출첵")
def attend() -> None:
    click.echo("attend")
