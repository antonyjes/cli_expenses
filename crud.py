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
        "amount": float(amount),
        "date": datetime.datetime.now().isoformat()
    }

    data = load_json('expenses.json')
    data['expenses'].append(new_expense)
    save_json('expenses.json', data)

    click.echo("Expense added successfully!")


# List all expenses
@click.command()
def list():
    data = load_json('expenses.json')

    click.echo("ID | DESCRIPTION | AMOUNT | DATE")
    for expense in data['expenses']:
        click.echo(f"{expense['id']} | {expense['description']} | {expense['amount']} | {expense['date']}")


# Delete an expense
@click.command()
@click.option('--id', prompt=True)
def delete(id):
    data = load_json('expenses.json')
    
    for expense in data['expenses']:
        if expense['id'] == id:
            data['expenses'].remove(expense)
            break
    
    save_json('expenses.json', data)

    click.echo("Expense deleted successfully!")

