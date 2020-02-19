from flask import request
from flask_restplus import Resource

from ..util.dto import BillDto
from app.main.util.decorator import token_required
from app.main.service.auth_helper import Auth

from ..service.bill_service import save_new_bill, get_user_bills, get_bill

api = BillDto.api
bill = BillDto.bill


@api.route('/')
class BillList(Resource):
    @api.doc('list_of_users_bills')
    # @api.marshal_list_with(bill, envelope='data')
    @token_required
    def get(self):
        """List all user's bills"""
        owner = Auth.get_logged_in_user(request)[0]['data']['email']
        return get_user_bills(owner)
        # return get_user_bills(request.headers)


    @api.response(201, 'Bill successfully created.')
    @api.doc('add a new bill')
    @api.expect(bill, validate=True)
    @token_required
    def post(self):
        """Creates a new Bill"""
        owner = Auth.get_logged_in_user(request)[0]['data']['email']
        data = request.json
        return save_new_bill(data=data, owner=owner)


@api.route('/<bill_id>')
@api.param('bill_id', 'The Bill identifier')
@api.response(404, 'Bill not found')
class Bill(Resource):
    @api.doc('get a bill')
    @api.marshal_with(bill)
    @token_required
    def get(self, bill_id):
        """get a bill given its identifier"""
        bill = get_bill(bill_id)
        if not bill:
            api.abort(404)
        else:
            return bill
