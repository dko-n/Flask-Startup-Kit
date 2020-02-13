import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String

Base = sqlalchemy.ext.declarative.declarative_base()

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    database = Column(String(50))

    def __init__(self, id, database):
        self.id = id
        self.database = database

    @classmethod
    def migration(cls, engine):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

if __name__ == "__main__":
    pass