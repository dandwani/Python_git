
import datetime
import math
import random
import uuid


def show_current_time():
    now = datetime.datetime.now()
    print("Current Date and Time:", now)


def date_difference():
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")

    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

    difference = abs((d2 - d1).days)
    print("Difference:", difference, "days")


def factorial():
    num = int(input("Enter a number: "))
    print("Factorial:", math.factorial(num))


def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate (%): "))
    t = float(input("Enter time (years): "))

    amount = p * (1 + r/100) ** t
    print("Total Amount:", round(amount, 2))


def random_number():
    print("Random Number:", random.randint(1, 100))


def random_password():
    length = int(input("Enter password length: "))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def generate_uuid():
    print("Generated UUID:", uuid.uuid4())



def write_file():
    filename = input("Enter file name: ")
    data = input("Enter text to write: ")

    with open(filename, "w") as file:
        file.write(data)

    print("Data written successfully!")


def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("File Content:")
            print(file.read())
    except:
        print("File not found!")



def explore_module():
    name = input("Enter module name (math, random, datetime): ")

    if name == "math":
        print(dir(math))
    elif name == "random":
        print(dir(random))
    elif name == "datetime":
        print(dir(datetime))
    else:
        print("Module not supported")



def main():
    while True:
        print("\n===== Multi-Utility Toolkit =====")
        print("1. Show Current Date & Time")
        print("2. Date Difference")
        print("3. Factorial")
        print("4. Compound Interest")
        print("5. Random Number")
        print("6. Random Password")
        print("7. Generate UUID")
        print("8. Write to File")
        print("9. Read File")
        print("10. Explore Module (dir)")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_current_time()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            factorial()
        elif choice == "4":
            compound_interest()
        elif choice == "5":
            random_number()
        elif choice == "6":
            random_password()
        elif choice == "7":
            generate_uuid()
        elif choice == "8":
            write_file()
        elif choice == "9":
            read_file()
        elif choice == "10":
            explore_module()
        elif choice == "11":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()