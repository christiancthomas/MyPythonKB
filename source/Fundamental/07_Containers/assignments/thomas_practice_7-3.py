
def total_list(my_list):
    # total the integers in the list
    sum = 0
    for val in my_list:
        sum += val
    return sum
def main():
    # create two lists containing 5 integers of your choosing each
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    #join the two lists together, sort the list, pass it to total_list to get a total
    list3 = list1 + list2
    list3.sort()
    total = total_list(list3)
    # print the list, total, max, and min values
    print(f"Final List: {list3}\nTotal: {total}\nMax: {max(list3)}\nMin: {min(list3)}")

if __name__ == "__main__":
    main()