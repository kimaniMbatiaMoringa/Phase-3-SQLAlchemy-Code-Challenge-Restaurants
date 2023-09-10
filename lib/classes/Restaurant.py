from functools import reduce

class Restaurant:   
    def __init__(self,name):
        self.name = name
        self.ratings = []
        self.agg = 0
        self.customer_list = []

    def name(self):
        return self.name
    
    def average_star_rating(self):
        self.agg =sum(self.ratings) / len(self.ratings)
        print(self.agg)
    
    def set_rating(self,value):
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