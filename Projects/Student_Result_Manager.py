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

total_label = tk.Label(
    total_card,
    text = "0",
    font = ("Arial", 24, "bold"),
    bg = "white",
    fg = "#1f3a5f"
)
total_label.pack(pady=(0,10))

#Main Content

content = tk.Frame(root, bg = "#f4f6f9")
content.pack(fill = "both", expand = True, padx = 20, pady = 5)

# left panel : student form
form = tk.LabelFrame(
    content,
    text = "Student Information",
    font = ("Arial", 12, "bold"),
    bg = "white",
    fg = "#1f3a5f",
    padx = 15,
    pady = 15
)
form.pack(side="left", fill = "y", padx(0,15))

tk.Label(
    form, text = "Student ID",
    bg = "white",
    font = ("Arial", 10)
).pack(anchor = "w", pady = (5,2))

id_entry = ttk.Entry(form, width = 28)
id_entry.pack(pady=(0,10))

tk.Label(
    form, text = "Student Name", 
    bg="white", 
    font=("Arial", 10)
).pack(anchor="w", pady=(5, 2))

name_entry = ttk.Entry(form, width=28)
name_entry.pack(pady=(0, 10))

tk.Label(
    form, text = "Marks (0-100)", 
    bg="white", 
    font=("Arial", 10)
).pack(anchor="w", pady=(5, 2))

marks_entry = ttk.Entry(form, width=28)
marks_entry.pack(pady=(0, 15))

# Right panel: Student table
table_frame = tk.LabelFrame(
    content,
    text=" Student Records ",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#1f3a5f",
    padx=10,
    pady=10
)
table_frame.pack(side="left", fill="both", expand=True)

columns = ("id", "name", "marks", "result")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

tree.heading("id", text="Student ID")
tree.heading("name", text="Student Name")
tree.heading("marks", text="Marks")
tree.heading("result", text="Result")

tree.column("id", width=90, anchor="center")
tree.column("name", width=150)
tree.column("marks", width=70, anchor="center")
tree.column("result", width=80, anchor="center")

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tree.tag_configure("pass", foreground="#15803d")
tree.tag_configure("fail", foreground="#dc2626")

