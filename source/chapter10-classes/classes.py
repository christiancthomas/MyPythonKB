class MyList:
    def __init__(self):
        self.__items = []  # Private list to store elements

    # Method to add an item to the list
    def append(self, item):
        self.__items.append(item)

    # Method to remove an item from the list
    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            raise ValueError(f"Item {item} not found in the list")

    # Method to get an item at a specific index
    def get(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]
        else:
            raise IndexError("Index out of range")

    # Method to display the list
    def display(self):
        return self.__items

    # Method to get the length of the list
    def length(self):
        return len(self.__items)

    # Method to clear the list
    def clear(self):
        self.__items = []

    # Method to check if an item is in the list
    def contains(self, item):
        return item in self.__items

    # Method to get the index of an item in the list
    def index(self, item):
        if item in self.__items:
            return self.__items.index(item)
        else:
            raise ValueError(f"Item {item} not found in the list")

    # __str__ method to display the list as a string
    def __str__(self):
        return str(self.__items)


# Example usage of the MyList class
my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("List after adding elements:", my_list)

my_list.remove(2)
print("List after removing element 2:", my_list)

print("Element at index 1:", my_list.get(1))
print("Length of the list:", my_list.length())
print("Is 3 in the list?", my_list.contains(3))
print("Index of element 3:", my_list.index(3))

my_list.clear()
print("List after clearing:", my_list)
