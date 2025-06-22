"""
Christian Thomas
Complete
This program is a date printer.
It reads a string from the user containing a date in the form mm/dd/yyyy.   
It should print the date in the format March 12, 2018.  

Sample dialog:
Enter a date in the format mm/dd/yyyy: 01/16/2018
January 16, 2018
"""
import datetime as d

def main():
    while True:
        try:
            # Validation checks
            date = input("Enter date in mm/dd/yyyy format: ")
            date_split = date.split("/")

            for i in date_split:
                if not i.isdigit():
                    raise ValueError("Only allowed values are numbers and \"/\" characters.")
            if len(date_split) != 3:
                raise ValueError
            elif len(date_split[0]) != 2 or int(date_split[0]) > 12:
                raise ValueError("Month must be 2 digits between 01-12.")
            elif len(date_split[1]) != 2 or int(date_split[1]) > 31:
                raise ValueError("Date must be two digits between 01-31.")
            elif len(date_split[2]) != 4:
                raise ValueError("Must provide a four-digit year.")
            
            month = d.date(int(date_split[2]), int(date_split[0]), int(date_split[1])).strftime('%B')
            print(f"{month} {date_split[1]}, {date_split[2]}")
            return
            
        except ValueError as e:
            print(f"Error: {e}\n")
        
        
if __name__ == "__main__":
    main()