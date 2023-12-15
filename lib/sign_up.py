#! /usr/bin/env python3


import click
from click_params import EMAIL, DOMAIN, PUBLIC_URL

@click.group()
def main():
    pass


@main.command()
@click.option("--name", "-n", prompt=True)
@click.option("--email", "-e", prompt=True, type=EMAIL)
@click.option("--domain", "-d", prompt=True, type=DOMAIN)
@click.option("--website", "-w", prompt=True, type=PUBLIC_URL)
def sign_up(name, email, domain, website):
    '''Register/Signup'''
    click.secho((f"Name: {name}"), fg="green")
    click.secho((f"Email: {email}"), fg="green")
    click.secho((f"Domain: {domain}"), fg="green")
    click.secho((f"Website: {website}"), fg="green")

if __name__ == "__main__":
    main()