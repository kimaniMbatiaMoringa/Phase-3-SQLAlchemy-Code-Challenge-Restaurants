from Review import Review

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Customer(Base):
    __tablename__='customers'                           #Creates a customers table

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    family_name = Column(String())



    def __init__(self,name, family_name):
        self.name =name
        self.family_name = family_name
        self.instances.append(self)
        self.review_count=[]

    def given_name(self):
        return self.name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return self.name + " " + self.family_name
    
    def __str__(self) -> str:
        return f"Name: {self.name}"
    
    def all(self):
        for item in self.instances:
            print(item.name)

    def add_review(self,restaurant, rating):
         review = Review(self,restaurant,rating)
         restaurant.add_customer(self.full_name())
         self.review_count.append(1)
         return review.customer()

    def num_reviews(self):
        print(len(self.review_count))

    def restaurants(self):
        pass    


#sfdsfsd

if __name__=='__main__':
        engine = create_engine('sqlite:///restaurants.db', echo=True)
        Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

