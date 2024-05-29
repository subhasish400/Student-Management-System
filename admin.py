import sqlite3

con = sqlite3.connect('database.db')
cr = con.cursor()

cr.execute("create table if not exists admin(name TEXT, password TEXT)")

cr.execute("insert into admin values('admin', 'admin')")
con.commit()