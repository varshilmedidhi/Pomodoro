import math
from tkinter import  *
import  winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global click
    click=0
    start_btn.config(state='normal')
    canvas.itemconfig(text_time,text=f'{"00"}:{"00"}')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global click
    click+=1
    if click%8==0:
        Timer_label.config(text='Long Break',fg=RED)
        count_down(LONG_BREAK_MIN* 60)
        winsound.PlaySound('ding-47489.wav',winsound.SND_FILENAME)
    elif click%2==0:
        Timer_label.config(text='Break',fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
        winsound.PlaySound('ding-47489.wav',winsound.SND_FILENAME)
    else:
        Timer_label.config(text='Timer',fg=GREEN)
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    seconds=int(count%60)
    minutes=count//60
    start_btn.config(state='disabled')
    nutral=0
    if click==1:
        nutral=click
    elif  click%2!=0:
        nutral=math.ceil(click/2)
    if count%60<10:
        seconds=f"0{seconds}"
    if minutes<10:
        minutes = f"0{minutes}"
    canvas.itemconfig(text_time, text=f'{minutes}:{seconds}')
    if int(count)>0:
        global timer
        timer=window.after(1000, count_down, int(count) - 1)
    elif count==0:
        if click==8:
            start_btn.config(state='normal')
            return 0
        if click%2!=0:
            check_marks = Label(text='✅' *nutral , bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
            check_marks.grid(row=4, column=2)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
WORK = 25
click=0
canvas=Canvas(width=300,height=300,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(140,108,image=tomato_img)
Timer_label=Label(text='Timer',fg=GREEN,width=10,font=(FONT_NAME,30),bg=YELLOW)
Timer_label.grid(row=0,column=2)
text_time=canvas.create_text(140,130,text="00:00",fill='white',font=(FONT_NAME,30))
canvas.grid(row=1,column=2)
start_btn=Button(text='Start',command=start_timer)
start_btn.grid(row=4,column=0)
stop_btn=Button(text="Reset",command=reset_timer)
stop_btn.grid(row=4,column=3)
window.mainloop()

