from tabulate import tabulate
import mysql.connector as mysql
db=mysql.connect(
    host="localhost",
    user="root",
    passwd="root")
s= db.cursor(buffered = True)


s.execute("CREATE DATABASE IF NOT EXISTS Management_system")
s.execute("USE Management_system")
s.execute("CREATE TABLE IF NOT EXISTS Student \
(Sno INT PRIMARY KEY Auto_Increment,Sname VARCHAR(20) NOT NULL\
,email VARCHAR(25) NOT NULL UNIQUE KEY,phone BIGINT NOT NULL UNIQUE KEY\
,address VARCHAR(255), username VARCHAR (20) NOT NULL UNIQUE KEY,\
password VARCHAR(18) NOT NULL,User_ID VARCHAR(255) UNIQUE KEY ,\
privilege VARCHAR(8),grade VARCHAR(5))")

s.execute ("CREATE TABLE IF NOT EXISTS attendence\
(Sno INT PRIMARY KEY Auto_Increment,Sname VARCHAR(255) NOT NULL ,date DATE ,status VARCHAR(1),Grade VARCHAR(5))")

s.execute("CREATE TABLE IF NOT EXISTS Teacher\
(Tno INT PRIMARY KEY Auto_Increment,Sname VARCHAR(20) NOT NULL\
,email VARCHAR(25) NOT NULL UNIQUE KEY,phone BIGINT NOT NULL UNIQUE KEY\
, username VARCHAR (20) NOT NULL UNIQUE KEY,password VARCHAR(18) NOT NULL,teach VARCHAR(7),privilege  VARCHAR(8))")

def student_session(Sname):
    print("-"*80)
    print("Student's Menu")
    print("")
    print("1.View Register ")
    print("2.Download Register ")
    print("3.Logout")
    user_option=input(str("Option : "))
    if user_option =="1":
        print(Sname)
        print("Displaying Register")
        Sname = (str(Sname),)
        s.execute("SELECT Sname, date, status FROM attendence WHERE Sname=%s",Sname)
        records = s.fetchall()
        for record in records:
            print(record)
    elif user_option =="2":
        print("Download Register")
        Sname = (str(Sname),)
        s.execute("SELECT Sname,status,date FROM attendence WHERE Sname =%s",Sname)
        records= s.fetchall()
        for record in records:
            with open ('C:/Users/Dell/Desktop/Register.txt',"w") as f :
                f.writelines(str(record)+"\n")
            f.close()
        print("All records Successfully downloaded")
    elif user_option =="3":
       return
    else:
        print("No valid option was selected")
        return


def teacher_session():
    while 1:
        print("_"*80,"\n\n")
        print("Teacher Menu".center(40))
        print("\n1.Mark student register")
        print("2.View register")
        print("3.Student profile")
        print("4.Logout")
        user_option=input(str("Option : "))
        print("*"*80,"\n")
        if user_option =="1":
            print("Mark student register")
            grade= input(str("Enter the Grade for register :"))
            query_val = (grade ,'Student')
            s.execute("SELECT Sname  FROM Student WHERE grade = %s AND privilege = %s",query_val)
            records=s.fetchall()
            date= input(str("Date :YYYY-MM-DD:"))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                #present|absent|late
                status = input (str("status for " + str(record)+" "+ "[P/A/L] :"))
                query_val = (str(record),date, status)
                s.execute("INSERT INTO attendence (Sname,date,status) VALUES(%s,%s,%s)",query_val)
                db.commit()
                print(record + " Marked as " +""+ status)
        elif user_option == "2":
            print("viewing all student registers")
            s.execute("SELECT Sname ,date,status FROM attendence " )
            print(tabulate(s,headers=['Student Name','Date','Status'],tablefmt='fancy_grid'))
            records = s.fetchall()
            for record in records:
                print(record)
        elif user_option == "3":
            print("-"*80)
            print("Student Profile".center(30))
            grade = input(str("Enter the Grade for Viewing Student details :"))
            query_val = (grade ,'Student')
            s.execute("SELECT Sname,email,phone,User_ID,address FROM student WHERE grade=%s AND privilege = %s",query_val)
            print(tabulate(s,headers=['Student Name','Email','Phone','User_ID','Address' ],tablefmt='fancy_grid'))
            res=s.fetchall()
            for rec in res:
                print(rec)

        elif user_option =="4":
            break
        else:
            print("No valid option was selected")
            return


