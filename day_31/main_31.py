from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- GETTING DATA ------------------------------------ #

try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("french_words.csv")

language_learn = df.columns.values.tolist()[0]
language_known = df.columns.values.tolist()[0]

to_learn = df.to_dict(orient="records")

# ---------------------------- GENERATING FLASHCARDS ------------------------------- #
FINISHED = False
current_card = {}
is_front = True
def next_card(knew: bool):
    if len(to_learn) == 1:
        finished()
        return

    global current_card, is_front
    if knew:
        to_learn.remove(current_card)

        data = pd.DataFrame(to_learn)
        data.to_csv("words_to_learn.csv", index=False)

    current_card = random.choice(to_learn)

    is_front = True

    canvas.itemconfig(language_text, text=language_learn, fill="black")
    canvas.itemconfig(meaning_text, text=current_card[language_learn], fill="black")
    canvas.itemconfig(card_image, image=card_front)

def flip_card():
    if FINISHED:
        return
    global is_front

    if is_front:
        canvas.itemconfig(language_text, text=language_known, fill="white")
        canvas.itemconfig(meaning_text, text=current_card[language_known], fill="white")
        canvas.itemconfig(card_image, image=card_back)
        is_front = False
    else:
        canvas.itemconfig(language_text, text=language_learn, fill="black")
        canvas.itemconfig(meaning_text, text=current_card[language_learn], fill="black")
        canvas.itemconfig(card_image, image=card_front)
        is_front = True


def finished():
    canvas.itemconfig(language_text, text="YOU FINISHED YOUR WORDLIST", fill="black", font=("Ariel", 25, "italic"))
    canvas.itemconfig(meaning_text, text="CONGRATULATION", fill="black", font=("Ariel", 40, "bold"))
    canvas.itemconfig(card_image, image=card_front)
    global FINISHED
    FINISHED = True

# ----------------------------------- UI SETUP ------------------------------------- #
window = Tk()
window.title("Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 526/2, image=card_front)
canvas.grid(row=0, column=0, columnspan=3)

language_text = canvas.create_text(400, 150, text="language", font=("Ariel", 40, "italic"))
meaning_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

r_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=r_button_img, highlightthickness=0, command=lambda: next_card(knew=True))
right_button.grid(row=1, column=0)

f_button_img = PhotoImage(file="images/flip.png")
flip_button = Button(image=f_button_img, highlightthickness=0, command=flip_card)
flip_button.grid(row=1, column=1)

w_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=w_button_img, highlightthickness=0, command=lambda: next_card(knew=False))
wrong_button.grid(row=1, column=2)


next_card(knew=False)

window.mainloop()
