import time
from tkinter import  *
YELLOW = "#f7f5dd"
win=Tk()
win.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=300,height=300,bg=YELLOW,highlightthickness=0)
canvas.create_text(100,100,text='x')
x=0
while x>10:
    canvas.delete()
    canvas.create_text(100,100,text=f'{x}',fill='white',font=('Courier',30))
    x-=1
canvas.grid(row=1,column=2)
win.mainloop()