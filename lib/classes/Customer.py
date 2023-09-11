from classes.Review import Review

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Customer(Base):
    instances=[]

    __tablename__='customers'                           #Creates a customers table

    __table_args__=(
        PrimaryKeyConstraint(
            'id',
            name='id_pk'
        ),
        UniqueConstraint(
            'name',
            name='unique_name'
        )
    )

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    family = Column(String())


    def __init__(self,name, family):
        self.name =name
        self.family = family
        #self.instances.append(self)
        #self.review_count=[]
        engine = create_engine('sqlite:///restaurants.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()

    def given_name(self):
        return self.name

    def familyname(self):
        return self.family

    def full_name(self):
        return self.name + " " + self.family
    
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




