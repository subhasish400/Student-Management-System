import sqlite3

con = sqlite3.connect('database.db')
cr = con.cursor()

cr.execute("create table if not exists admin(name TEXT, password TEXT)")
cr.execute("create table if not exists user(name TEXT, password TEXT, mobile TEXT, email TEXT)")
cr.execute("create table if not exists students(name TEXT, phone TEXT, email TEXT, usn TEXT, sem TEXT, branch TEXT)")

cr.execute("create table if not exists python(name TEXT, usn TEXT, one TEXT, two TEXT, three TEXT, four TEXT, five TEXT, six TEXT, seven TEXT, eight TEXT, nine TEXT, ten TEXT, eleven TEXT, twelw TEXT, thirteen TEXT, fourtneen TEXT, fifteen TEXT, sixteen TEXT, seventeen TEXT, eighteen TEXT, nineteen TEXT, twenty TEXT, twentyone TEXT, twentytwo TEXT, twentythree TEXT, twentyfour TEXT, twentyfive TEXT, twentysix TEXT, twentyseven TEXT, twentyeight TEXT, twentynine TEXT, thirty TEXT, total TEXT)") 
cr.execute("create table if not exists python_marks(name TEXT, usn TEXT, IA1 TEXT, IA2 TEXT, IA3 TEXT, total TEXT)")