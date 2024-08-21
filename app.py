import click
from crud import add, list, delete
from summary import summary, year

@click.group()
def cli():
    pass

# Main CRUD commands
cli.add_command(add)
cli.add_command(list)
cli.add_command(delete)

# Summary command
cli.add_command(summary)

if __name__ == '__main__':
    cli()