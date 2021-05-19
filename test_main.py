# from typer.testing import CliRunner

# from .main import app

# runner = CliRunner()

# def test_app():
#     result = runner.invoke(app, ["Camila", "--city", "Berlin"])
#     assert result.exit_code == 0
#     assert "Hello Camila" in result.stdout
#     assert "Let's have a coffee in Berlin" in result.stdout


from typer.testing import CliRunner

from .main import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["Camila"], input="camila@example.com\n")
    assert result.exit_code == 0
    assert "Hello Camila, your email address is: camila@example.com" in result.stdout

# import typer
# from typer.testing import CliRunner
# from .main import main

# app = typer.Typer()
# app.command()(main)

# runner = CliRunner()

# def test_app():
#     result = runner.invoke(app, ["--name"], ["Camila"])
#     assert result.exit_code == 0
#     assert "Hello Camila" in result.stdout