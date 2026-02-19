import os
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    
    def add_entry(self):
        entry = input("Enter your journal entry:\n")

        try:
            with open(self.filename, "a") as file:   # append mode
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"\n[{time}]\n")
                file.write(entry + "\n")

            print("Entry added successfully!\n")

        except Exception as e:
            print("Error while writing to file:", e)

    
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:   # read mode
                content = file.read()

                if content.strip() == "":
                    print("No journal entries found.\n")
                else:
                    print("\nYour Journal Entries:")
                    print("---------------------------------")
                    print(content)

        except FileNotFoundError:
            print("Journal file does not exist. Please add an entry first.\n")

    
    def search_entry(self):
        keyword = input("Enter keyword to search: ")

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

                found = False
                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("No matching entries found.\n")

        except FileNotFoundError:
            print("Journal file does not exist.\n")

   
    def delete_entries(self):
        if os.path.exists(self.filename):
            choice = input("Are you sure you want to delete all entries? (yes/no): ")

            if choice.lower() == "yes":
                os.remove(self.filename)
                print("All entries deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
        else:
            print("No journal file found to delete.\n")




def main():
    journal = JournalManager()

    while True:
        print("===== Personal Journal Manager =====")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entry()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print("Thank you for using Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1-5.\n")

main()

