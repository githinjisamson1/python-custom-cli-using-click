#! /usr/bin/env python3 

import click

@click.group()
def main():
    pass

@main.command()
@click.argument("text")
def say(text):
    click.echo(f"You said {text}")

@main.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello {name}")
    
if __name__ =="__main__":
    main()