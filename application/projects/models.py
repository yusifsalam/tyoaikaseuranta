from application import db
from application.models import Base
from sqlalchemy.sql import text

projectTask = db.Table('projectTask',
                       db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
                       db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
                       )


class Project(Base):
    name = db.Column(db.String(144), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    tasks = db.relationship("Task", secondary=projectTask, lazy='subquery', backref=db.backref('projects', lazy=True))

    def __init__(self, name):
        self.name = name
        self.completed = False

    @staticmethod
    def get_owner(self):
        sql_stmt = text("SELECT DISTINCT Account.name FROM Account "
                        "LEFT JOIN Project ON Project.account_id = Account.id "
                        "WHERE Account.id = :account_id ").params(account_id=self.account_id)
        res = db.engine.execute(sql_stmt)
        return res.first()[0]
