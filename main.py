from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

word_dictionary = {}
current_word = {}

try:
  data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
  data = pandas.read_csv("./data/french_words.csv")
finally:
  word_dictionary = data.to_dict(orient="records")

def next_card():
  global current_word, flip_delay
  
  window.after_cancel(flip_delay)

  current_word = random.choice(word_dictionary)
  canvas.itemconfig(card_background, image=card_front_image)
  canvas.itemconfig(card_title, text="French", fill="black")
  canvas.itemconfig(card_word, text=current_word["French"], fill="black")

  flip_delay = window.after(3000, func=flip_card)

def flip_card():
  canvas.itemconfig(card_background, image=card_back_image)
  canvas.itemconfig(card_title, text="English", fill="white")
  canvas.itemconfig(card_word, text=current_word["English"], fill="white")

def remove_card():
  word_dictionary.remove(current_word)

  data = pandas.DataFrame(word_dictionary)
  data.to_csv("./data/words_to_learn.csv", index=False)
  next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("French Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_delay = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

button_right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_image, highlightthickness=0, command=remove_card)
button_right.grid(row=1, column=1)

next_card()

window.mainloop()