import usersDB
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("users_list")

users = [("Pavel", 33, "+380 73 555 13 05")]

columns = ("name", "age", "telephone number")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("telephone number", text="Tel. number")

for user in users:
    tree.insert("", END, values=user)

root.mainloop()
