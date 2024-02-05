from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv(r"C:\Users\angel\Desktop\100 days of code\flashcards\data\words_to_learn")
    flash_dict = df.to_dict(orient='records')

except FileNotFoundError:
    df = pd.read_csv(r"data/french_words.csv")
    flash_dict = df.to_dict(orient='records')
window = Tk()
current_card = {}


def english_word(choice):
    canvas.itemconfig(image_item, image= card_back)
    canvas.itemconfig(language, text="English", fill="white")
    english = choice.get('English')
    canvas.itemconfig(word, text=english, fill="white")


def french_word():
    global current_card
    current_card = random.choice(flash_dict)
    french = current_card.get('French')
    canvas.itemconfig(image_item, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=french,fill="black")
    window.after(3000, lambda: english_word(current_card))


def known_word():
    flash_dict.remove(current_card)
    data = pd.DataFrame(flash_dict)
    data.to_csv("data/words_to_learn", index=FALSE)
    french_word()


#-----------------------UI SETUP-----------------------

window.config(width=850, height=576, background=BACKGROUND_COLOR, padx=50, pady=50)
card_front = PhotoImage(file=r"images/card_front.png")
card_back = PhotoImage(file=r"images/card_back.png")
canvas = Canvas(width=card_front.width(), height=card_front.height(), background=BACKGROUND_COLOR, highlightthickness=0)
image_item = canvas.create_image(0, 0, anchor="nw", image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

right_button = PhotoImage(file=r"images/right.png")
wrong_button = PhotoImage(file =r"images/wrong.png")
right = Button(image=right_button, highlightthickness=0, background=BACKGROUND_COLOR, height=50, width=50,
               command=known_word)
wrong = Button(image=wrong_button, highlightthickness=0, background=BACKGROUND_COLOR, height=50, width=50,
               command=french_word)
right.grid(column=1, row=1)
wrong.grid(column=0, row=1)
french_word()
window.mainloop()
