import random
from tkinter import *
import tkinter.messagebox as mb
import tksvg
import sqlite3
import datetime
from collections import deque

class Window():
    def randomize():

        # Создаём таблицу
        human = sqlite3.connect('humans_duty_former23.db')
        global cursor
        cursor = human.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS human(
        name STR
        )""")

        # Создаём словарь с фамилиями учеников
        slovar_secondname = ["Балаев","Балашов","Будовская","Виноградов"]

        # Текущая дата, время и тд
        data_time = datetime.datetime.now()

        # Запись даты и время в текстовый документ
        list_history = "list_history.txt"
        f = open(list_history,'at')
        f.write(f'--------------------{data_time}--------------------\n')
        f.close()

        # Выбираем случайного 2-х учеников
        duty_one = random.choice(slovar_secondname)
        duty_two = random.choice(slovar_secondname)
        # Проверяем на одинаковость и если одиноаковы выбираем ещё раз
        if duty_one == duty_two:
            duty_one = random.choice(slovar_secondname)
            duty_two = random.choice(slovar_secondname)


        # Выводим их на экран
        gg_chel_first.configure(text=duty_one)
        gg_chel_second.configure(text=duty_two)
    

        # Записываем историю дежурных
        f = open(list_history,'at')
        f.write(f'Первый дежурный:{duty_one}, Второй дежурный:{duty_two}\n')
        f.close()  

    # Показываем историю дежурных
    def show_history():
        
        list_history = "list_history.txt"
        with open(list_history) as file:
            # Ищем последнюю строчку в файле
            [last_line] = deque(file, maxlen=1) or ['']
        # Выводим её с помощью окна информации    
        mb.showinfo('DUTIES', last_line)

    #-----------------------TKINTER---------------------------------------------
    # Создание окна 
    window = Tk()
    window.title('Randomizer')
    window.geometry("410x280")
    # Не даём пользователю его уменьшать и растягивать
    window.resizable(width=0, height=0)

    #----------BACKGROUND-----------------------------------------------------
    back_image = tksvg.SvgImage(master=window, file="c.svg", scale=1)
    label =Label(bg='#CCCCCC', image=back_image, borderwidth=0, relief="solid")
    print(label.winfo_reqwidth(), label.winfo_reqheight())
    label.pack()  
     
    #----------------BUTTONS-------------------------------------------------------
    btn = Button(window, text="START", font="Verdana",bg="green", command=randomize)
    btn.place(relx=0.5, rely=0.6,anchor=CENTER)
    
    btn = Button(window, text="Show history", font="Verdana",bg="green", command=show_history)
    btn.place(relx=0.5, rely=0.8,anchor=CENTER)
    
    #---------------LABELS---------------------------------------------------------------
    text_one = Label(window, text='First:', bg="#270f1c",font="Elephant",fg='green')
    text_one.place(relx=0.2, rely=0.1,anchor=CENTER)

    text_two =Label(window, text='Second:', bg="#270f1c",font="Elephant",fg='green')
    text_two.place(relx=0.8, rely=0.1,anchor=CENTER)

    global gg_chel_first
    gg_chel_first = Label(window, text='0', bg="#270f1c",font="Elephant",fg='#d00000')
    gg_chel_first.place(relx=0.2, rely=0.3,anchor=CENTER)

    global gg_chel_second
    gg_chel_second = Label(window, text='0', bg="#270f1c",font="Elephant",fg='#d00000')
    gg_chel_second.place(relx=0.8, rely=0.3,anchor=CENTER)
    
    window.mainloop()

if __name__ == "__main__":
    Window()
    
