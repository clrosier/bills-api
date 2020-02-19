from .. import db

class Bill(db.Model):
    """ Bill Model for storing bill related details """
    __tablename__ = "bill"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String(255), db.ForeignKey("user.email"))
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    amount = db.Column(db.Float(), nullable=False)
    first_occurrence = db.Column(db.Date, nullable=False)
    period = db.Column(db.String(15), nullable=False)
    next_occurrence = db.Column(db.Date, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
