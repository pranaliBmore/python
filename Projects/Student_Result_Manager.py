student = {}

while True:
    print("\n*****STUDENT RESULT MANAGEMENT SYSTEM*****")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    #Add Student
    if choice == "1":
        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))
        student[id] = {"name" : name, "marks" : marks}
        print(f"{name} Successfully Added!")

    #view Student
    elif choice =="2":
        if not student:
            print("No Student Found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    #check Result
    elif choice =="3":
        id = int(input("Enter Student ID: "))
        if id in student:
            marks = student[id]["marks"]
            if marks >= 40:
                print(f"{student[id]['name']} : PASS")
            else:
                print(f"{student[id]['name']} : FAIL")
        else:
            print("Student Not Found!")

    #Update Student
    elif choice == "4":
        id = int(input("Enter Student ID: "))
        if id in student:
            name = input("Enter New Student Name: ")
            marks = int(input("Enter new marks: "))
            student[id] = {"name" : name, "marks" : marks}
            print(f"{name} Successfully Updated!")

    #Delete Student
    elif choice == "5":
        id = int(input("Enter student ID: "))
        if id in student:
            del student[id]
            print("Student Successfully Deleted!")
        else:
            print("Student Not Found!")

    #Exit
    elif choice == "6":
        print("Exiting the Program...")
        break
    else:
        print("Invalid Choice! Please Try Again.")


        
              