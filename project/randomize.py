import random
from tkinter import *
import tkinter.messagebox as mb
import tksvg
import sqlite3
import filecmp


human = sqlite3.connect('humans_duty_former.db')
c = human.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS human(
    number STR

)
""")
human.commit()

c.execute("""INSERT INTO human(number)
VALUES('1')
""")
human.commit()

c.execute("SELECT * FROM human;")
one_result = c.fetchone()
print(one_result)








even_numbers=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
list_history = "list_history.txt"




count_clicks = 0

def randomaize():
    global slovar
    global count_clicks
    global nothing
    global duties
    global number_one
    global number_two
    nothing = 2000

    count_clicks+=1
   
    slovar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

    number_one = random.choice(slovar)
    number_two = random.choice(slovar)
    gg_chel_first.configure(text=number_one)
    gg_chel_second.configure(text=number_two)

    





    f = open(list_history,'at')
    f.write(str(f'Первый дежурный:{number_one}\n'))
    f.write(str(f'Второй дежурный:{number_two}\n'))
    f.write(f'-------------------------------------------------\n')
    f.close()  

    c.execute("SELECT number FROM human")
    duties = c.fetchall()
    print(duties)
    if number_one and number_two in duties:
        mb.showinfo('DUTIES', "They on duty")

    
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
def duty_one():
    duty = (str(number_one))
    c.executemany("INSERT INTO human VALUES(?);", duty)
    c.execute("SELECT * FROM human;")
    one_result = c.fetchall()
    print(one_result) 
    human.commit()


window = Tk()
window.title("Randomizer")
window.geometry("410x280")


window.resizable(width=0, height=0)
window["bg"] = "gray22"

#----------BACKGROUND-----------------------------------------------------
back_image = tksvg.SvgImage(master=window, file="c.svg", scale=1)
label =Label(bg='#CCCCCC', image=back_image, borderwidth=0, relief="solid")
print(label.winfo_reqwidth(), label.winfo_reqheight())
label.pack()  
#----------------BUTTONS---------------------------------------------
btn = Button(window, text="START", font="Verdana",bg="green", command=randomaize)
btn.place(relx=0.5, rely=0.6,anchor=CENTER)

btn_one= Button(window, text="APPEND", font="Verdana",bg="green", command=duty_one)
btn_one.place(relx=0.1, rely=0.4)

btn_two= Button(window, text="APPEND", font="Verdana",bg="green", command=duty_one)
btn_two.place(relx=0.7, rely=0.4)

#---------------LABELS---------------------------------------------------------------
text_one = Label(window, text='First:', bg="#270f1c",font="Elephant",fg='green')
text_one.place(relx=0.2, rely=0.1,anchor=CENTER)

text_two =Label(window, text='Second:', bg="#270f1c",font="Elephant",fg='green')
text_two.place(relx=0.8, rely=0.1,anchor=CENTER)

gg_chel_first = Label(window, text='0', bg="#270f1c",font="Ethnocentric",fg='#d00000')
gg_chel_first.place(relx=0.2, rely=0.3,anchor=CENTER)

gg_chel_second = Label(window, text='0', bg="#270f1c",font="Ethnocentric",fg='#d00000')
gg_chel_second.place(relx=0.8, rely=0.3,anchor=CENTER)

window.mainloop()