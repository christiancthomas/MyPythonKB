"""
The class below is intended  to represent a database entry  for storing  information  
about  an item sold in a retail  store.


class RetailItem:
    def __init__(self, name, num_on_hand, price):
        self.__name = name
        self.__num_on_hand = num_on_hand
        self.__price = price

    def __str__(self):
        return self.__name+'\t'+'\t'+str(self.__num_on_hand) + '\t'+'\t'+ \
               format(self.__price,".2f")

If the main program contains the following statement, what will be displayed?

item = RetailItem("Hat", 10, 12.50)
print(item)

"""

# print(item) will return the following:

Hat        10       12.50