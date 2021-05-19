# typer

# from typing import Optional

# def type_example(name: str, formal: bool = False, intro: Optional[str] = None):
#     pass

# import typer

# def main():
#     typer.echo("Hello World")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str, lastname: str, formal: bool = False):
#     if formal:
#         typer.echo(f"Good day Ms. {name} {lastname}.")
#     else:
#         typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str, lastname: str = "", formal: bool = False):
#     if formal:
#         typer.echo(f"Good day Ms. {name} {lastname}.")
#     else:
#         typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str, lastname: str = "", formal: bool = False):
#     """
#     Say hi to NAME, optionally with a --lastname.

#     If --formal is used, say hi very formally.
#     """
#     if formal:
#         typer.echo(f"Good day Ms. {name} {lastname}.")
#     else:
#         typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main():
#     typer.echo("Hello World")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(good: bool = True):
#     message_start = "everything is "
#     if good:
#         ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
#     else:
#         ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
#     message = message_start + ending
#     typer.echo(message)


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str):
#     typer.secho(f"Welcome here {name}", fg=typer.colors.MAGENTA)


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main():
#     typer.echo(f"Here is something written to standard error", err=True)


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# existing_usernames = ["rick", "morty"]


# def maybe_create_user(username: str):
#     if username in existing_usernames:
#         typer.echo("The user already exists")
#         raise typer.Exit()
#     else:
#         typer.echo(f"User created: {username}")


# def send_new_user_notification(username: str):
#     # Somehow send a notification here for the new user, maybe an email
#     typer.echo(f"Notification sent for new user: {username}")


# def main(username: str):
#     maybe_create_user(username=username)
#     send_new_user_notification(username=username)


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(username: str):
#     if username == "root":
#         typer.echo("The root user is reserved")
#         raise typer.Exit(code=1)
#     typer.echo(f"New user created: {username}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(username: str):
#     if username == "root":
#         typer.echo("The root user is reserved")
#         raise typer.Abort()
#     typer.echo(f"New user created: {username}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument(...)):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Optional

# import typer


# def main(name: Optional[str] = typer.Argument(None)):
#     if name is None:
#         typer.echo("Hello World!")
#     else:
#         typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("Wade Wilson")):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import random

# import typer


# def get_name():
#     return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


# def main(name: str = typer.Argument(get_name)):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str, lastname: str = "", formal: bool = False):
#     """
#     Say hi to NAME, optionally with a --lastname.

