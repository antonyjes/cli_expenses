import click
from utils import load_json

@click.command()
def summary():
    total_expenses = 0
    data = load_json('expenses.json')

    for expense in data['expenses']:
        total_expenses += expense['amount']

    click.echo(f"Total expenses: {total_expenses}")