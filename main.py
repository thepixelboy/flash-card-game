from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# ---------------------------- CARDS ------------------------------- #
data = pandas.read_csv("./data/french_words.csv")
word_dictionary = data.to_dict(orient="records")

def next_card():
  current_word = random.choice(word_dictionary)
  canvas.itemconfig(card_title, text="French")
  canvas.itemconfig(card_word, text=current_word["French"])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

button_right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_image, highlightthickness=0, command=next_card)
button_right.grid(row=1, column=1)

next_card()

window.mainloop()