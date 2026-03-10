import numpy as np

class NumpyAnalyzer:

    def __init__(self):
        self.arr = None


    def create_array(self):
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        
        self.arr = np.array(elements).reshape(rows, cols)
        print("Array created:")
        print(self.arr)

   
    def math_operation(self):
        print("1. Addition")
        print("2. Subtraction")
        choice = int(input("Enter choice: "))

        elements = list(map(int, input("Enter same size elements: ").split()))
        arr2 = np.array(elements).reshape(self.arr.shape)

        if choice == 1:
            result = self.arr + arr2
            print("Result of Addition:")
        else:
            result = self.arr - arr2
            print("Result of Subtraction:")

        print(result)

   
    def slice_array(self):
        r1 = int(input("Start row: "))
        r2 = int(input("End row: "))
        c1 = int(input("Start column: "))
        c2 = int(input("End column: "))

        sliced = self.arr[r1:r2, c1:c2]
        print("Sliced Array:")
        print(sliced)

   
    def sort_array(self):
        sorted_arr = np.sort(self.arr, axis=None)
        print("Sorted Array:")
        print(sorted_arr)

    def statistics(self):
        print("Sum:", np.sum(self.arr))
        print("Mean:", np.mean(self.arr))
        print("Median:", np.median(self.arr))
        print("Standard Deviation:", np.std(self.arr))
        print("Variance:", np.var(self.arr))


def main():

    obj = NumpyAnalyzer()

    while True:
        print("\n--- NumPy Analyzer ---")
        print("1. Create Array")
        print("2. Mathematical Operations")
        print("3. Slice Array")
        print("4. Sort Array")
        print("5. Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.create_array()
        elif choice == 2:
            obj.math_operation()
        elif choice == 3:
            obj.slice_array()
        elif choice == 4:
            obj.sort_array()
        elif choice == 5:
            obj.statistics()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main()