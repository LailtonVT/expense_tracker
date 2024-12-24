import argparse
import json
import os
from datetime import datetime

# Função para carregar despesas do arquivo JSON
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return []

# Função para salvar despesas no arquivo JSON
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Função para adicionar uma despesa
def add_expense(description, amount):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

# Função para listar todas as despesas
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<5} {'Date':<15} {'Description':<20} {'Amount'}")
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<15} {expense['description']:<20} ${expense['amount']}")

# Função para deletar uma despesa
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    save_expenses(expenses)
    print(f"Expense deleted successfully")

# Função para mostrar o resumo total das despesas
def summary(month=None):
    expenses = load_expenses()
    total = sum(expense["amount"] for expense in expenses if (not month or int(expense["date"].split('-')[1]) == month))
    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")

# Função para analisar os argumentos do comando
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers()

    # Subcomando para adicionar uma despesa
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")
    add_parser.set_defaults(func=lambda args: add_expense(args.description, args.amount))

    # Subcomando para listar todas as despesas
    list_parser = subparsers.add_parser("list", help="List all expenses")
    list_parser.set_defaults(func=lambda args: list_expenses())

    # Subcomando para deletar uma despesa
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")
    delete_parser.set_defaults(func=lambda args: delete_expense(args.id))

    # Subcomando para mostrar o resumo das despesas
    summary_parser = subparsers.add_parser("summary", help="Show a summary of all expenses")
    summary_parser.add_argument("--month", type=int, help="Month for the summary (1-12)")
    summary_parser.set_defaults(func=lambda args: summary(args.month))

    # Parse os argumentos
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
