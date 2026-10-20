student = {}

while True:
    print("\n*****STUDENT RESULT MANAGEMENT SYSTEM*****")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add Student
    if choice == "1":
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))
        student[name] = marks
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
        name = input("Enter Student Name: ")
        if name in student:
            marks = student[name]
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student Not Found!")

    #Exit
    elif choice == "4":
        print("Exiting the Program...")
        break
    else:
        print("Invalid Choice! Please Try Again.")


        
              