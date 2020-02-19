from datetime import datetime, timedelta
import calendar

from app.main import db
from app.main.model.expense import Expense

from app.main.util.helpers import get_date

from flask import jsonify


def save_new_expense(data, owner):
    new_expense = Expense(
        owner = owner,
        name = data['name'],
        description = data['description'],
        amount = data['amount'],
        created_on = datetime.utcnow()
    )
    save_changes(new_expense)
    response_object = {
        'status': 'success',
        'message': 'Expense successfully created.'
    }
    return response_object, 201


def get_user_expenses(owner):
    expenses = Expense.query.filter_by(owner=owner).all()

    expense_list = [make_expense_object(expense) for expense in expenses]

    print(expense_list)
    response_object = {
        'status': 'success',
        'expenses': expense_list
    }
    return response_object, 200


def make_expense_object(expense):
    expense_object = {
        'name': expense.name,
        'description': expense.description,
        'amount': expense.amount,
    }
    return expense_object


def get_expense(data):
    pass


def save_changes(data):
    db.session.add(data)
    db.session.commit()
