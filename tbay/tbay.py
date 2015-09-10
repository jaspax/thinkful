from sqlalchemy import Column, Integer, String, DateTime, Interval, Numeric, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

engine = create_engine('postgresql://jaspax:flavor@localhost/tbay')
session = sessionmaker(bind=engine)()
Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    items = relationship("Item", backref="seller")
    bids = relationship("Bid", backref="bidder")

class Item(Base):
    __tablename__ = "Item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    duration = Column(Interval, default=datetime.timedelta(days=1))
    owner_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    bids = relationship("Bid", backref="item")

class Bid(Base):
    __tablename__ = "Bid"

    id = Column(Integer, primary_key=True)
    price = Column(Numeric)
    bidder_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('Item.id'), nullable=False)

Base.metadata.create_all(engine)
