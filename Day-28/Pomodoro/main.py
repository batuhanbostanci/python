from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marker.config(text="")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", font=(FONT_NAME, 30), bg=YELLOW, fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", font=(FONT_NAME, 30), bg=YELLOW, fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 30), bg=YELLOW, fg=RED)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marker.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)

timer_text = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)


start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marker = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_marker.grid(column=1, row=3)

window.mainloop()