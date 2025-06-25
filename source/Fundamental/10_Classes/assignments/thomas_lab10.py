"""
Christian Thomas
Complete

This file uses the employee module to enter and return employee information.
"""

from employee import Employee

def main():
    employees = []

    while True:
        ans = input("Would you like to add an employee? (y/n): ")
        print()
        if ans.lower() == "n":
            break
        else:
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            department = input("Enter department: ")
            job_title = input("Enter job title: ")

            employees.append(Employee(name, employee_id, department, job_title))
        
    count = 0
    for employee in employees:
        count += 1
        print(f"Employee {count}:")
        print(employee)


if __name__ == "__main__":
    main()