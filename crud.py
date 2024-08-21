import click
from utils import load_json, save_json
import uuid
import datetime

# Create a new expense
@click.command()
@click.option('--description', prompt=True)
@click.option('--amount', prompt=True)
def add(description, amount):
    new_expense = {
        "id": str(uuid.uuid4()),
        "description": description,
        "amount": amount,
        "date": datetime.datetime.now.isoformat()
    }

    data = load_json('expenses.json')
    data['expenses'].append(new_expense)
    save_json('expenses.json', data)

    click.echo("Expense added successfully!")

