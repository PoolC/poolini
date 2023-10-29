import click

from .seminar import seminar
from .user import user


def cli_static_factory(permissions="user") -> click.CommandCollection:
    return click.CommandCollection(sources=[seminar, user])


if __name__ == "__main__":
    poolini = cli_static_factory()
    poolini()
