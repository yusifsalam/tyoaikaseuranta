from application import db
from application.models import Base


class Task(Base):
    category = db.Column(db.String(144), nullable=False)
    hours = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __init__(self, category, hours, description):
        self.category = category
        self.hours = hours
        self.description = description
