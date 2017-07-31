from app import db
from datetime import datetime

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(20))
    points = db.Column('points' , db.Integer)
    date = db.Column('date' , db.DateTime)

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.date = datetime.now()
