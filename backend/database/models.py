from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
import sqlalchemy.types as types

Base = declarative_base()


class ChoiceType(types.TypeDecorator):
    impl = types.String(32)

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.items() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,  autoincrement=True, index=True, unique=True)
    # username = Column(String(32), unique=True)
    fullname = Column(String(32))
    student_id = Column(String(32), unique=True)
    email = Column(String(32), unique=True)
    password = Column(String(255))


class Bookings(Base):
    """ Bookings to user mapping """
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    device_id = Column(Integer)
    user_id = Column(Integer)
    status = Column(ChoiceType(
        {0: 'available', 1: 'booked', 2: 'unavailable'},
    ), default=0, nullable=False)


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    name = Column(String(32))  # Example: "Компьютер 12"
    type = Column(ChoiceType(
        {0: 'PC', 1: 'Billiard', 2: 'Console', 3: 'VR'}
    ), nullable=False)
