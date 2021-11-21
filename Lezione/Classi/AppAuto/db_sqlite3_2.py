import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
#from tkinter import Pack
from glob import glob


def create(obj):
    db = obj.e.get()

    if db[-3] == ".db" :
        pass
    else:
        db = db + ".db"
    try:
        conn = lite.connect(db)
        return conn
    except Error as e:
        print(e)
    finally:
        conn.close()
        obj.lb.insert(tk.END, db)
        obj.db.set("")

# crea un pulsante di: db(name)
# pulsante: call create (db)
# lista: mostra i database avviabili

class Win:
    # window
    def __init__(self):
        self.win = tk.Tk()
        # inserisci nome db
        self.l = tk.Label(self.win, text="Create a db [insert the name]")
        self.l.pack()
        self.db = tk.StringVar()
        self.e = tk.Entry(self.win, textvariable=self.db)
        self.e.pack()
        self.b = tk.Button(self.win, text="Create DB", command= lambda: 
            create(self))
        self.b.pack()
        self.lb = tk.Listbox(self.win)
        self.lb.pack()
        self.show_db()
        
    def show_db(self):
        for file in glob("*.db"):
            self.lb.insert(tk.END, file)



        # entry

        # button
        
        self.win.mainloop()

win = Win()
