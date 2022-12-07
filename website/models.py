from . import db
from flask_login import UserMixin



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(200), nullable=False)
    appt_date = db.Column(db.String(30)) # formatted str date (ex: Tuesday, April 05, 2022)
    appt_date_int = db.Column(db.String(20)) # YYYY-MM-DD str format
    time = db.Column(db.String(20)) # str type, account for untimed tasks
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(30), default="Not Yet Started") # Other Statuses: In Progress, Completed, Cancelled


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    tasks = db.relationship('Task')