#     If --formal is used, say hi very formally.
#     """
#     if formal:
#         typer.echo(f"Good day Ms. {name} {lastname}.")
#     else:
#         typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument(..., help="The name of the user to greet")):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument(..., help="The name of the user to greet")):
#     """
#     Say hi to NAME very gently, like Dirk.
#     """
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", help="Who to greet")):
#     """
#     Say hi to NAME very gently, like Dirk.
#     """
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", help="Who to greet", show_default=False)):
#     """
#     Say hi to NAME very gently, like Dirk.
#     """
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(
#     name: str = typer.Argument(
#         "Wade Wilson", help="Who to greet", show_default="Deadpoolio the amazing's name"
#     )
# ):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", metavar="✨username✨")):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", hidden=True)):
#     """
#     Say hi to NAME very gently, like Dirk.
#     """
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", envvar="AWESOME_NAME")):
#     typer.echo(f"Hello Mr. {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"])):
#     typer.echo(f"Hello Mr. {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str = typer.Argument("World", envvar="AWESOME_NAME", show_envvar=False)):
#     typer.echo(f"Hello Mr. {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(
#     name: str,
#     lastname: str = typer.Option("", help="Last name of person to greet."),
#     formal: bool = typer.Option(False, help="Say hi formally."),
# ):
#     """
#     Say hi to NAME, optionally with a --lastname.

#     If --formal is used, say hi very formally.
#     """
#     if formal:
#         typer.echo(f"Good day Ms. {name} {lastname}.")
#     else:
#         typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(fullname: str = typer.Option("Wade Wilson", show_default=False)):
#     typer.echo(f"Hello {fullname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str, lastname: str = typer.Option(...)):
#     typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name: str, lastname: str = typer.Option(..., prompt=True)):
#     typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(
#     name: str, lastname: str = typer.Option(..., prompt="Please tell me your last name")
# ):
#     typer.echo(f"Hello {name} {lastname}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(project_name: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
#     typer.echo(f"Deleting project {project_name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(
#     name: str, email: str = typer.Option(..., prompt=True, confirmation_prompt=True)
# ):
#     typer.echo(f"Hello {name}, your email is {email}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(
#     name: str,
#     password: str = typer.Option(
#         ..., prompt=True, confirmation_prompt=True, hide_input=True
#     ),
# ):
#     typer.echo(f"Hello {name}. Doing something very secure with password.")
#     typer.echo(f"...just kidding, here it is, very insecure: {password}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(user_name: str = typer.Option(..., "--name")):
#     typer.echo(f"Hello {user_name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(user_name: str = typer.Option(..., "--name", "-n")):
#     typer.echo(f"Hello {user_name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(user_name: str = typer.Option(..., "-n")):
#     typer.echo(f"Hello {user_name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(user_name: str = typer.Option(..., "--user-name", "-n")):
#     typer.echo(f"Hello {user_name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(
#     name: str = typer.Option(..., "--name", "-n"),
#     formal: bool = typer.Option(False, "--formal", "-f"),
# ):
#     if formal:
#         typer.echo(f"Good day Ms. {name}.")
#     else:
#         typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def name_callback(value: str):
#     if value != "Camila":
#         raise typer.BadParameter("Only Camila is allowed")
#     return value


# def main(name: str = typer.Option(..., callback=name_callback)):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def name_callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
#     if ctx.resilient_parsing:
#         return
#     typer.echo(f"Validating param: {param.name}")
#     if value != "Camila":
#         raise typer.BadParameter("Only Camila is allowed")
#     return value


# def main(name: str = typer.Option(..., callback=name_callback)):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Optional

# import typer

# __version__ = "0.1.0"


# def version_callback(value: bool):
#     if value:
#         typer.echo(f"Awesome CLI Version: {__version__}")
#         raise typer.Exit()


# def main(
#     name: str = typer.Option("World"),
#     version: Optional[bool] = typer.Option(
#         None, "--version", callback=version_callback
#     ),
# ):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Optional

# import typer

# __version__ = "0.1.0"


# def version_callback(value: bool):
#     if value:
#         typer.echo(f"Awesome CLI Version: {__version__}")
#         raise typer.Exit()


# def name_callback(name: str):
#     if name != "Camila":
#         raise typer.BadParameter("Only Camila is allowed")


# def main(
#     name: str = typer.Option(..., callback=name_callback),
#     version: Optional[bool] = typer.Option(
#         None, "--version", callback=version_callback
#     ),
# ):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def name_callback(value: str):
#     if value != "Camila":
#         raise typer.BadParameter("Only Camila is allowed")
#     return value


# def main(name: str = typer.Option(..., callback=name_callback)):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Optional

# import typer

# __version__ = "0.1.0"


# def version_callback(value: bool):
#     if value:
#         typer.echo(f"Awesome CLI Version: {__version__}")
#         raise typer.Exit()


# def name_callback(name: str):
#     if name != "Camila":
#         raise typer.BadParameter("Only Camila is allowed")
#     return name


# def main(
#     name: str = typer.Option(..., callback=name_callback),
#     version: Optional[bool] = typer.Option(
#         None, "--version", callback=version_callback, is_eager=True
#     ),
# ):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer


# def main(name:str):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# app = typer.Typer()


# @app.command()
# def main(name:str):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()


# @app.command()
# def create():
#     typer.echo("Creating user: Hiro Hamada")


# @app.command()
# def delete():
#     typer.echo("Deleting user: Hiro Hamada")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()


# @app.command()
# def create(username: str):
#     typer.echo(f"Creating user: {username}")


# @app.command()
# def delete(username: str):
#     typer.echo(f"Deleting user: {username}")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()


# @app.command()
# def create(username: str):
#     typer.echo(f"Creating user: {username}")


# @app.command()
# def delete(username: str, force: bool =typer.Option(..., prompt="Are you sure you want to delete the user?")):
#     if force:
#         typer.echo(f"Deleting user: {username}")
#     else:
#         typer.echo("Operation cancelled")


# @app.command()
# def delete_all(force: bool = typer.Option(..., prompt="Are you sure you want to delete ALL users?")):
#     if force:
#         typer.echo("Deleting all users")
#     else:
#         typer.echo("Operation cancelled")

# @app.command()
# def init():
#     typer.echo("Initializing user databases")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer(help="Awesome CLI user manager")

# @app.command()
# def create(username: str):
#     """Create a new user with USERNAME."""
#     typer.echo(f"Creating user: {username}")

# @app.command()
# def delete(username: str, force: bool = typer.Option(..., prompt="Are you sure you want to delete the user?", help="Force deletion without confirmation.")):
#     """Delete a user with USERNAME.
#     If --force is not used, will ask for confirmation."""
#     if force:
#         typer.echo(f"Deleting user: {username}")
#     else:
#         typer.echo("Operation cancelled")

# @app.command()
# def delete_all(foce: bool = typer.Option(..., prompt="Are you sure you want to delete ALL users?")):
#     """Delete ALL users in the database.
#     If --force is not used, will ask for confirmation."""
#     if force:
#         typer.echo("Deleting all users")
#     else:
#         typer.echo("Operation cancelled")

# @app.command()
# def init():
#     """Initialize the users database."""
#     typer.echo("Initializing user database")

# if __name__ == "__main__":
#     app()

# import typer
# app = typer.Typer()

# @app.command(help="Create a new user with USERNAME.")
# def create(username: str):
#     """Some internal utility function to create."""
#     typer.echo(f"Creating user: {username}")


# @app.command(help="Delete a user with USERNAME.")
# def delete(username: str):
#     """Some internal utility function to delete."""
#     typer.echo(f"Deleting user: {username}")

# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.command("create")
# def cli_create_user(username: str):
#     typer.echo(f"Creating user: {username}")


# @app.command("delete")
# def cli_delete_user(username: str):
#     typer.echo(f"Deleting user: {username}")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()
# state = {"verbose": False}

# @app.command()
# def create(username: str):
#     if state["verbose"]:
#         typer.echo("About to create a user")
#     typer.echo(f"Creating user: {username}")
#     if state["verbose"]:
#         typer.echo("Just created a user")

# @app.command()
# def delete(username: str):
#     if state[verbose]:
#         typer.echo("About to delete a user")
#     typer.echo(f"Deleting user: {username}")
#     if state[verbose]:
#         typer.echo("Just deleted a user")

# @app.callback()
# def main(verbose: bool = False):
#     """Manage users in the awesome CLI app."""
#     if verbose:
#         typer.echo("Will write verbose output")
#         state["verbose"] = True

# if __name__ == "__main__":
#     app()

# import typer

# def callback():
#     typer.echo("Running a command")

# app = typer.Typer(callback=callback)

# @app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# if __name__ == "__main__":
#     app()

# import typer

# def callback():
#     typer.echo("Running a command")

# app = typer.Typer(callback=callback)

# @app.callback()
# def new_callback():
#     typer.echo("Override callback, running a command")

# @app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.callback()
# def callback():
#     """Manage users CLI app.
#     Use it with the create command.
#     A new user with the given NAME will be created."""

# @app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.command()
# def create():
#     typer.echo("Creating user: Hiro Hamada")

# @app.command()
# def delete():
#     typer.echo("Deleting user: Hiro Hamada")

# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.command()
# def create():
#     typer.echo("Creating user: Hiro Hamada")


# @app.callback()
# def callback():
#     """Creates a single user Hiro Hamada.

#     In the next version it will create 5 users more."""


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# @app.command()
# def delete(name: str):
#     typer.echo(f"Deleting user: {name}")


# @app.callback()
# def main(ctx: typer.Context):
#     """Manage users in the awesome CLI app."""
#     typer.echo(f"About to execute command: {ctx.invoked_subcommand}")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# @app.command()
# def delete(name: str):
#     typer.echo(f"Deleting user: {name}")

# @app.callback(invoke_without_command=True)
# def main(ctx: typer.Context):
#     """Manage users in the awesome CLI app."""
#     if ctx.invoked_subcommand is None:
#         typer.echo("Initializing database")


# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# @app.command(context_settings = {"allow_extra_args": True, "ignore_unknown_options": True})
# def main(ctx: typer.Context):
#     for extra_arg in ctx.args:
#         typer.echo(f"Got an extra arg: {extra_arg}")
    
# if __name__ == "__main__":
#     app()

# import typer

# def main(name: str, age: int=20, height_meters: float= 1.89, female: bool = True):
#     typer.echo(f"NAME is {name}, of type {type(name)}")
#     typer.echo(f"--age is {age}, of type {type(age)}")
#     typer.echo(f"--height-meters is {height_meters}, of type {type(height_meters)}")
#     typer.echo(f"--female is {female}, of type {type(female)}")

# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(id: int= typer.Argument(..., min=0, max=1000), rank: int= typer.Option(0, max=10, clamp=True), score: float = typer.Option(0, min=0, max=100, clamp=True)):
#     typer.echo(f"ID is {id}")
#     typer.echo(f"--rank is {rank}")
#     typer.echo(f"--score is {score}")


# if __name__ == "__main__":
#     typer.run(main)


# import typer

# def main(verbose: int = typer.Option(0, "--verbose", "--v", count = True)):
#     typer.echo(f"Verbose level is {verbose}")

# if __name__ == "__main__":
#     typer.run(main)


# import typer

# def main(force: bool = typer.Option(False, "--force")):
#     if force:
#         typer.echo("Forcing operation")
#     else:
#         typer.echo("Not forcing")
    

# if __name__ == "__main__":
#     typer.run(main)

# from typing import Optional

# import typer

# def main(accept: Optional[bool] = typer.Option(None, "--accept/--reject")):
#     if accept is None:
#         typer.echo("I don't know what you want yet")
#     elif accept:
#         typer.echo("Accepting!")
#     else:
#         typer.echo("Rejecting!")

# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(force: bool = typer.Option(False, "--force/--no-force", "--f/--F")):
#     if force:
#         typer.echo("Forcing operation")
#     else:
#         typer.echo("Not forcing")

# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(in_prod: bool = typer.Option(True, " /--demo", " /-d")):
#     if in_prod:
#         typer.echo("Running in production")
#     else:
#         typer.echo("Running demo")
    

# if __name__ == "__main__":
#     typer.run(main)

# from uuid import UUID

# import typer

# def main(user_id: UUID):
#     typer.echo(f"USER_ID is {user_id}")
#     typer.echo(f"UUID version is {user_id.version}")

# if __name__ == "__main__":
#     typer.run(main)

# from datetime import datetime

# import typer

# def main(birth: datetime):
#     typer.echo(f"Interesting day to be born: {birth}")
#     typer.echo(f"Birth hour: {birth.hour}")

# if __name__ == "__main__":
#     typer.run(main)

# from datetime import datetime

# import typer

# def main(launch_date: datetime = typer.Argument(..., formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y"])):
#     typer.echo(f"Launch will be at: {launch_date}")

# if __name__ == "__main__":
#     typer.run(main)

# from enum import Enum

# import typer

# class NeuralNetwork(str, Enum):
#     simple = "simple"
#     conv = "conv"
#     lstm = "lstm"

# def main(network: NeuralNetwork = NeuralNetwork.simple):
#     typer.echo(f"Training neural network of type: {network.value}")

# if __name__ == "__main__":
#     typer.run(main)

# from enum import Enum

# import typer

# class NeuralNetwork(str, Enum):
#     simple = "simple"
#     conv = "conv"
#     lstm = "lstm"

# def main(network: NeuralNetwork = typer.Option(NeuralNetwork.simple, case_sensitive=False)):
#     typer.echo(f"Training neural network of type: {network.value}")

# if __name__ == "__main__":
#     typer.run(main)

# from pathlib import Path
# from typing import Optional

# import typer

# def main(config: Path = typer.Option(..., exists=True, file_okay=True, dir_okay=True, writable=True, readable=True, resolve_path=True)):
#         text = config.read_text()
#         typer.echo(f"Config file contents: {text}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(config: typer.FileText = typer.Option(...)):
#     for line in config:
#         typer.echo(f"Config line: {line}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(config: typer.FileTextWrite = typer.Option(...)):
#     config.write("Some config written by the app")
#     typer.echo("Config written")

# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(file: typer.FileBinaryRead = typer.Option(...)):
#     processed_total = 0
#     for bytes_chunk in file:
#         #Process the bytes in bytes_chunk
#         processed_total += len(bytes_chunk)
#     typer.echo(f"Processed bytes total: {processed_total}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(file: typer.FileBinaryWrite = typer.Option(...)):
#     first_line_str = "some settings\n"
#     #You cannot write str directly to a binary file, you have to encode it to get bytes
#     first_line_bytes = first_line_str.encode("utf-8")
#     #Then you can write the bytes
#     file.write(first_line_bytes)
#     #This is already bytes, it starts with b
#     second_line = b"la cig\xc3\xbce\xc3\xb1a trae al ni\xc3\xb1o"
#     file.write(second_line)
#     typer.echo("Binary file written")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main(config: typer.FileText = typer.Option(..., mode = "a")):
#     config.write("This is a single line\n")
#     typer.echo("Config line written")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# app = typer.Typer()

# @app.command()
# def create(item: str):
#     typer.echo(f"Creating item: {item}")

# @app.command()
# def delete(item: str):
#     typer.echo(f"Deleting item: {item}")

# @app.command()
# def sell(item: str):
#     typer.echo(f"Selling item: {item}")


# if __name__ == "__main__":
#     app()

# import typer

# import items
# import users


# app = typer.Typer()
# app.add_typer(users.app, name="users")
# app.add_typer(items.app, name="items")

# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()
# items_app = typer.Typer()
# app.add_typer(items_app, name = "items")
# users_app = typer.Typer()
# app.add_typer(users_app, name = "users")

# @items_app.command("create")
# def items_create(item: str):
#     typer.echo(f"Creating item: {item}")

# @items_app.command("delete")
# def items_delete(item: str):
#     typer.echo(f"Deleting item: {item}")

# @items_app.command("sell")
# def items_sell(item: str):
#     typer.echo(f"Selling item: {item}")

# @users_app.command("create")
# def users_create(user_name: str):
#     typer.echo(f"Creating user: {user_name}")

# @users_app.command("delete")
# def users_delete(user_name: str):
#     typer.echo(f"Deleting user: {user_name}")


# if __name__ == "__main__":
#     app()

# import typer

# import items
# import lands
# import users

# app = typer.Typer()
# app.add_typer(users.app, name= "users")
# app.add_typer(items.app, name= "items")
# app.add_typer(lands.app, name= "lands")

# if __name__ == "__main__":
#     app()

# import typer

# app = typer.Typer()

# def default_callback():
#     typer.echo("Running a users command")

# users_app = typer.Typer(callback=default_callback)

# def callback_for_add_typer():
#     typer.echo("I have the high land! Running a users command")

# app.add_typer(users_app, name= "users", callback=callback_for_add_typer)

# @users_app.callback()
# def user_callback():
#     typer.echo("Callback override, running a users command")


# @users_app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# if __name__ == "__main__":
#     app()


# import typer

# app = typer.Typer()

# def old_callback():
#     """Old callback help."""


# users_app = typer.Typer(callback= old_callback, name="exp-users", help="Explicit help.")

# def new_users():
#     """I have the highland! Create some users."""


# app.add_typer(users_app, callback=new_users, name="cake-sith-users", help="Unlimited powder! Eh, users.")

# @users_app.callback("call-users", help="Help from callback for users.")
# def users():
#     """Manage users in the app."""


# @users_app.command()
# def create(name: str):
#     typer.echo(f"Creating user: {name}")


# if __name__ == "__main__":
#     app()

# from typing import List, Optional

# import typer

# def main(number: List[float] = typer.Option([])):
#     typer.echo(f"The sum is {sum(number)}")


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Tuple
# import typer

# def main(user: Tuple[str, int, bool] = typer.Option((None, None, None))):
#     username, coins, is_wizard = user
#     if not username:
#         typer.echo("No user provided")
#         raise typer.Abort()
#     typer.echo(f"The username {username} has {coins} coins")
#     if is_wizard:
#         typer.echo("And this user is a wizard!")


# if __name__ == "__main__":
#     typer.run(main)

# from pathlib import Path
# from typing import List

# import typer

# def main(files: List[Path], celebration: str):
#     for path in files:
#         if path.is_file():
#             typer.echo(f"This file exists: {path.name}")
#             typer.echo(celebration)


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Tuple

# import typer

# def main(names: Tuple[str, str, str] = typer.Argument(("Harry", "Hermione", "Ron"), help= "Select 3 characters to play with")):
#     for name in names:
#         typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main():
#     person_name = typer.prompt("What's your name?")
#     typer.echo(f"Hello {person_name}")

# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main():
#     delete = typer.confirm("Are you sure want to delete it?")
#     if not delete:
#         typer.echo("Not deleting")
#         raise typer.Abort()
#     typer.echo("Deleting it!")


# if __name__ == "__main__":
#     typer.run(main)

# import typer

# def main():
#     delete = typer.confirm("Are you sure you want to delete it?", abort= True)
#     typer.echo("Deleting it!")


# if __name__ == "__main__":
#     typer.run(main)

# import time

# import typer

# def main():
#     total = 0
#     with typer.progressbar(range(100)) as progress:
#         for value in progress:
#             #Fake processing time
#             time.sleep(0.01)
#             total += 1
#     typer.echo(f"Processed {total} things.")


# if __name__ == "__main__":
#     typer.run(main)

# import time
# import typer

# def iterate_user_ids():
#     #Let's imagine this is a web API, not a range()
#     for i in range(100):
#         yield i


# def main():
#     total = 0
#     with typer.progressbar(iterate_user_ids(), length= 100) as progress:
#         for value in progress:
#             #Fake processing time
#             time.sleep(0.01)
#             total += 1
#     typer.echo(f"Processed {total} user IDs.")


# if __name__ == "__main__":
#     typer.run(main)

# import time

# import typer

# def main():
#     total = 0
#     with typer.progressbar(range(100), label= "Processing") as progress:
#         for value in progress:
#             #Fake processing time
#             time.sleep(0.01)
#             total += 1
#     typer.echo(f"Processed {total} things.")


# if __name__ == "__main__":
#     typer.run(main)

# import time
# import typer

# def main():
#     total = 1000
#     with typer.progressbar(length= total) as progress:
#         for batch in range(10):
#             #Fake processing time
#             time.sleep(1)
#             progress.update(100)
#     typer.echo(f"Processed {total} things in batches.")


# if __name__ == "__main__":
#     typer.run(main)

# from pathlib import Path

# import typer

# APP_NAME = "my-super-cli-app"

# def main():
#     app_dir = typer.get_app_dir(APP_NAME)
#     config_path: Path = Path(app_dir) / "config.json"
#     if not config_path.is_file():
#         typer.echo("Config file doesn't exist yet")


# if __name__ == "__main__":
#     typer.run(main)


# import typer

# def main():
#     typer.echo("Opening Typer's docs")
#     typer.launch("https://typer.tiangolo.com")


# if __name__ == "__main__":
#     typer.run(main)

# from pathlib import Path

# import typer


# APP_NAME = "my-super-cli-app"

# def main():
#     app_dir = typer.get_app_dir(APP_NAME)
#     app_dir_path = Path(app_dir)
#     app_dir_path.mkdir(parents=True, exist_ok=True)
#     config_path: Path = Path(app_dir) / "config.json"
#     if not config_path.is_file():
#         config_path.write_text('{"version": "1.0.0"}')
#     config_file_str = str(config_path)
#     typer.echo("Opening config directory")
#     typer.launch(config_file_str, locate=True)


# if __name__ == "__main__":
#     typer.run(main)

# from typing import Optional
# import typer

# app = typer.Typer()

# @app.command()
# def main(name: str, city: Optional[str] = None):
#     typer.echo(f"Hello {name}")
#     if city:
#         typer.echo(f"Let's have a coffee in {city}")


# if __name__ == "__main__":
#     app()

import typer

app = typer.Typer()

@app.command()
def main(name: str, email: str = typer.Option(..., prompt=True)):
    typer.echo(f"Hello {name}, your email is: {email}")


if __name__ == "__main__":
    app()


# import typer

# def main(name: str = "World"):
#     typer.echo(f"Hello {name}")


# if __name__ == "__main__":
#     typer.run(main)