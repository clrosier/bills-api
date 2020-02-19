# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.bill_controller import api as bill_ns
from .main.controller.expense_controller import api as expense_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='BILL API',
          version='0.1',
          description='A RESTful API for tracking bills and expenses'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(bill_ns)
api.add_namespace(expense_ns)
