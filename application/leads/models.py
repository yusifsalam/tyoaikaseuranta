from application import db
from application.models import Base


class Lead(Base):
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('leads', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, project_id, user_id):
        self.project_id = project_id
        self.user_id = user_id


