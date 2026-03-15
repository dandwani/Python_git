import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_plot = None
        print("Sales Data Analyzer Started")

    def __del__(self):
        print("Program Closed")

    
    def load_dataset(self):
        file = input("Enter CSV file path: ")
        try:
            self.data = pd.read_csv(file)
            print("Dataset loaded successfully")
        except:
            print("Error loading file")

    def explore_data(self):

        if self.data is None:
            print("Load dataset first")
            return

        print("\n1. Display first 5 rows")
        print("2. Display last 5 rows")
        print("3. Display columns")
        print("4. Display dataset info")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(self.data.head())

        elif choice == 2:
            print(self.data.tail())

        elif choice == 3:
            print(self.data.columns)

        elif choice == 4:
            print(self.data.info())

    
    def dataframe_operations(self):

        if self.data is None:
            print("Load dataset first")
            return

        print("\n1 Sort by column")
        print("2 Filter rows")

        choice = int(input("Enter choice: "))

        if choice == 1:
            col = input("Enter column name: ")
            print(self.data.sort_values(by=col))

        elif choice == 2:
            col = input("Enter column name: ")
            val = input("Enter value: ")
            print(self.data[self.data[col] == val])

    
    def handle_missing(self):

        if self.data is None:
            print("Load dataset first")
            return

        print("\n1 Show missing values")
        print("2 Fill missing values")
        print("3 Drop missing values")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(self.data.isnull().sum())

        elif choice == 2:
            self.data.fillna(0, inplace=True)
            print("Missing values filled")

        elif choice == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values removed")


    def descriptive_statistics(self):

        if self.data is None:
            print("Load dataset first")
            return

        print(self.data.describe())


    def visualize_data(self):

        if self.data is None:
            print("Load dataset first")
            return

        print("\n1 Bar Plot")
        print("2 Line Plot")
        print("3 Scatter Plot")
        print("4 Histogram")

        choice = int(input("Enter choice: "))

        if choice == 1:
            x = input("Enter X column: ")
            y = input("Enter Y column: ")

            plt.bar(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Bar Plot")

            self.last_plot = plt
            plt.show()

        elif choice == 2:
            x = input("Enter X column: ")
            y = input("Enter Y column: ")

            plt.plot(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Line Plot")

            self.last_plot = plt
            plt.show()

        elif choice == 3:
            x = input("Enter X column: ")
            y = input("Enter Y column: ")

            plt.scatter(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Scatter Plot")

            self.last_plot = plt
            plt.show()

        elif choice == 4:
            col = input("Enter column name: ")

            plt.hist(self.data[col])
            plt.title("Histogram")

            self.last_plot = plt
            plt.show()

    def save_visualization(self):

        if self.last_plot is None:
            print("No plot to save")
            return

        name = input("Enter file name (example: chart.png): ")
        self.last_plot.savefig(name)
        print("Visualization saved successfully")


def main():

    analyzer = SalesDataAnalyzer()

    while True:

        print("\n===== Data Analyzer Menu =====")
        print("1 Load Dataset")
        print("2 Explore Data")
        print("3 DataFrame Operations")
        print("4 Handle Missing Data")
        print("5 Generate Statistics")
        print("6 Data Visualization")
        print("7 Save Visualization")
        print("8 Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            analyzer.load_dataset()

        elif choice == 2:
            analyzer.explore_data()

        elif choice == 3:
            analyzer.dataframe_operations()

        elif choice == 4:
            analyzer.handle_missing()

        elif choice == 5:
            analyzer.descriptive_statistics()

        elif choice == 6:
            analyzer.visualize_data()

        elif choice == 7:
            analyzer.save_visualization()

        elif choice == 8:
            print("Exiting program")
            break

        else:
            print("Invalid choice")


main()