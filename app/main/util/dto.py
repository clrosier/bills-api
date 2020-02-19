from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class BillDto:
    api = Namespace('bills', description='bill related operations')
    bill = api.model('bill_details', {
        'name': fields.String(required=True, description='The name of the bill'),
        'description': fields.String(required=True, description='A description of what the bill is'),
        'amount': fields.Float(required=True, description='The amount payable for the bill'),
        'first_occurrence': fields.Date(required=True, description="When this bill first starts"),
        'period': fields.String(required=True, description='How often the bill occurs: "month-end", "biweekly", "weekly"'),
        'next_occurrence': fields.Date(required=True, description='A representation of when the bill is next due (ex. 2020-02-16)'),
        'paid': fields.Boolean(required=True, description='Whether or not the bill has already been paid')
    })

class ExpenseDto:
    api = Namespace('expenses', description='expense related operations')
    bill = api.model('expense_details', {
        'name': fields.String(required=True, description='The name of the expense'),
        'description': fields.String(required=True, description='A description of what the bill is'),
        'amount': fields.Float(required=True, description='The amount payable for the bill')
    })
