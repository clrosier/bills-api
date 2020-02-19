from .. import db

class Expense(db.Model):
    """ Expense Model for storing expense related details """
    __tablename__ = "expense"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String(255), db.ForeignKey("user.email"))
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    amount = db.Column(db.Float(), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
