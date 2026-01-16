from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

def generate_word():
    global new_chosen_word
    canvas.itemconfig(card, image=white_logo)
    new_chosen_word = choice(words)
    new_word_french = new_chosen_word["French"]
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=new_word_french, fill="black")
    window.after(3000, flip_card)

def is_right():
    words.remove(new_chosen_word)
    data_frame = pandas.DataFrame(words)
    data_frame.to_csv("data/words_to_learn.csv", index=False)
    generate_word()

def flip_card():
    canvas.itemconfig(card, image=green_logo)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_chosen_word["English"], fill="white")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words = data.to_dict(orient="records")
new_chosen_word = {}

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
white_logo = PhotoImage(file="images/card_front.png")
green_logo = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=white_logo)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_right)
right_button.grid(row=1, column=1)

generate_word()

window.mainloop()
