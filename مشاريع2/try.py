import sqlite3

records = [('29906131500317', '9999', '6000', 0), ('301070500317', '2222', '4500', 0), ('299042000542', '0000', '5200', 0)]
idd = '29906131500317'
if idd in records[2]:
    print("repeated")
else:
    print("new")

conn = sqlite3.connect("atm.db")
c = conn.cursor()
c.execute("INSERT INTO card_code VALUES(:id, :password, :cash, :verify)",
        {
            'id': idd,
            'password': '9999',
            'cash': '60000',
            'verify': 0
        }
         )
conn.commit()
conn.close()