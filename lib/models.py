from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,ForeignKey,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base,relationship,backref

#ONLY use this to create a restaurant table IF and only IF it does not exist
#Also use to add columns

Base = declarative_base()

class Customer(Base):

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
#c

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
#c
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


engine =create_engine('sqlite:///restaurants.db')