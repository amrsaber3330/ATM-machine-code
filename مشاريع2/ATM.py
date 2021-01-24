import tkinter as tk
import sqlite3
import tkinter.messagebox

ids = []
password = []
cash = []
ver = []
# ids = ["29906131500317", "301070500317", "299042000542"]
# password = ["9999", "2222", "0000"]
# cash = ["6000", "4500", "5200"]
card = 0


def msg(out):
    tkinter.messagebox.showinfo("ATM", out)


def show_entry_fields():
    global card
    global ids
    global password
    global cash
    conn = sqlite3.connect("atm.db")
    c = conn.cursor()
    c.execute("SELECT * FROM card_code")
    records = c.fetchall()
    print(records)
    conn.commit()
    conn.close()
    for i in range(len(records)):
        ids.append(records[i][0])
        password.append(records[i][1])
        cash.append(records[i][2])
        ver.append(records[i][3])
    in_id = e1.get()
    in_pass = e2.get()
    e3.delete(0, tk.END)
    if in_id in ids:
        for i in range(len(ids)):
            if in_id == ids[i] and in_pass == password[i]:
                if ver[i] == 0:
                    f2.tkraise()
                    card = i
                    e3.insert(0, cash[card])
                    msg("welcome")
                    break
                else:
                    print("This bank card isn't verified")
                    msg("This bank card isn't verified")
                    break
            else:
                if i == len(ids) - 1:
                    print("Wrong password please try again")
                    msg("Wrong password please try again")
    else:
        print("Your ID not exist")
        msg("Your ID not exist")
    print("ID: %s\nPassword: %s" % (e1.get(), e2.get()))
    print(card)
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)


def withdraw():
    if float(cash[card]) >= float(e4.get()):
        reminder = float(cash[card]) - float(e4.get())
        cash[card] = str(reminder)
        conn = sqlite3.connect("atm.db")
        c = conn.cursor()
        c.execute("UPDATE card_code SET cash = :cash WHERE id=:charge_card", {'cash': cash[card], 'charge_card': ids[card]})
        conn.commit()
        conn.close()
        f2.tkraise()
        print(f'''a {e4.get()} L.P has been withdrawn from your balance''')
        msg(f'''a {e4.get()} L.P has been withdrawn from your balance''')
    else:
        print("Not enough money in your balance")
        msg("Not enough money in your balance")
    e4.delete(0, tk.END)
    e3.delete(0, tk.END)
    e3.insert(0, cash[card])


def back():
    f2.tkraise()
    e3.delete(0, tk.END)
    e3.insert(0, cash[card])


def raise_frame(frame):
    frame.tkraise()


master = tk.Tk()
master.title("ATM")
f1 = tk.Frame(master, bg="#11EBC2")
f2 = tk.Frame(master, bg="#11EBC2")
f3 = tk.Frame(master, bg="#11EBC2")
f4 = tk.Frame(master, bg="#11EBC2")
for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

# *********Frame1*******
tk.Label(f1, text="", bg="#11EBC2").grid(row=0)
tk.Label(f1, text="ID", bg="#11EBC2").grid(row=1, column=1)
tk.Label(f1, text="Password", bg="#11EBC2").grid(row=2, column=1)
tk.Label(f1, text="", bg="#11EBC2").grid(row=3, column=1)

e1 = tk.Entry(f1, width=40)
e2 = tk.Entry(f1, width=40)
e1.grid(row=1, column=2, pady=5, padx=10)
e2.grid(row=2, column=2, pady=5, padx=10)

tk.Button(f1, text='Quit', command=master.quit, width=10).grid(row=4, column=0, sticky=tk.W, pady=20, padx=8)
tk.Button(f1, text='Enter', command=show_entry_fields, width=10).grid(row=4, column=2, sticky=tk.W, pady=20, padx=80)

# *********Frame2**********
tk.Button(f2, text='Balance inquiry', command=lambda: raise_frame(f3), width=25, height=2).grid(row=3, column=2, sticky=tk.W, pady=8, padx=150)
tk.Button(f2, text='Withdraw', command=lambda: raise_frame(f4), width=25, height=2).grid(row=4, column=2, sticky=tk.W, pady=8, padx=150)
tk.Button(f2, text='Return Card', command=lambda: raise_frame(f1), width=15).grid(row=5, column=2, sticky=tk.W, pady=8, padx=180)

# *********Frame3*********
tk.Label(f3, text="Your Balance", height=2).grid(row=1, column=1, pady=12)
e3 = tk.Entry(f3, width=40)
tk.Button(f3, text='Return Card', command=lambda: raise_frame(f1), width=10).grid(row=4, column=0, sticky=tk.W, pady=4, padx=8)
tk.Button(f3, text='Back', command=back, width=10).grid(row=4, column=1, sticky=tk.W, pady=4, padx=80)
e3.grid(row=2, column=1, padx=10, pady=10)
# *********Frame4**********
tk.Label(f4, text="Enter the cash you want", height=2).grid(row=1, column=1, pady=12)
e4 = tk.Entry(f4, width=40)
e4.grid(row=2, column=1, padx=40, pady=12)
# tk.Label(f4, text="Note that the available categories", height=1).grid(row=4, column=1, padx=10)
tk.Button(f4, text='Return Card', command=lambda: raise_frame(f1), width=10).grid(row=5, column=0, sticky=tk.W, pady=8, padx=5)
tk.Button(f4, text='Withdraw', command=withdraw, width=10).grid(row=5, column=1, sticky=tk.W, pady=8, padx=5)
tk.Button(f4, text='Back', command=lambda: f2.tkraise(), width=10).grid(row=5, column=1, sticky=tk.W, pady=8, padx=95)

f1.tkraise()
master.mainloop()

tk.mainloop()
