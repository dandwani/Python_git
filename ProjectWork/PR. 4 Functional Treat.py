
data = []  

def input_data():
    """Function to take 1D list input from user"""
    global data
    numbers = input("Enter numbers separated by space: ")
    data = list(map(int, numbers.split()))
    print("Data stored successfully!")

def show_summary():
    """Display basic statistics using built-in functions"""
    if len(data) == 0:
        print("No data available!")
        return

    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum:", sum(data))
    print("Average:", sum(data) / len(data))


def find_duplicates():
    """Find duplicate values"""
    duplicates = []

    for num in data:
        if data.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    if duplicates:
        print("Duplicate values:", duplicates)
    else:
        print("No duplicates found!")

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def filter_data():
    """Filter numbers greater than threshold using lambda"""
    threshold = int(input("Enter threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, data))
    print("Filtered data:", filtered)

def sort_data():
    """Sort data ascending or descending"""
    choice = input("Enter 1 for Ascending, 2 for Descending: ")

    if choice == "1":
        print("Sorted data:", sorted(data))
    elif choice == "2":
        print("Sorted data:", sorted(data, reverse=True))
    else:
        print("Invalid choice!")

def statistics():
    """Return min, max and average"""
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)
    return minimum, maximum, average

def show_values(*args):
    """Display multiple values using *args"""
    print("Values received:")
    for value in args:
        print(value)

def show_summary_dict(**kwargs):
    """Display key-value pairs using **kwargs"""
    print("Summary:")
    for key, value in kwargs.items():
        print(key, ":", value)

while True:
    print("\n===== MENU =====")
    print("1. Input Data")
    print("2. Show Summary (Built-in)")
    print("3. Find Duplicates")
    print("4. Calculate Factorial")
    print("5. Filter Data (Lambda)")
    print("6. Sort Data")
    print("7. Show Statistics (Return Multiple Values)")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        show_summary()

    elif choice == "3":
        find_duplicates()

    elif choice == "4":
        num = int(input("Enter number: "))
        print("Factorial:", factorial(num))

    elif choice == "5":
        filter_data()

    elif choice == "6":
        sort_data()

    elif choice == "7":
        if len(data) == 0:
            print("No data available!")
        else:
            mn, mx, avg = statistics()
            show_summary_dict(Minimum=mn, Maximum=mx, Average=avg)

    elif choice == "8":
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice!")
        