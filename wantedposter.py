from guizero import App, Text, Picture

app = App(title="Wanted!")
app.bg = "#D6E8D9"
wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.font = "Impact"
cat = Picture(app, image="garf.png")
app.display()
