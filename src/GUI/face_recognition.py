from tkinter import *
from tkinter import Canvas, filedialog, messagebox, ttk

# Init
window = Tk()
window.configure(bg='#BAD1C2')
window.title("TUBES ALGEO 2 YGY")
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

my_menu = Menu(window)
window.config(menu=my_menu)

# click command
def our_command():
    pass

# rounded button

# Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Page", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Create a edit item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=our_command)
edit_menu.add_command(label="Redo", command=our_command)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)

# Create a edit item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

message = Label(window, text="Face Recognition", bg="#4FA095", fg="white", width=50, height=3, font=('times', 30, 'bold'))
message.place(x = 170, y=20)

message1 = Label(window, text="Insert Your Dataset", bg="#BAD1C2", fg="#153462", font=('Helvetica', 20, 'bold'))
message1.place(x = 50, y=240)

myButton1 = Button(window, text="Choose A Folder!", fg="#153462", bg="#5CDB95", padx=35, pady=15,)
myButton1.place(x = 85, y=300)

message2 = Label(window, text="Insert Your Image", bg="#BAD1C2", fg="#153462", font=('Helvetica', 20, 'bold'))
message2.place(x = 50, y=390)

myButton2 = Button(window, text="Choose An Image!", fg="#153462", bg="#5CDB95", padx=35, pady=15,)
myButton2.place(x = 75, y=450)

message3 = Label(window, text="Result", bg="#BAD1C2", fg="#153462", font=('Microsoft Yahei UI Light', 23, 'bold'))
message3.place(x = 50, y=550)

message4 = Label(window, text="Test Image", bg="#BAD1C2", fg="#153462", font=('Helvetica', 20, 'normal'))
message4.place(x = 550, y=220)

message5 = Label(window, text="Closest Result", bg="#BAD1C2", fg="#153462", font=('Helvetica', 20, 'normal'))
message5.place(x = 1050, y=220)

message6 = Label(window, text="Execution time", bg="#BAD1C2", fg="#153462", font=('Helvetica', 15, 'normal'))
message6.place(x = 550, y=670)

# Menjalankan GUI
window.mainloop()
