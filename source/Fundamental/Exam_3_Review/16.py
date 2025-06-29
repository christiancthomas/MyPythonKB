"""
Add the following two functions to the class:
•  get_total_value, which receives nothing  (except  self, of course), 
and returns the total  value of the items on hand.  For example,  
the total  value of the hats  from the previous problem would be $125.00.
•  set_on_hand, which receives an integer indicating  the number  
of that item that have been received (a positive  integer)  or sold 
(a negative  integer),  and  updates the  object’s  on_hand attribute to 
reflect the change.
"""

class RetailItem:
    def __init__(self, name, num_on_hand, price):
        self.__name = name
        self.__num_on_hand = num_on_hand
        self.__price = price
    
    def get_total_value(self):
        return self.__num_on_hand * self.__price

    def set_on_hand(self, num):
        self.__num_on_hand += num

    def __str__(self):
        return self.__name+'\t'+'\t'+str(self.__num_on_hand) + '\t'+'\t'+ \
               format(self.__price,".2f")