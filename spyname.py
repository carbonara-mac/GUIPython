# Imports -----------------------------
from guizero import App, Text, PushButton
from random import choice
# Functions ---------------------------
def choose_name():
    print("Button was pressed")
    first_names = ["Jovani", "Desiree", "Joe", "Roberto", "Elvio", "Chu"]
    last_names = ["Vazquez", "Janice", "Mama", "Clemente", "Lao", "Ramirez"]
    spy_name = choice(first_names) + " " + choice(last_names)
    name.value = spy_name
    #print(spy_name)
# App----------------------------------
app = App(title="Top Secret!")
# Widgets------------------------------
title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text = "Tell me!")
button.bg = "red"
button.text_size=30
name = Text(app, text="")
# Display -----------------------------
app.display()