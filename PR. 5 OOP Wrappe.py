
class Employee:

    def __init__(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.__emp_id = emp_id     
        self.__salary = salary     
        print("Employee created successfully!")

    
    def get_salary(self):
        return self.__salary

    
    def set_salary(self, new_salary):
        self.__salary = new_salary

    
    def get_emp_id(self):
        return self.__emp_id

    
    def set_emp_id(self, new_id):
        self.__emp_id = new_id

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)

    def __del__(self):
        print("Employee object deleted.")


class Manager(Employee):

    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

class Developer(Employee):

    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)

emp = None

while True:
    print("\n==== Employee Management System ====")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Check Subclass")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        emp = Employee(name, age, emp_id, salary)

    elif choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        emp = Manager(name, age, emp_id, salary, dept)

    elif choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        lang = input("Enter Programming Language: ")
        emp = Developer(name, age, emp_id, salary, lang)

    elif choice == "4":
        if emp:
            emp.display()
        else:
            print("No employee created yet!")

    elif choice == "5":
        print("Is Manager subclass of Employee?",
              issubclass(Manager, Employee))
        print("Is Developer subclass of Employee?",
              issubclass(Developer, Employee))

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
