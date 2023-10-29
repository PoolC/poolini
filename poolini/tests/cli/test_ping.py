from click.testing import CliRunner
from ...cli.ping import ping


def test_ping() -> None:
    runner = CliRunner()
    res = runner.invoke(ping)

    assert res.exit_code == 0
    assert res.output == "pong\n"
