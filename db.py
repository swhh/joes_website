from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine('postgres://ikzsogicqzfoqk:zHHnNISnb4YH-2S8YiH5F9ES1U@ec2-107-20-136-89.compute-1.amazonaws.com:5432/d5c6j70ceof3k4', echo=True)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    message = Column(String(500))
    email = Column(String(20))
    date = Column(String(50))

    def __repr__(self):
        return "<Message(name='%s', email='%s', message='%s', date='%s')>" % (self.name, self.email, self.message, self.date)


Base.metadata.create_all(engine)