import click
from utils import load_json, date_format

# Total expenses
@click.command()
@click.option('--year', default=None, required=False)
@click.option('--month', default=None, required=False)
def summary(year, month):
    total_expenses = 0
    data = load_json('expenses.json')

    for expense in data['expenses']:
        if year and month:
            if date_format(expense['date']).year == int(year) and date_format(expense['date']).month == int(month):
                total_expenses += expense['amount']
        elif year and not month:
            if date_format(expense['date']).year == int(year):
                total_expenses += expense['amount']
        elif month and not year:
            if date_format(expense['date']).month == int(month):
                total_expenses += expense['amount']
        else:
            total_expenses += expense['amount']
    
    if year and month:
        click.echo(f"Total expenses in {year}-{month}: {total_expenses}")
    elif year and not month:
        click.echo(f"Total expenses in {year}: {total_expenses}")
    elif month and not year:
        click.echo(f"Total expenses in {month}: {total_expenses}")
    else:
        click.echo(f"Total expenses: {total_expenses}")
