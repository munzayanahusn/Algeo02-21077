from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk

window=Tk()

width_of_window = 427
height_of_window = 250
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
window.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

window.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(window,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

# Progress Bar
def new_win():
    import face_recognition

def bar():
    l4=Label(window,text='Loading...',fg='white',bg=a)
    setting4=('Calibri (Body)',10)
    l4.config(font=setting4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        window.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    window.destroy()
    new_win()
        
progress.place(x=-10,y=235)

a='#249794'
Frame(window,width=427,height=241,bg=a).place(x=0,y=0)
b1=Button(window,width=10,height=1,text='Mulai',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)

######## Label

# image = PhotoImage(file="D:\Vs Code\GUI PYTHON\Tubes\logo.png")
# l0=Label(window, image=image, padx=10, pady=10)
# l0.place(x=30,y=200)

l1=Label(window,text='TUBES IF2123',fg='white',bg=a)
l1.config(font=('Calibri (Body)',18,'bold'))
l1.place(x=50,y=60)

l2=Label(window,text='Kelompok YGY',fg='white',bg=a)
l2.config(font=('Calibri (Body)',13))
l2.place(x=50,y=90)

l3=Label(window,text='FACE RECOGNITION',fg='white',bg=a)
l3.config(font=('Calibri (Body)',13))
l3.place(x=50,y=110)

window.mainloop()