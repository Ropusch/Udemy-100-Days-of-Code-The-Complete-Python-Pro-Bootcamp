from tkinter import *
import requests


url = "https://api.api-ninjas.com/v2/randomquotes?categories=success,wisdom"
headers = {"X-Api-Key": "EBm01iLlpEjoU63yN2eNs61EPMr1eQqPHp2gQLm1"}
#api from: https://api-ninjas.com/api/quotes


def get_quote():
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    data = response.json()[0]
    res = f"{data['quote']}\n ~{data['author']}"

    if len(res) > 70:
        canvas.itemconfig(quote_text, text=res, font=("Ariel", 18, "bold"))
    elif len(res) > 150:
        canvas.itemconfig(quote_text, text=res, font=("Ariel", 8, "bold"))
    else:
        canvas.itemconfig(quote_text, text=res, font=("Arial", 30, "bold"))



window = Tk()
window.title("Quote machine")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="quote_button.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()