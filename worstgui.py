#Imports-----------------------------------
from guizero import App, Text, Combo, Slider, PushButton, Window
from string import ascii_letters
from time import ctime
#Functions---------------------------------
def flash_text():
    if title.visible:
        title.hide()
    else:
        title.show()
def update_date():
    the_date.value = ctime(date_slider.value)
def are_you_sure():
    if app.yesno("question", "is cereal a soup"):
        app.error("no", "you're wrong")
    else:
        app.info("cool", "smart")
#App---------------------------------------
app = App("it's all wrong", bg = "dark green")
window = Window(app, "Some window lol")
window.show()
windowtext= Text(window, text= "BRUH", size= 190)
app.info("Bruh", "Your mom")
app.warn("Pitbull says: ", "We at the hotel, motel, holiday inn")
app.error("Ew", "Leave")
title =Text(app, text = "Some hard to read text", size= "14",
font = "Comic Sans", color = "yellow")
app.repeat(1000, flash_text)
name_letters =[]
title1 = Text(app, text = "write something hehe", align = "left")
for count in range(10):
    a_letter = Combo(app, options= " "+ ascii_letters, align="left")
    name_letters.append(a_letter)

title2 = Text(app, text = "Enter time lol", align = "left")
the_date = Text(app)
date_slider = Slider(app, start=0, end=9999999999, command=update_date, align ="left")
Question = PushButton(app, command=are_you_sure)
app.display()
