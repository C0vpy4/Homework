import random
from tkinter import *
import tkinter.messagebox as mb
import tksvg
import sqlite3
import datetime
from collections import deque



class Window():

    def randomize():

        # Подключаем таблицу
        
        human = sqlite3.connect('humans_duty_former.db')
        
        cursor = human.cursor()

        # Текущая дата, время и тд
        data_time = datetime.datetime.now()
        
        # Запись даты и время в текстовый документ
        list_history = "list_history.txt"
        f = open(list_history,'at', encoding='utf-16')
        f.write(f'--------------------{data_time}--------------------\n')
        f.close()

        # Ищем все фамилии
        cursor.execute("SELECT name FROM human;")
        res1 = random.choice(cursor.fetchall())
        
        cursor.execute("SELECT name FROM human;")
        res2 = random.choice(cursor.fetchall())
        #print(res1, res2)

        # Создаём словарь с фамилиями учеников
        slovar_secondname = [res1,res2]#"Балаев","Балашов","Будовская","Виноградов"]

        

        # Выбираем случайно 2-х учеников
        duty_one = random.choice(slovar_secondname)
        cursor.execute(f"SELECT userid FROM human WHERE name='{''.join(duty_one)}'")
        pust = cursor.fetchall()
        
        duty_two = random.choice(slovar_secondname)
        cursor.execute(f"SELECT userid FROM human WHERE name='{''.join(duty_two)}'")
        pust2 = cursor.fetchall()

        # Проверяем на одинаковость и если одинаковы выбираем ещё раз
        if pust == pust2:
            slovar_secondname = [res1,res2]
            duty_one = random.choice(slovar_secondname)
            duty_two = random.choice(slovar_secondname)
        

     


        # Выводим их на экран
        gg_chel_first.configure(text=duty_one)
        gg_chel_second.configure(text=duty_two)

        #
        cursor.execute(f"DELETE FROM human WHERE name='{''.join(duty_one)}'")
        cursor.execute(f"DELETE FROM human WHERE name='{''.join(duty_two)}'")
        
    
        cursor.execute(f"SELECT * FROM human WHERE name='{''.join(duty_one)}'")
        cursor.execute(f"SELECT * FROM human WHERE name='{''.join(duty_two)}'")
        #print(cursor.fetchall())

        #cursor.execute("SELECT name FROM human;")
        #print(cursor.fetchall())

        # Записываем историю дежурных
        f = open(list_history,'at', encoding="utf-16")
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

    def update_db():

        human = sqlite3.connect('humans_duty_former.db')
        cursor = human.cursor()
        # Создаём таблицу
        cursor.execute("""CREATE TABLE IF NOT EXISTS human(
        userid INT PRIMARY KEY,
        name STR 
        )""")
        human.commit()
        #
        peaple = [('0001','Балаев'),('0002','Балашов'),('0003','Будовская'),('0004','Виноградов'),('0005','Гатаулин'),('0006','Горовой'),('0007','Данилюк'),('0008','Демидов'),('0009','Жабборов'),('0010','Иванов'),('0011','Касьяненко'),('0012','Королёв'),('0013','Кузьмин'),('0014','Лукашин'),('0015','Мешков'),('0016','Никитин'),('0017','Подгорнов'),('0018','Попов'),('0019','Постников'),('0020','Савилов'),('0021','Сеченев'),('0022','Сивак'),('0023','Солодовников'),('0024','Фиронов'),('0025','Хасбулаев'),('0026','Шевченко'),('0027','Шулькевич'),]
        #
        cursor.executemany("INSERT INTO human VALUES(?,?);", peaple)
        human.commit()


    #-----------------------TKINTER---------------------------------------------
    # Создание окна 
    window = Tk()
    window.title('Randomizer')
    window.geometry("410x290")
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
    btn.place(relx=0.3, rely=0.8,anchor=CENTER)

    btn = Button(window, text="Update DB", font="Verdana",bg="green", command=update_db)
    btn.place(relx=0.7, rely=0.8,anchor=CENTER)
    
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
    
