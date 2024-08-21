import click
from utils import load_json, date_format

# Total expenses
@click.command()
@click.option('--year', default=None, required=False)
def summary(year):
    total_expenses = 0
    data = load_json('expenses.json')

    for expense in data['expenses']:
        if year:
            if date_format(expense['date']).year == int(year):
                total_expenses += expense['amount']
        else:
            total_expenses += expense['amount']
    
    if year:
        click.echo(f"Total expenses in {year}: {total_expenses}")
    else:
        click.echo(f"Total expenses: {total_expenses}")
