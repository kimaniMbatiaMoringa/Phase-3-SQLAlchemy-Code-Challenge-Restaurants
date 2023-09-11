from functools import reduce

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Restaurant(Base):

    __tablename__='restaurants'

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    price = Column(Integer())


    def __init__(self,name,price):
        self.name = name
        #self.ratings = []
        #self.agg = 0
        #self.customer_list = []
        self.price = price
        engine = create_engine('sqlite:///restaurants.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()

    def average_star_rating(self):
        pass
        self.agg =sum(self.ratings) / len(self.ratings)
        print(self.agg)
    
    def set_rating(self,value):
        pass
        input = value
        self.ratings.append(input)

    def reviews(self):
        for item in self.ratings:
            print(f"Review: {item} stars")

    def add_customer(self, customer):
        self.customer_list.append(customer)

    def customers(self):
        print("Customers:")
        for item in self.customer_list:
            print(item)                