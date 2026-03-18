import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Bookstore:

    
    def __init__(self):
        try:
            self.inventory = pd.read_csv("inventory.csv")
            self.sales = pd.read_csv("sales.csv")
            print("Data Loaded Successfully!")
        except:
           
            self.inventory = pd.DataFrame(columns=["Title", "Author", "Genre", "Price", "Quantity"])
            self.sales = pd.DataFrame(columns=["Date", "Title", "Quantity Sold", "Total Revenue"])
            print("Initialized new dataframes.")

  

    def add_book(self, title, author, genre, price, quantity):
        new_book = pd.DataFrame([{
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": float(price), 
            "Quantity": int(quantity) 
        }])

        self.inventory = pd.concat([self.inventory, new_book], ignore_index=True)
        print("Book added!")

    def update_inventory(self, title, quantity):
        if quantity < 0:
            print("Invalid quantity")
            return

        self.inventory.loc[self.inventory["Title"] == title, "Quantity"] = quantity
        print("Inventory updated!")

    def remove_book(self, title):
        self.inventory = self.inventory[self.inventory["Title"] != title]
        print("Book removed!")

  
    def record_sale(self, title, quantity):
        if quantity <= 0:
            print("Invalid quantity")
            return

        book = self.inventory[self.inventory["Title"] == title]

        if book.empty:
            print("Book not found")
            return

        price = book.iloc[0]["Price"]

        new_sale = pd.DataFrame([{
            "Date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "Title": title,
            "Quantity Sold": quantity,
            "Total Revenue": quantity * price
        }])

        self.sales = pd.concat([self.sales, new_sale], ignore_index=True)

      
        self.inventory.loc[self.inventory["Title"] == title, "Quantity"] -= quantity

        print("Sale recorded!")

    
    def generate_report(self):
        total_revenue = np.sum(self.sales["Total Revenue"])
        avg_price = np.mean(self.inventory["Price"])

        top_books = self.sales.groupby("Title")["Quantity Sold"].sum().sort_values(ascending=False).head(5)

        print("\n--- REPORT ---")
        print("Total Revenue:", total_revenue)
        print("Average Book Price:", avg_price)
        print("\nTop Selling Books:\n", top_books)

   
    def visualize_data(self):
        sns.set_style("whitegrid")

       
        genre_sales = self.inventory.groupby("Genre")["Quantity"].sum()
        genre_sales.plot(kind='bar', title="Books by Genre")
        plt.show()

        
        self.sales["Date"] = pd.to_datetime(self.sales["Date"])
        monthly_sales = self.sales.groupby(self.sales["Date"].dt.month)["Total Revenue"].sum()
        monthly_sales.plot(kind='line', title="Monthly Sales")
        plt.show()

        
        revenue_by_genre = self.inventory.groupby("Genre")["Price"].sum()
        revenue_by_genre.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Revenue Share by Genre")
        plt.show()

       
        pivot = self.inventory.pivot_table(values="Price", index="Genre", columns="Author")
        sns.heatmap(pivot, annot=True)
        plt.title("Heatmap (Price vs Genre & Author)")
        plt.show()
    
    def save_data(self):
       
        self.inventory.to_csv("inventory.csv", index=False)
        self.sales.to_csv("sales.csv", index=False)
        print("Data saved successfully!")



def main():
    store = Bookstore()

    while True:
        print("\n1. Add Book")
        print("2. Update Inventory")
        print("3. Remove Book")
        print("4. Record Sale")
        print("5. Generate Report")
        print("6. Visualize Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            store.add_book(title, author, genre, price, quantity)

        elif choice == "2":
            title = input("Title: ")
            quantity = int(input("New Quantity: "))
            store.update_inventory(title, quantity)

        elif choice == "3":
            title = input("Title: ")
            store.remove_book(title)

        elif choice == "4":
            title = input("Title: ")
            quantity = int(input("Quantity Sold: "))
            store.record_sale(title, quantity)

        elif choice == "5":
            store.generate_report()

        elif choice == "6":
            store.visualize_data()

        elif choice == "7":
            store.save_data()
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
