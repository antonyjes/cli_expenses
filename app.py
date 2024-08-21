import click
from crud import add, list, delete

@click.group()
def cli():
    pass

# Main CRUD commands
cli.add_command(add)
cli.add_command(list)
cli.add_command(delete)

if __name__ == '__main__':
    cli()