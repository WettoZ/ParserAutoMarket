import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime

engine = create_engine('postgresql+psycopg2://postgres:myhome11@localhost/autobot')
Base = declarative_base()

class Ads(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    id_mark = Column(Integer,  ForeignKey('mark.id'), nullable=False, index=True)
    id_model = Column(Integer,  ForeignKey('model.id'), nullable=False, index=True)
    salone = Column(Integer)
    price = Column(Integer, nullable=False)
    mile = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    motor = Column(String)
    rudder = Column(String)
    trans = Column(String)
    gear = Column(String)
    href = Column(String)
    img = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String )

    def __init__(self, id_mark, id_model, salone, price, mile, year, motor, rudder, trans, gear, href, img, description):
        self.id_mark = id_mark
        self.id_model = id_model
        self.salone = salone
        self.price = price
        self.mile = mile
        self.year = year
        self.motor = motor
        self.rudder =rudder
        self.trans = trans
        self.gear = gear
        self.href = href
        self.img = img
        self.description = description

    def __repr__(self):
        return "<Ads('%s', '%s', '%s', '%s', '%s')>" % (self.id, self.id_mark, self.id_model, self.price, self.mile)

class Mark(Base):
    __tablename__ = 'mark'

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Mark('%s', '%s')>" % (self.id, self.name)

class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    id_mark = Column(Integer, ForeignKey('mark.id'), nullable=False, index=True)

    def __init__(self, name, id_mark):
        self.name = name
        self.id_mark = id_mark

    def __repr__(self):
        return "<Mark('%s', '%s', '%s')>" % (self.id, self.name, self.id_mark)

Base.metadata.create_all(engine)
