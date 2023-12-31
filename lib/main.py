from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,ForeignKey,
    Index, Column, DateTime, Integer, String,delete)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base,relationship,backref

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
    reviewsList = relationship("Review",back_populates=("customers"))    


    def __init__(self,name, family):
        self.name =name
        self.family = family
        #self.instances.append(self)
        self.review_count=[]

    def given_name(self):
        engine = create_engine('sqlite:///restaurants.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return self.name

    def familyname(self):
        return self.family

    def full_name(self):
        #return self.name + " " + self.family
        result = session.query(Customer).where(Customer.id==self.id).first()
        print(result.name + " " + result.family)
    
    def favorite_restaurant(self):
        result = session.query(Review).where(Review.customer_id==self.id)

    def __str__(self) -> str:
        return f"Name: {self.name}"
    
    def all(self):
        for item in self.instances:
            print(item.name)

    def add_review(self,rating):
         review = Review(rating)
         self.reviewsList.append(review)
         #restaurant.add_customer(self.full_name())
         #self.review_count.append(1)
         session.add(review)
         session.commit()
         #return review.customer()

    def delete_reviews(self):
        reviewlist = session.query(Review).where(Review.customer_id==self.id).all()
        print(reviewlist)
        for i in reviewlist:
            session.delete(i)
        session.commit()       

    def restaurants(self):
        pass

    def reviews(self):
        session.query(Review).where(Review.customer_id==self.id)

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
    customers = relationship("Customer", back_populates="restaurants")


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
    )

    id = Column(Integer, primary_key=True)
    rating = Column(Integer())
    customer_id = Column(Integer, ForeignKey('customers.id'))        #gets the Id of the customer who created the re
    #restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  
    customers = relationship('Customer', back_populates='reviewsList')
    #restaurant = relationship('Restaurant', back_populates='reviews')

    def __init__(self,rating):
        #self.customer_obj = customer_id
        #self.restaurant_obj = restaurant_id
        self.rating = rating

    def customer(self):
        result =session.query(Customer).where(Customer.id==self.customer_id).first()
        print(result.name)
    
    def restaurant(self):
        return self.restaurant_obj
        
        
    def see_rating(self):
        return self.rating
    
    

if __name__ == '__main__':                      
    engine = create_engine('sqlite:///restaurants.db') #Creates a db called students.db
    Base.metadata.create_all(engine)                            #Uses the schema in the student class as a base for the tables created


kimani_mbatia = Customer(
    name="Kimani",
    family="Mbatia",
)

mong_kok = Restaurant(
    name="Mong Kok",
    price=100,
)

""" review1 = Review(
    customer_inp=kimani_mbatia,
    restaurant_inp=mong_kok,
    rating=4 
)
 """
Session = sessionmaker(bind=engine)
session = Session()
session.add(kimani_mbatia)
session.add(mong_kok)
session.commit()

kimani_mbatia.add_review(4)
kimani_mbatia.add_review(3)


ipdb.set_trace()

#JOIN table using customer id 