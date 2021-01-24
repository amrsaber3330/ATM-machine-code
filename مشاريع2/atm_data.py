import tkinter as tk
import sqlite3

idd = ""
password = ""
cash = ""
ver = ""


def show():
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("SELECT * FROM card_code")
    records = c.fetchall()
    print(records)
    conn.commit()
    conn.close()


def insert():
    global idd
    global password
    global cash
    global ver
    idd = e1.get()
    password = e2.get()
    cash = e3.get()
    ver = e4.get()
#    ver = check.getboolean(ver)
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("SELECT * FROM card_code")
    records = c.fetchall()
    print(records)
    conn.commit()
    conn.close()
    for i in range(len(records)):
        if idd in records[i] and i == len(records) - 1:
            print("This bank card is already exist")
        elif idd not in records[i] and i == len(records) - 1:
            conn = sqlite3.connect("atm.db")
            c = conn.cursor()
            c.execute("INSERT INTO card_code VALUES(:id, :password, :cash, :verify)",
                    {
                        'id': idd,
                        'password': password,
                        'cash': cash,
                        'verify': int(ver)
                    }
                    )
            conn.commit()
            conn.close()


def update():
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("UPDATE card_code SET cash = :cash , password = :pass , verify = :ver WHERE id=:charge_card", {'cash': e3.get(), 'pass': e2.get(), 'ver': int(e4.get()), 'charge_card': e1.get()})
    conn.commit()
    conn.close()


# conn = sqlite3.connect("atm.db")
# c = conn.cursor()
# c.execute('''CREATE TABLE card_code(
#              id text,
#              password text,
#              cash text,
#             verify bool
#             )''')
# conn.commit()
# conn.close()


master = tk.Tk()
e1 = tk.Entry(master, width=40)
e2 = tk.Entry(master, width=40)
e3 = tk.Entry(master, width=40)
e4 = tk.Entry(master, width=40)
e1.grid(row=0, column=0, pady=5)
e2.grid(row=1, column=0, pady=5)
e3.grid(row=2, column=0, pady=5)
e4.grid(row=3, column=0, pady=5)
# check = tk.Checkbutton(master, text="Verify")
# check.grid(row=3, columnspan=2)
tk.Button(master, text='Add data', command=insert, width=20, height=3).grid(row=4, column=0, sticky=tk.W, pady=10, padx=150)
tk.Button(master, text='Show data', command=show, width=20, height=3).grid(row=5, column=0, sticky=tk.W, pady=10, padx=150)
tk.Button(master, text='Update', command=update, width=20, height=3).grid(row=6, column=0, sticky=tk.W, pady=10, padx=150)
tk.Button(master, text='Quit', command=master.quit, width=10, height=2).grid(row=7, column=0, sticky=tk.W, pady=15, padx=180)

master.mainloop()
