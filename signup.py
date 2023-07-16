from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()== '' or usernameEntry.get()== '' or passwordEntry.get()== '' or confirmEntry.get()== '':
        messagebox.showerror('Error', 'All Feilds Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept terms and conditions')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='sureshsara')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issues,please try again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error', 'Username Already exists')
        else:

            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import signin



def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.title('SIGNUP PAGE')
signup_window.resizable(0,0)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text=' CREATE AN ACCOUNT ',font=('Arial',17,'bold'),bg='white',fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLable=Label(frame,text='Email',font=('Arial',10,'bold'),bg='white',fg='black')
emailLable.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=30,font=('Arial',10,'bold'))
emailEntry.grid(row=2,column=0,sticky='w',padx=25,pady=2)

usernameLable=Label(frame,text='Username',font=('Arial',10,'bold'),bg='white',fg='black')
usernameLable.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Arial',10,'bold'))
usernameEntry.grid(row=4,column=0,sticky='w',padx=25,pady=2)

passwordLable=Label(frame,text='Password',font=('Arial',10,'bold'),bg='white',fg='black')
passwordLable.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Arial',10,'bold'))
passwordEntry.grid(row=6,column=0,sticky='w',padx=25,pady=2)

confirmLable=Label(frame,text='Confirm Password',font=('Arial',10,'bold'),bg='white',fg='black')
confirmLable.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,font=('Arial',10,'bold'))
confirmEntry.grid(row=8,column=0,sticky='w',padx=25,pady=2)
check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree',font=('Arial',10,'bold'),cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)


signupButton=Button(frame,text='Signup',font=('Arial',16,'bold'),bd=0,bg='blue',fg='white'
                    ,width=17,cursor='hand2',command=connect_database)
signupButton.grid(row=11,column=0,padx=10,pady=25)

alreadyaccount=Label(frame,text='Have an account ?',font=('Arial',9,'bold')
                     ,bg='white',fg='black')
alreadyaccount.grid(row=12,column=0,padx=25)

loginButton=Button(frame,text='Login',font=('Arial',10,'bold '),bg='white',fg='blue'
                   ,bd=0,cursor='hand2',activebackground='white'
                   ,activeforeground='black',command=login_page)

loginButton.grid(row=13,column=0,)
signup_window.mainloop()
