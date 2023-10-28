import click

from .seminar import seminar
from .user import user

poolini = click.CommandCollection(sources=[seminar, user])

if __name__ == "__main__":
    poolini()
