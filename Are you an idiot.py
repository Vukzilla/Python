from tkinter import *
import random

app = Tk()

def on_closing():
    # Do nothing to ignore the close button event
    pass

def no():
    app1 = Tk()    
    app1.title("Idiot")
    app1.geometry("300x130")
    app1.resizable(False,False)

    text = Label(app1, text="Are you an idiot?")
    text.place(x=100, y=10)  

    x1 = random.randint(0, screen_width - 400)
    y1 = random.randint(0, screen_height - 300)

    app1.geometry("+{}+{}".format(x1, y1))

    nobutton = Button(app1,text = "No",width=8, command=no)
    nobutton.place(x=215, y = 80)

    yesbutton = Button(app1,text = "Yes",width=8, command=app.quit)
    yesbutton.place(x=20, y=80)

    app1.attributes('-toolwindow', True)

    app1.protocol("WM_DELETE_WINDOW", on_closing)
    

app.title("Idiot")
app.geometry("300x130")
app.configure(bg='white')
app.resizable(False,False)

text = Label(app, text="Are you an idiot?")
text.place(x=100, y=10)

nobutton = Button(text = "No",width=8, command=no)
nobutton.place(x=215, y = 80)

yesbutton = Button(text = "Yes",width=8, command=app.quit)
yesbutton.place(x=20, y=80)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x1 = random.randint(0, screen_width - 400)
y1 = random.randint(0, screen_height - 300)

app.attributes('-toolwindow', True)

app.geometry("+{}+{}".format(x1, y1))

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
