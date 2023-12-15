#! /usr/bin/env python3

from rich.console import Console
from rich import print
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.table import Table, Column


# !text/color
console = Console()
# console.print("Hello World!")

#  style format
# console.log("Hello World!", style="bold yellow")

#  span format
console.print("Hello [bold yellow]Monroe[/bold yellow]!")
print("[u]Hello[/u] [bold magenta]Monroe[/bold magenta]!")


# !emoji
console.print("I :heart: coding :smiley:")

# !markdown
with open("README.md") as md_file:
    markdown = Markdown(md_file.read())
    console.print(markdown)

# !syntax
my_code = '''
def hello(name):
    return f"Hello {name}"
'''

syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
console.print(syntax)


# !table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Title", style="bold", width=12)
table.add_column("Author", style="bold", width=12)

table.add_row("The Pearl", "John Steinbeck")

console.print(table)


'''
rich 
package for rich text in terminal

installation
pipenv install rich
pipenv install commonmark

features
color
style
emoji
syntax
tables
markdown
etc.

'''
