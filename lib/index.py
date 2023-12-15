#! /usr/bin/env python3
# saves the hustle of having to run python3 lib/index.py

import click
import click_config_file


@click.command()
# !basic option
@click.option("--name", "-n", default="John", help="Provide user name")
# !multiple values
@click.option("--salary", "-s", nargs=2, help="Provide monthly salary", type=int)
# !multiple options
@click.option("--location", "-l", help="Provide locations visited", multiple=True)
def main(name, salary, location):
    # different in python versions/use click.echo() instead
    # print(f"My name is : {name}\nMy salary is: {sum(salary)}")

    click.echo(
        f"My name is : {name}\nMy salary is: {sum(salary)}\nLocations visited: {location}")



# !working with args/args are a must to pass
@click.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello {name}")


# !multiple args
@click.command()
@click.argument("num1", type=int)
@click.argument("num2", type=int)
@click.argument("operation", default="sum")
def operate(num1, num2, operation):
    '''Add num1 and num2'''

    if operation == "sum":
        # result = int(num1)+int(num2)
        result = num1 + num2
    elif operation == "subtract":
        if num1 > num2:
            result = num1 - num2
        else:
            result = num2 - num1
    elif operation == "multiply":
        result = num1 * num2

    click.echo(result)


# !multiple values
@click.command()
@click.argument("source", nargs=-1)
@click.argument("destination", nargs=1)
def move_files(source, destination):
    for item in source:
        click.echo(f"Moving {item} to folder {destination}")


# ! prompting user input
@click.command()
@click.option("--name", prompt=True)
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
# @click.option("--name", prompt="Enter your name: ")
def user_input(name, password):
    # fname = click.prompt("Enter your name: ")
    click.echo(f"Your name is: {name}\nYour password: {password}")


# !working with colors
@click.command()
@click.option("--name", default="John", help="Change the color of text")
def intro(name):
    '''Add color to text fg == foreground bg == background'''
    
    # click.echo(click.style((f"Hello {name}"), fg="blue", bold=True))
    click.secho((f"Hello {name}"), fg="blue", bg="yellow", bold=True)

# TODO: setuptools
'''
1.pipenv install setuptools
2.mycalculator.py
3.setup.py

from setuptools import setup

setup(
    name="mycalculator,
    version="0.1",
    py_modules=["mycalculator"],
    install_requires=["click"]
    entry-points="
    [console_scripts]
    mycalculator=mycalculator:main
    "
)

4.pipenv install --editable
'''
@click.command()
@click.option("--name", "-n", default="John")
@click.option("--salary", "-s")
@click_config_file.configuration_option()

def name_salary(name, salary):
    click.echo(f"Your name is {name}\nYour salary is: {salary}")

if __name__ == "__main__":
    # main()
    # greet()
    # operate()
    # move_files()
    # user_input()
    # intro()
    name_salary()
