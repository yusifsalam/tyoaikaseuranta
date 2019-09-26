from application import db
from application.models import Base
from sqlalchemy.sql import text


class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.completed = False

    @staticmethod
    def get_owner(self):
        sql_stmt = text("SELECT DISTINCT Account.name FROM Account "
                        "LEFT JOIN Project ON Project.account_id = Account.id "
                        "WHERE Account.id = :account_id ").params(account_id=self.account_id)
        res = db.engine.execute(sql_stmt)
        print("NOW PRINTING OWNER")
        return res.first()[0]

