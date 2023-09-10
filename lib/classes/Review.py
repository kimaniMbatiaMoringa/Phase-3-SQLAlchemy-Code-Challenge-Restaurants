class Review:
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
    
"""     def get_customer(self):
        return self.customer 
    
    def set_customer(self,value):
        if type(value) == str:
            print("Valid input")
            self._customer = value  """

    #customer = property(fget=get_customer,fset=set_customer)        
