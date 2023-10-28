import click


@click.group()
def user():
    pass


@user.command()
def activity_time():
    click.echo("총 활동시간은 2시간입니다")
