from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import csv
import telepot

con = sqlite3.connect('database.db')
cr = con.cursor()

cr.execute("create table if not exists admin(name TEXT, password TEXT)")
cr.execute("create table if not exists user(name TEXT, password TEXT, mobile TEXT, email TEXT)")
cr.execute("create table if not exists students(name TEXT, phone TEXT, email TEXT, usn TEXT, sem TEXT, branch TEXT)")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlog', methods=['GET', 'POST'])
def adminlog():
    if request.method == 'POST':

        con = sqlite3.connect('database.db')
        cr = con.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM admin WHERE name = '"+name+"' AND password= '"+password+"'"
        cr.execute(query)

        result = cr.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            con = sqlite3.connect('database.db')
            cr = con.cursor()

            cr.execute("select name from user")
            result = cr.fetchall()
            print(result)
            return render_template('adminlog.html', result=result)

    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        con = sqlite3.connect('database.db')
        cr = con.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cr.execute(query)

        result = cr.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            # f = open('timing.csv', 'r')
            # reader = csv.reader(f)
            # List = []
            # for row in reader:
            #     List.append(row)
            # print(List)
            # head=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
            return render_template('class_time.html')#, List=List, head=head)

    return render_template('index.html')

@app.route('/class_time_table', methods=['GET', 'POST'])
def class_time_table():
    if request.method == 'POST':

        branch = request.form['branch']
        sem = request.form['sem']

        file1 = '{}_{}.csv'.format(sem, branch)
        print(file1)

        f = open(file1, 'r')
        reader = csv.reader(f)
        List = []
        for row in reader:
            List.append(row)
        print(List)
        head=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        return render_template('class_time.html', List=List, head=head)

    return render_template('index.html')

@app.route('/staff_time_table', methods=['GET', 'POST'])
def staff_time_table():
    if request.method == 'POST':

        name = request.form['name']

        file1 = '{}.csv'.format(name)
        print(file1)

        f = open(file1, 'r')
        reader = csv.reader(f)
        List = []
        for row in reader:
            List.append(row)
        print(List)
        head=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        return render_template('staff_time.html', List=List, head=head)

    return render_template('index.html')

@app.route('/lecturer')
def lecturer():
    con = sqlite3.connect('database.db')
    cr = con.cursor()
    query = "SELECT * FROM user"
    cr.execute(query)
    result = cr.fetchall()
    if result:
        return render_template('viewlecture.html', result=result)
    else:
        return render_template('viewlecture.html', msg="data not found")

@app.route('/remove/<email>')
def remove(email):
    con = sqlite3.connect('database.db')
    cr = con.cursor()
    cr.execute("delete from user where email='"+email+"'")
    con.commit()
    return redirect(url_for('lecturer'))

