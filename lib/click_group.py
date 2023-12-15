#! /usr/bin/env python3


import click
import random

# parent/combining commands
@click.group()
def main():
    click.echo("Hello World")
    
@main.command()  
@click.argument("text")  
# @click.option("--text", prompt=True)  
def reverse(text):
    '''Reverse a text'''
    click.echo(text[::-1])

@main.command()
def leet():
    '''Leet a text'''
    pass

@main.command()
@click.argument("text")
def shuffle(text):
    '''Shuffle a text'''
    click.echo("".join(random.sample(text, len(text))))

if __name__ == "__main__":
    main()
    
# TODO:
'''
main command
annotate each command using main

i.e. 
@click.group() == parent

@click.command() == each child
'''