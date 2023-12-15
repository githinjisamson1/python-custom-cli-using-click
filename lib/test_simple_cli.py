from click.testing import CliRunner
from simple_cli import main

# unit test


def test_say_in_simple_cli():
    runner = CliRunner()
    # test command + arg
    result = runner.invoke(main, ["say", "Hello"])
    assert "You said Hello" in result.output
    assert result.exit_code == 0


def test_greet_in_simple_cli():
    runner = CliRunner()
    # test command + arg
    result = runner.invoke(main, ["greet", "John"])
    assert "Hello John" in result.output
    # assert result.output == "Hello John\n"    
    assert result.exit_code == 0


# TODO:
'''
pytest
pytest -x
pytest -v
pytest -v -k test_say_in_simple_cli

'''