import click


@click.command
def ping() -> None:
    click.echo("pong")
