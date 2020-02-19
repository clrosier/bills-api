from datetime import datetime, timedelta
import calendar

from app.main import db
from app.main.model.bill import Bill

from app.main.util.helpers import get_date

from flask import jsonify


def save_new_bill(data, owner):
    new_bill = Bill(
        owner = owner,
        name = data['name'],
        description = data['description'],
        amount = data['amount'],
        first_occurrence = data['first_occurrence'],
        period = data['period'],
        next_occurrence = get_next_occurence(data['user_local_date'], data['first_occurrence'], data['period']),
        paid = data['paid'],
        created_on = datetime.utcnow()
    )
    save_changes(new_bill)
    response_object = {
        'status': 'success',
        'message': 'Bill successfully created.'
    }
    return response_object, 201

def get_next_occurence(usr_lcl_tm, start, period):
    """
    Takes in a period (which is how often the bill occurs) and calculates the next occurence of the date
    """

    # If start date is later than the user's local time, then we can simply set the next occurence to the start date
    if start >= usr_lcl_tm:
        return start

    if period == 'weekly':
        return datetime.strptime(start, '%Y-%m-%d') + timedelta(days=7)

    if period == 'biweekly':
        return datetime.strptime(start, '%Y-%m-%d') + timedelta(days=14)

    if period == 'month-end':
        start_date = datetime.strptime(usr_lcl_tm, '%Y-%m-%d')  # 2020-01-31
        year = start_date.year
        month = start_date.month
        day = str(calendar.monthrange(year, month)[1])

        if len(str(day)) == 1:
            day = '0' + str(day)

        if len(str(month)) == 1:
            month = '0' + str(month)

        return datetime.strptime('%s-%s-%s' % (year, month, day), '%Y-%m-%d')

def get_user_bills(owner):
    bills = Bill.query.filter_by(owner=owner).all()

    bill_list = [make_bill_object(bill) for bill in bills]

    print(bill_list)
    response_object = {
        'status': 'success',
        'bills': bill_list
    }
    return response_object, 200


def make_bill_object(bill):
    bill_object = {
        'name': bill.name,
        'description': bill.description,
        'amount': bill.amount,
        'first_occurrence': str(bill.first_occurrence),
        'period': bill.period,
        'next_occurrence': str(bill.next_occurrence),
        'paid': bill.paid
    }
    return bill_object


def get_bill(data):
    pass


def save_changes(data):
    db.session.add(data)
    db.session.commit()
