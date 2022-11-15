import sqlite3
import inline
import random
from colorama import init, Fore
init(autoreset=True)


# IN START
          
def create_db():
    conn = sqlite3.connect(r'users.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        password BLOB,
        money INT);
    """)
    conn.commit()

    cur.execute("SELECT * FROM users;")
    one_result = cur.fetchone()
    print(one_result)

def __init__():
    print("Registration")

    name = input('Name = ')
    password = inline.input('Password =', secret=True)
    money = 0
    insert = [name, password, money]
    conn = sqlite3.connect(r'users.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES(?,?,?);", insert )
    conn.commit()
    game()

def game():
    A = "Устное предупреждение"
    B = "5 в журнал"
    C = "4 в журнал"
    D = "3 в журнал"
    E = "2 в журнал"
    F = "Чел ты, бж"
    G = "......Как?"
    
    randomP = [A,B,C,D,E,F,G]

    priz = random.choice(randomP)
    bad = [E,F,G]
    good = [A,D]
    excelent = [B,C]

    if priz in bad:
        print(Fore.RED + f"Всё плохо:{priz}")
    if priz in good:
        print(Fore.BLUE +  f"Норм:{priz}")    
    if priz in excelent:
        print(Fore.GREEN + f"Красава, лучший:{priz}")    

def start():
    name = input("Name = " )
    conn = sqlite3.connect(r'users.db')
    cur = conn.cursor()
    for i in cur.execute("SELECT name FROM users;"): 
        if i == name:
            print(i)
            password = inline.input("Password = ", secret = True)
            for i in cur.execute("SELECT password FROM users;"):
                if password == i:
                    game()
        else:
            __init__()
  
game()

