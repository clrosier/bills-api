from flask import request
from flask_restplus import Resource

from ..util.dto import ExpenseDto
from app.main.util.decorator import token_required
from app.main.service.auth_helper import Auth

from ..service.expense_service import save_new_expense, get_user_expenses, get_expense

api = ExpenseDto.api
expense = ExpenseDto.bill


@api.route('/')
class ExpensesList(Resource):
    @api.doc('list_of_users_expenses')
    @token_required
    def get(self):
        """List all user's expenses"""
        owner = Auth.get_logged_in_user(request)[0]['data']['email']
        return get_user_expenses(owner)


    @api.response(201, 'Expense successfully created.')
    @api.doc('add a new expense')
    @api.expect(expense, validate=True)
    @token_required
    def post(self):
        """Creates a new Expense"""
        owner = Auth.get_logged_in_user(request)[0]['data']['email']
        data = request.json
        return save_new_expense(data=data, owner=owner)


@api.route('/<expense_id>')
@api.param('expense_id', 'The Expense identifier')
@api.response(404, 'Expense not found')
class Expense(Resource):
    @api.doc('get a expense')
    @api.marshal_with(expense)
    @token_required
    def get(self, expense_id):
        """get an expense given its identifier"""
        expense = get_expense(expense_id)
        if not expense:
            api.abort(404)
        else:
            return expense
