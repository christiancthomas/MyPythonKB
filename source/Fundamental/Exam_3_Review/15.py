"""
class RetailItem:
    def __init__(self, name, num_on_hand, price):
        self.__name = name
        self.__num_on_hand = num_on_hand
        self.__price = price

    def __str__(self):
        return self.__name+'\t'+'\t'+str(self.__num_on_hand) + '\t'+'\t'+ \
               format(self.__price,".2f")

Write  a  very  simple  main function  that creates  a  list  of 
RetailItem objects  to  represent  the following items,  and then  
displays the following:
=============================
Name	Units in Inventory	Price
=============================
Jacket 	12	59.95
Jeans 	40	34.95
Shirt 	20	24.95

"""

from RetailItem import RetailItem

def main():
    items = []
    items.append(RetailItem("Jacket", 12, 59.95))
    items.append(RetailItem("Jeans", 40, 34.95))
    items.append(RetailItem("Shirt", 20, 24.95))

    print("=" * 27)
    print("Name\tUnits in Inventory\tPrice")
    print("=" * 27)

    for item in items:
        print(item)

if __name__ == "__main__":
    main()