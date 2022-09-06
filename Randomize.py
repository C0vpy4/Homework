import random
from tkinter import *

even_numbers=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

count_clicks = 0

def randomaize():
    global slovar
    global count_clicks
    global nothing
    
    nothing = 2000

    count_clicks+=1
   
    slovar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    number_one = random.choice(slovar)
    number_two = random.choice(slovar)
    gg_chel_first.configure(text=number_one)
    gg_chel_second.configure(text=number_two)
    
    while nothing>0:
        nothing-=1
        btn.configure(text="....", background="red", state=DISABLED)
        window.update()
        if nothing == 0 :
            btn.configure(text="Retry?",state=ACTIVE, bg="green")
    #if count_clicks not in even_numbers:
        #btn.configure(text="Retry?", background="red")
    #else:
       # pass



window = Tk()
window.title("Randomizer")
window.geometry("450x285")
window.resizable(width=0, height=0)
window["bg"] = "gray22"

#----------------BUTTONS---------------------------------------------
btn = Button(window, text="START", font="Verdana",bg="green", command=randomaize)
btn.place(relx=0.5, rely=0.6,anchor=CENTER)

#---------------LABELS---------------------------------------------------------------
text_one = Label(window, text='First:', bg="gray22",font="Elephant",fg='green')
text_one.place(relx=0.2, rely=0.1,anchor=CENTER)

text_two =Label(window, text='Second:', bg="gray22",font="Elephant",fg='green')
text_two.place(relx=0.8, rely=0.1,anchor=CENTER)

gg_chel_first = Label(window, text='0', bg="gray22",font="Ethnocentric",fg='#d00000')
gg_chel_first.place(relx=0.2, rely=0.3,anchor=CENTER)

gg_chel_second = Label(window, text='0', bg="gray22",font="Ethnocentric",fg='#d00000')
gg_chel_second.place(relx=0.8, rely=0.3,anchor=CENTER)

window.mainloop()
