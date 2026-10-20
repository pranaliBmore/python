import tkinter as tk
from tkinter import ttk

#main window

root = tk.Tk()
root.title("Student Result Management System")
root.geometry("800x500")
root.configure(bg="#f4f6f9")
root.minsize(800,500)

#student dictionary for storing student Info
student = {}

#styles
style = ttk.Style()
style.theme_use("clam")

style.configuration(
    "Treeview",
    rowheight = 30,
    font = ("Arial", 12)
)

style.configure(
    "Treeview.Heading",
    font = ("Arial", 10, "bold"),
    bg = "#dce6f1"
)

style.configure(
    "TButton",
    font = ("Arial", 10),
    padding = 7
)

#header

header = tk.Frame(root, bg = "#1f3a5f", height = 110)
header.pack(fill = "x")

tk.Label(
    header,
    text = "Student Result Management System",
    font = ("Arial", 22, "bold"),
    bg = "#1f3a5f",
    fg = "white"
).pack(pady=(20, 5))

tk.Label(
    header,
    text = "Manage student records and academic result",
    font = ("Arial", 12),
    bg="#1f3a5f",
    fg="#dce6f1"
).pack()

#dashboard

dashboard = tk.Frame(root, bg = "#f4f6f9")
dashboard.pack(fill = "x", padx = 20, pady = 15)

total_card = tk.Frame(
    dashboard,
    bg = "white",
    highlightbackground = "#dce6f1", 
    highlightthickness = 1
)
total_card.pack(fill = "x")

tk.Label(
    total_card,
    text = "TOTAL STUDENTS",
    font = ("Arial", 10, "bold"),
    bg = "white",
    fg = "#64748b"
).pack(pady=(10,0))



while True:
    #print("\n*****STUDENT RESULT MANAGEMENT SYSTEM*****")
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


        
              