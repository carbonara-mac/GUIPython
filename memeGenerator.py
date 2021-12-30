from guizero import App, TextBox, Drawing, Combo, Slider

def draw_meme():
    meme.clear()
    meme.image(0,0, image.value)
    meme.text(150,20, top_text.value,
    color= color.value,
    size=size.value,
    font=font.value)
    meme.text(150,720, bottom_text.value,
    color= color.value,
    size=size.value,
    font=font.value)

app = App("meme")

top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command= draw_meme)
color= Combo(app,
     options=[ "red", "green", "blue", "purple", "pink", "white", "black"], 
     command=draw_meme, selected= "blue")
font= Combo(app,
     options=[ "impact", "verdana", "courier"], 
     command=draw_meme, selected= "impact")
size= Slider(app, start=20, end=100, command=draw_meme)
meme = Drawing(app, width="fill", height="fill" )
image = TextBox(app, "garf.png", command=draw_meme)

draw_meme()
app.display()