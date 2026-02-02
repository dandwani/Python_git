print("Welcome to Student Data Organizer")

students = []        
subjects_set = set() 

while True:

    print("\nMenu")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show Subjects")
    print("6. Exit")

    choice = input("Enter choice: ")

   
    if choice == "1":
        student_id = int(input("Enter student id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        dob = input("Enter date of birth: ")

        sub = input("Enter subjects (comma separated): ")
        subject_list = sub.split(",")
        subject_set = set()

        for s in subject_list:
            subject_set.add(s.strip())
            subjects_set.add(s.strip())

        id_dob = (student_id, dob)   

        student = {}
        student["id_dob"] = id_dob
        student["name"] = name
        student["age"] = age
        student["grade"] = grade
        student["subjects"] = subject_set

        students.append(student)
        print("Student added")

   
    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                print("--------------------")
                print("ID:", student["id_dob"][0])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("Subjects:", student["subjects"])

    
    elif choice == "3":
        sid = int(input("Enter student id to update: "))
        found = False

        for student in students:
            if student["id_dob"][0] == sid:
                found = True
                print("1. Update age")
                print("2. Update subjects")
                opt = input("Enter option: ")

                if opt == "1":
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated")

                elif opt == "2":
                    new_sub = input("Enter new subjects: ")
                    new_list = new_sub.split(",")
                    new_set = set()

                    for s in new_list:
                        new_set.add(s.strip())
                        subjects_set.add(s.strip())

                    student["subjects"] = new_set
                    print("Subjects updated")

                break

        if found == False:
            print("Student not found")

   
    elif choice == "4":
        sid = int(input("Enter student id to delete: "))
        deleted = False

        for i in range(len(students)):
            if students[i]["id_dob"][0] == sid:
                del students[i]   
                deleted = True
                print("Student deleted")
                break

        if deleted == False:
            print("Student not found")

   
    elif choice == "5":
        print("Subjects offered:")
        for s in subjects_set:
            print(s)

   
    elif choice == "6":
        print("Thank you for using the program")
        break

    else:
        print("Invalid choice")

