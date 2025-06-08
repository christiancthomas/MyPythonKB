def main():
    room_length = float(input("Enter the length of the room: "))
    room_width = float(input("Enter the width of the room: "))
    price_per_sq_ft = float(input("Enter the price per square foot: "))
    
    room_area = room_length * room_width
    total_cost = room_area * price_per_sq_ft

    print("Total cost: $", format(total_cost, ".2f"), sep="")

main()