@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        con = sqlite3.connect('database.db')
        cr = con.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        cr.execute("insert into user values ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        con.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/class_time')
def class_time():
    return render_template('class_time.html')

@app.route('/staff_time')
def staff_time():
    con = sqlite3.connect('database.db')
    cr = con.cursor()

    cr.execute("select name from user")
    result = cr.fetchall()

    print(result)
    return render_template('staff_time.html', result=result)

@app.route('/addstudent')
def addstudent():
    return render_template('add_student.html')

@app.route('/take_attendence', methods=['POST', 'GET'])
def take_attendence():
    if request.method == 'POST':
        con = sqlite3.connect('database.db')
        cr = con.cursor()
        names=[]
        usns= []
        attend = []
        
        try:
            i = 0
            while True:
                names.append(request.form['name'+str(i)])
                usns.append(request.form['usn'+str(i)])
                attend.append(request.form['AP'+str(i)])
                i += 1
        except:
            pass

        subject = request.form['subject']
        day = int(request.form['day'])

        print(subject, day)
        print(names)
        print(usns)
        print(attend)

        col = ['','one', 'two','three','four', 'five', 'six', 'seven', 'eight','nine', 'ten', 'eleven', 'twelw' , 'thirteen', 'fourtneen','fifteen' , 'sixteen' , 'seventeen' , 'eighteen' , 'nineteen' , 'twenty' , 'twentyone' , 'twentytwo' , 'twentythree' , 'twentyfour' , 'twentyfive' , 'twentysix' , 'twentyseven' , 'twentyeight' , 'twentynine' , 'thirty']           
        
        for l in range(len(names)):
            cr.execute("create table if not exists '"+subject+"'(name TEXT, usn TEXT, one TEXT, two TEXT, three TEXT, four TEXT, five TEXT, six TEXT, seven TEXT, eight TEXT, nine TEXT, ten TEXT, eleven TEXT, twelw TEXT, thirteen TEXT, fourtneen TEXT, fifteen TEXT, sixteen TEXT, seventeen TEXT, eighteen TEXT, nineteen TEXT, twenty TEXT, twentyone TEXT, twentytwo TEXT, twentythree TEXT, twentyfour TEXT, twentyfive TEXT, twentysix TEXT, twentyseven TEXT, twentyeight TEXT, twentynine TEXT, thirty TEXT, total TEXT)") 
            cr.execute("select * from '"+subject+"' where usn = '"+usns[l]+"' and name = '"+names[l]+"'")
            result = cr.fetchall()
            if result:
                cr.execute("update '"+subject+"' set '"+col[day]+"' = '"+attend[l]+"' where usn = '"+usns[l]+"' and name = '"+names[l]+"'")
                con.commit()
            else:
                cr.execute("insert into '"+subject+"' (name, usn, '"+col[day]+"') values ('"+names[l]+"','"+usns[l]+"','"+attend[l]+"')")
                con.commit()

        return redirect(url_for('attendence'))    
    return render_template('add_student.html')

@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        data = request.form

        List = []
        for key in data:
            List.append(data[key])

        con = sqlite3.connect('database.db')
        cr = con.cursor()
        cr.execute("insert into students values (?,?,?,?,?,?)", List)
        con.commit()

    return render_template('add_student.html')

@app.route('/addmarks')
def addmarks():
    con = sqlite3.connect('database.db')
    cr = con.cursor()

    cr.execute("select name, usn from students")
    result = cr.fetchall()
    if result:
        names = []
        usns = []
        for row in result:
            names.append(row[0])
            usns.append(row[1])
        return render_template('add_marks.html', names = names, usns=usns)
    else:
        return render_template('add_marks.html', msg = 'student data not found')


@app.route('/add_marks', methods=['POST', 'GET'])
def add_marks():
    if request.method == 'POST':
        con = sqlite3.connect('database.db')
        cr = con.cursor()
        name = request.form['name']
        usn = request.form['usn']
        subject = request.form['subject']
        marks = request.form['marks']
        ia = int(request.form['ia'])
        col = ['IA1', 'IA2', 'IA3']
        subject = subject+'_marks'
        cr.execute("create table if not exists '"+subject+"'(name TEXT, usn TEXT, IA1 TEXT, IA2 TEXT, IA3 TEXT, total TEXT)")
        cr.execute("insert into '"+subject+"' (name, usn,'"+col[ia]+"') values ('"+name+"','"+usn+"','"+marks+"')")
        con.commit()
        return render_template('add_student.html')
    return render_template('add_student.html')

@app.route('/reports_page')
def reports_page():
    return render_template('reports.html')

@app.route('/viewstudents', methods=['POST', 'GET'])
def viewstudents():
    if request.method == 'POST':
        sem = request.form['sem']
        branch = request.form['branch']

        con = sqlite3.connect('database.db')
        cr = con.cursor()

        cr.execute("select * from students where sem='"+sem+"' and branch = '"+branch+"'")
        result = cr.fetchall()
        if result:
            headings = ['name', 'phone', 'email', 'usn', 'sem', 'branch']
            return render_template('view_students.html', result=result, headings=headings)  
        else:
            return render_template('view_students.html', msg='data not found')
    return render_template('view_students.html')

@app.route('/send_alert/<sub>')
def send_alert(sub):
    con = sqlite3.connect('database.db')
    cr = con.cursor()

    cr.execute("select total, name from '"+sub+"'")
    result = cr.fetchall()
    for row in result:
        marks, name = row
        marks = float(marks)
        print(marks, name)

        if marks < 61.0:
                bot = telepot.Bot('5505770046:AAHZ00lFDyhh9AL_r7XFrzKaqDT2LWp52V4')
                bot.sendMessage('1388858613', str('hi {}, attendence shortlist, {} percentage'.format(name, marks)))

                # bot = telepot.Bot('6073132853:AAH_inordtq_AKyeP5GiT3MZByAJ0hs1sNs')
                # bot.sendMessage('803561002', str('hi {}, attendence shortlist, {} percentage'.format(name, marks)))
    return render_template('reports.html')

@app.route('/reports', methods=['POST', 'GET'])
def reports():
    if request.method == 'POST':
        sub = request.form['subject']
        con = sqlite3.connect('database.db')
        cr = con.cursor()

        cr.execute("select * from '"+sub+"'")
        result = cr.fetchall()
        
        if result:
            for row in result:
                total = 0
                for col in row[2:]:
                    if col == 'P':
                        total += 1

                percentage = total/30*100

                percentage=str(percentage)
                
                cr.execute("update '"+sub+"' set total = '"+percentage+"' where name = '"+row[0]+"' and usn = '"+row[1]+"'")
                con.commit()

            cr.execute("select * from '"+sub+"'")
            result = cr.fetchall()

            #get table column name
            List = cr.execute("select * from '"+sub+"'")
            headings = []
            for row in List.description:
                headings.append(row[0])

            return render_template('reports.html', result=result, headings=headings, Sub=sub)
        else:
            return render_template('reports.html', msg='result not found')
    return render_template('reports.html')

@app.route('/attendence')
def attendence():
    con = sqlite3.connect('database.db')
    cr = con.cursor()

    cr.execute("select name, usn from students")
    result = cr.fetchall()
    if result:
        names = []
        usns = []
        for row in result:
            names.append(row[0])
            usns.append(row[1])
        return render_template('attendence.html', names = names, usns=usns, n=len(names))
    else:
        return render_template('attendence.html', msg = 'student data not found')

@app.route('/class_timings', methods=['GET', 'POST'])
def class_timings():
    if request.method == 'POST':
        data = request.form
        row = []
        List = []
        for key in data:
            row.append(data[key])
        
        List.append(row[:7])
        List.append(row[7:14])
        List.append(row[14:21])
        List.append(row[21:28])
        List.append(row[28:35])
        List.append(row[35:42])

        print(List)

        file1 = '{}_{}.csv'.format(row[42], row[43])
        print(file1)
        f = open(file1, 'w', newline='')
        writer = csv.writer(f)
        writer.writerows(List)
        f.close()
        return render_template('classtimepage.html')
    return render_template('classtimepage.html')

@app.route('/staff_timings', methods=['GET', 'POST'])
def staff_timings():
    if request.method == 'POST':
        data = request.form
        row = []
        List = []
        for key in data:
            row.append(data[key])
        
        List.append(row[:7])
        List.append(row[7:14])
        List.append(row[14:21])
        List.append(row[21:28])
        List.append(row[28:35])
        List.append(row[35:42])

        print(List)

        file1 = '{}.csv'.format(row[42])
        print(file1)
        f = open(file1, 'w', newline='')
        writer = csv.writer(f)
        writer.writerows(List)
        f.close()

        con = sqlite3.connect('database.db')
        cr = con.cursor()

        cr.execute("select name from user")
        result = cr.fetchall()

        print(result)

        return render_template('adminlog.html', result=result)
    return render_template('adminlog.html')

if __name__ == "__main__":
    app.run(debug=True)
