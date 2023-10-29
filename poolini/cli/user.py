import click

from ..api import poolc as poolc_api


@click.group()
def user() -> None:
    pass


@user.command("활동")
def activity_time() -> None:
    res = poolc_api.get_my_activity_hours()
    click.echo(res)


@user.command("나")
def me_info() -> None:
    res = poolc_api.get_me()
    click.echo(res)
