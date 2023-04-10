from tkinter import *

def submit():
    app1 = Tk()
    app1.title("Weight of your mom?")
    app1.geometry("200x50")

    label1 = Label(app1, text=("Damn, your mama fat boii"))
    label1.pack()
    app1.eval('tk::PlaceWindow . center')

app = Tk()
app.title("Weight of your mom?")
app.geometry("200x100")

label = Label(app, text=("put in your username"))
label.pack()

submit = Button(app, text="ok", command=submit)
submit.pack(side = BOTTOM)

app.eval('tk::PlaceWindow . center')


entry = Entry()
entry.config(font=(50))
entry.config(width=10)
entry.pack()
app.mainloop()
