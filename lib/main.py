from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,ForeignKey,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base,relationship

import ipdb


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

    def given_name(self):
        engine = create_engine('sqlite:///restaurants.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
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

class Restaurant(Base):

    __tablename__='restaurants'

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
    price = Column(Integer())


    def __init__(self,name,price):
        self.name = name
        self.ratings = []
        self.agg = 0
        self.customer_list = []
        self.price = price

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

class Review(Base):

    __tablename__='review'                           #Creates a customers table

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


    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    #customer = relationship('Customer', back_populates='reviews')
    #restaurant = relationship('Restaurant', back_populates='reviews')

    def __init__(self,customer_inp,restaurant_inp, rating):
        self.customer_obj = customer_inp
        self.restaurant_obj = restaurant_inp
        self.rating = restaurant_inp.set_rating(rating)

    def customer(self):
        return self.customer_obj.name
    
    def restaurant(self):
        return self.restaurant_obj
        
        
    def rating(self):
        return self.rating
    
    

if __name__ == '__main__':                      
    engine = create_engine('sqlite:///restaurants.db',echo=True) #Creates a db called students.db
    Base.metadata.create_all(engine)                            #Uses the schema in the student class as a base for the tables created


kimani_mbatia = Customer(
    name="Kimani",
    family="Mbatia",
)

mong_kok = Restaurant(
    name="Mong Kok",
    price=100,
)

review1 = Review(
    customer_inp=kimani_mbatia,
    restaurant_inp=mong_kok,
    rating=4 
)

Session = sessionmaker(bind=engine)
session = Session()
session.add(kimani_mbatia)
session.add(mong_kok)
session.add(review1)
session.commit()


ipdb.set_trace()

#JOIN table using customer id 