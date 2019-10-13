from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text

userProject = db.Table('userProject',
                       db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
                       db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
                       )


class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    projects = db.relationship("Project", secondary=userProject, lazy='subquery',
                               backref=db.backref('accounts', lazy=True))
    tasks = db.relationship('Task', backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def count_tasks(self):
        stmt = text("SELECT COUNT(Task.id) FROM Task "
                    "WHERE Task.account_id = :account_id").params(account_id=current_user.id)
        res = db.engine.execute(stmt)
        return res.first()[0]
