from tkinter import *

window = Tk()       #Inicjuje powstanie okienka
window.geometry('800x300')          #Ustala rozmiar okienka
window.title("Welcome to your worst dream")      #Nadanie nazwy okienka

lbl1 = Label(window, text = "Hello, sweetie." + "\n" + "Choose your favourite folders.", font = ("Times New Roman", 30))
lbl1.grid(column = 0, row = 0)

def clicked():
    res = "Button was clicked!" + txt.get()
    lbl1.configure(text = res)

def clicked1(label):
    label.set(True)

chk1_state = BooleanVar()
chk1_state.set(False)
chk1 = Checkbutton(window, text = 'Pictures', var = chk1_state, command=clicked1(chk1_state))
chk1.grid(column = 0, row = 1)

chk2_state = BooleanVar()
chk2_state.set(False)
chk2 = Checkbutton(window, text = 'Videos', var = chk2_state, command=clicked1(chk2_state))
chk1.grid(column = 0, row = 2)

chk3_state = BooleanVar()
chk3_state.set(False)
chk3 = Checkbutton(window, text = 'Music', var = chk3_state, command=clicked1(chk3_state))
chk3.grid(column = 0, row = 3)

chk4_state = BooleanVar()
chk4_state.set(False)
chk4 = Checkbutton(window, text = 'Exe files', var = chk4_state, command=clicked1(chk4_state))
chk4.grid(column = 0, row = 4)



chk5_state = BooleanVar()
chk5_state.set(False)
chk5 = Checkbutton(window, text = 'Folders', var = chk5_state, command=clicked1(chk5_state))
chk5.grid(column = 0, row = 5)


btn1 = Button(window, text = "Touch me to start", bg = "black", fg = "white", command = clicked)   #Tu tworze przycisk rozpoczynajacy dzialanie programu.
btn1.grid(column = 2, row = 5)

window.mainloop()    #Dzieki temu pokazuje sie okno

