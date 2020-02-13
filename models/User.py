import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String

Base = sqlalchemy.ext.declarative.declarative_base()

class User(Base):
    __tablename__ = 'users'
    name = Column(String(50), primary_key=True)
    password = Column(String(50))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @classmethod
    def migration(cls, engine):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

if __name__ == "__main__":
    pass