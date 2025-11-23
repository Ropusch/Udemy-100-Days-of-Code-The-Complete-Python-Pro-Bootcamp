from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

times = {
    "work": WORK_MIN,
    "break": SHORT_BREAK_MIN,
    "long break": LONG_BREAK_MIN
}
pomodoro_plan = ["work", "break", "work", "break", "work", "break", "work", "long break"]
plan = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
POMODORO_ON = False
def start_pomodoro():
    global POMODORO_ON
    if POMODORO_ON:
        return
    global plan
    POMODORO_ON = True
    plan = 0
    start_timer()

def start_timer():
    window.attributes("-topmost", 1)
    window.attributes("-topmost", 0)
    global plan, POMODORO_ON
    if plan > len(pomodoro_plan)-1:
        label.config(text="END")
        POMODORO_ON = False
        check_label.config(text="")
        plan = 0
        return
    label.config(text=pomodoro_plan[plan])
    count_down(1 * times[pomodoro_plan[plan]])
    plan += 1


def restart_pomodoro():
    global POMODORO_ON, plan
    label.config(text="TIMER")
    POMODORO_ON = False
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    plan = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if not POMODORO_ON:
        return
    mins = count // 60
    secs = count % 60
    canvas.itemconfig(timer_text, text=f"{mins:02}:{secs:02}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        if pomodoro_plan[plan-1] == "work":
            check_label.config(text=check_label["text"]+"✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="TIMER", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)
check_label = Label(text="", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=2, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), bg=GREEN, fg=RED, command=start_pomodoro)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), bg=GREEN, fg=RED, command=restart_pomodoro)
reset_button.grid(row=2, column=2)

window.mainloop()