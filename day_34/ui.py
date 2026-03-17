from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"
FONT_NAME = "Arial"

class QuizInterface:
    def answer(self, ans: str):
        score = self.quiz.check_answer(ans)[0]
        self.score_label.config(text=score)

        if self.quiz.check_answer(ans)[1]:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, self.get_next_question)

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzapp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.score_label = Label(text="Score: 0/0", font=(FONT_NAME, 10, "bold"), bg=THEME_COLOR, fg=WHITE)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="eiuofhe wifioaej foaf fqewifjqwif jfiqio",
            fill=BLACK,
            width=280,
            font=(FONT_NAME, 18, "italic")
        )

        self.true_button = Button(image=true_img, bg=THEME_COLOR, command=lambda: self.answer("true"))
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, bg=THEME_COLOR, command=lambda: self.answer("false"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            q_text = f"Your final score was: {self.quiz.score}/10"
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