def admin_session():
    print("\n\nLOGIN SUCCESSFULl\n")
    while 1:
        print("_"*80,"\n")
        print("\n","WELCOME ADMIN TO OUR SYSTEM")
        print("\n","Admin Menu".center(79))
        print("\n1.Register new Student")
        print("2.Register new Teacher")
        print("3.Delete Existing student")
        print("4.Delete Existing Teacher")
        print("5.Logout")
        user_option =input(str("Option : "))
        print("_"*80,"\n\n")
        if user_option =="1":
            print("Register new Student")
            f_name = input(str("Enter the First Name : "))
            l_name = input(str("Enter the last Name : "))
            Sname= f_name + " " +l_name
            email = input(str("Enter email address : "))
            #alpha="abcdefghijklmnopqrstuvwxyz"
            #num="1234567890"
            while("@" not in email or "gmail.com" not in email):
                print("Invalid email address")
                email=input("Enter your email address = ")
            phone = input(str("Enter the Mobile number :"))
            while(len(phone)!=10 or phone.isdigit() is False):
                print("Enter Valid Mobile Number")
                phone=input("Enter the Mobile No. = ")
            username = input(str(" Student Username :-"))
            address=input(str(" Student address :-"))
            password = input(str(" Student Password :-"))
            User_ID= input(str(" Student ID :-"))
            grade = input(str("Enter the Grade of Student :"))
            query_vals = (Sname, email ,phone ,address, username,password ,User_ID,grade)
            s.execute("INSERT INTO Student(Sname, email ,phone ,address, username , password,User_ID,grade,privilege) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'Student')",query_vals)
            db.commit()
            print( Sname +" has been registered as a student")
        elif user_option =="2":
            print("Register new Teacher")
            f_name = input(str("Enter the First Name : "))
            l_name = input(str("Enter the last Name : "))
            Sname= f_name +" "+ l_name
            email = input(str("Enter email address : "))
            #alpha="abcdefghijklmnopqrstuvwxyz"
            #num="1234567890"
            while("@" not in email or "gmail.com" not in email):
                print("Invalid email address")
                email=input("Enter your email address = ")
            phone = input(str("Enter the Mobile number :"))
            while(len(phone)!=10 or phone.isdigit() is False):
                print("Enter Valid Mobile Number")
                phone=input("Enter the Mobile No. = ")
            username = input(str(" Teacher Username :-"))
            password = input(str(" Teacher Password :-"))
            teach = input (str("Enter the subject taught by him/her :"))
            query_vals = (Sname,email,phone,username,password,teach)
            s.execute("INSERT INTO Teacher(Sname,email,phone,username,password,teach,privilege) VALUES (%s,%s,%s,%s,%s,%s,'Teacher')",query_vals)
            db.commit()
            print( Sname + " has been registered as a teacher")
        elif user_option =="3":
            print("Delete Existing Student Accounts")
            Sname = input(str("Student Name :"))
            username = input (str("student username :"))
            query_val = (Sname,username,"student")
            s.execute("DELETE FROM Student WHERE Sname = %s AND username = %s AND privilege = %s",query_val)
            db.commit()
            if s.rowcount<1:
                print("user not found")
            else:
                print( Sname + " has been deleted as a student")
        elif user_option =="4":
            print("Delete Existing Teacher Accounts")
            Sname = input(str("Teacher Name :"))
            username = input (str("Teacher username :"))
            query_val = (Sname,username,'Teacher')
            s.execute("DELETE FROM teacher WHERE Sname = %s AND username = %s AND privilege = %s",query_val)
            db.commit()
            if s.rowcount<1:
                print("user not found")
            else:
                print( Sname +" has been deleted as a teacher")
        elif user_option =="5":
            break
        else:
            print("Invalid options")


def auth_student():
    print(" ")
    print("Student's login".center(35))
    print("")
    Sname = input(str("Student name = "))
    username= input(str("Student username = "))
    password = input(str("PASSWORD = "))
    query_val = (Sname,username,password)
    s.execute("SELECT Sname FROM Student WHERE Sname= %s AND username=%s AND password = %s ",query_val)
    #User_ID= s.fetchone()
    if s.rowcount <= 0:
        print("Invalid login details")
    else:
        student_session(Sname)


def auth_teacher():
    print(" ")
    print("Teacher's login")
    print("")
    username = input(str("USERNAME = "))
    password = input(str("PASSWORD = "))
    teach = input(str("Enter the Subject you teach : "))
    query_val = (username,password,teach)
    s.execute("SELECT * FROM Teacher WHERE username = %s AND password = %s AND teach = %s",query_val)
    if s.rowcount <= 0:
        print("\n\nLogin unauthorized")
        print("_"*80)
        return auth_user()
    else:
        teacher_session()
        #print("Welcome"+username)

def correct_auth():
    print("*"*80,"\n\n")
    print ("Incorrect username/password !!!\n\n")
    print("1.Login")
    print("2.Main Menu")
    xuser_option = input(str("\nOPTION :-  "))
    if xuser_option == "1":
        username = input(str("USERNAME = "))
        password = input(str("PASSWORD = "))
        if username == "admin":
            if password == "password":
                admin_session()
            else:
                print ("\nIncorrect username/password !!!\n")
    elif xuser_option == "1":
        return main()


def auth_admin():
    print("\n","ADMIN LOGIN".center(80))
    username = input(str("USERNAME = "))
    password = input(str("PASSWORD = "))
    if (username != "admin"):
        if(password != "password"):
            correct_auth()
    elif (username == "admin"):
        if (password == "password"):
            admin_session()
    else:
        print("Login details not recognised ")

def auth_user():
    print("LOGIN AS".center(40))
    print("\n1.TEACHER")
    print("2.STUDENT")
    print("3.Exit")
    user_option = input(str("\nOPTION :-  "))
    print("_"*80,"\n\n")
    if user_option == "1":
        auth_teacher()
    elif user_option =="2":
        auth_student()
    elif user_option =="3":
        return
    else:
        print("Out of range")
        
def main():
    while 1:
        print("_"*80,"\n\n")
        print("="*80)
        print("="*9,"WELCOME TO THE COLLEGE MANAGEMENT SYSTEM","="*9)
        print("="*80)
        print("MAIN MENU".center(80),"\n\n")
        print("1.Login as USER".center(40))
        print("2.login as ADMIN".center(40))
        print("3.Exit".center(30))
        user_option = input(str("\nOPTION :-  "))
        print("_"*80,"\n")
        if user_option == "1":
            auth_user()
        elif user_option =="2":
            auth_admin()
        elif user_option =="3":
            print("Exit")
            break
        else:
            print("\n\nNo valid choice was selected")
main()
