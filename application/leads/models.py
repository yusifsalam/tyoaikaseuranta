from application import db
from application.models import Base
from sqlalchemy.sql import text


class Lead(Base):
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('leads', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, project_id, user_id):
        self.project_id = project_id
        self.user_id = user_id


    @staticmethod
    def findByProjectAndUser(project_id, user_id):
        stmt = text('SELECT Lead.id FROM Lead '
                    'JOIN Project ON Lead.project_id = Project.id '
                    'JOIN Account ON Lead.user_id = Account.id '
                    'WHERE (Lead.project_id = :project_id AND Lead.user_id = :user_id)')\
            .params(project_id=project_id, user_id=user_id)
        res = db.engine.execute(stmt)
        resp = []
        for row in res:
            resp.append(row[0])
        return resp
