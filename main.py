BACKGROUND_COLOR = "#76BA99"
CANVAS_COLOR = "#EDDFB3"
BROWN = "#876445"
LIGHT_BROWN = "#CA955C"
from tkinter import *
import pandas as pd
from random import randint


df = pd.read_csv("C:\\Users\\DELL\\Desktop\\flash-card-project-start\\data\\french_words.csv")
dictdf = df.to_dict(orient="records")
# print(dictdf)
# print(dictdf[randint(0,100)]["French"])
# print(dictdf[1]["French"])

def next_frword():
    global a,flip_timer
    a = randint(0, 102)
    window.after_cancel(flip_timer)
    card_front.itemconfig(title_text,text="French",fill="black")
    card_front.itemconfig(word_text,text=dictdf[a]["French"],fill="black")
    card_front.itemconfig(card_front_img,image=frontcard_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    # window.after(3000)
    card_front.itemconfig(card_front_img,image=backcard_img)
    card_front.itemconfig(title_text,text="English",fill="white")
    card_front.itemconfig(word_text,text=dictdf[a]["English"],fill="white")


window = Tk()

window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.geometry("900x900")
window.title("FlashyApp")

flip_timer = window.after(3000,func=flip_card)

frontcard_img = PhotoImage(file="C:\\Users\\DELL\\Desktop\\flash-card-project-start\\images\\card_front.png")
backcard_img = PhotoImage(file="C:\\Users\\DELL\\Desktop\\flash-card-project-start\\images\\card_back.png")
card_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = card_front.create_image(400, 263, image=frontcard_img)
title_text = card_front.create_text(400, 145, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = card_front.create_text(400, 263, text="Word", fill="black", font=("Ariel", 40, "bold"))
right_img = PhotoImage(file="C:\\Users\\DELL\\Desktop\\flash-card-project-start\\images\\right.png")
wrong_img = PhotoImage(file="C:\\Users\\DELL\\Desktop\\flash-card-project-start\\images\\wrong.png")
wrong = Button(image=wrong_img,highlightthickness=0,command=next_frword)
right = Button(image=right_img,highlightthickness=0,command=next_frword)

card_front.grid(row=0, columnspan=2)
wrong.grid(row=1,column=0)
right.grid(row=1,column=1)
window.mainloop()
