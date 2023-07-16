from tkinter import *
from tkinter import  messagebox
from PIL import ImageTk
import pymysql


def forget_pass():
    def change_password():
        if user_entry.get()==''or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required ',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching ',parent=window)
        else:

            con = pymysql.connect(host='localhost', user='root', password='sureshsara',database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset,Please login with new password',parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window,image=bgPic)
    bgLabel.grid()

    heading_label= Label(window, text='RESET PASSWORD', font=('Arial', 19, 'bold'), bg='white')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('Arial', 12, 'bold'), bg='white',fg='black')
    userLabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), bd=0,fg='black')
    user_entry.place(x=470, y=160)

    Frame(window,width=250,height=2,bg='black').place(x=470,y=180)

    passwordLabel = Label(window, text='New Password', font=('Arial', 12, 'bold'), bg='white', fg='black')
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), bd=0, fg='black')
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='black').place(x=470, y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('Arial', 12, 'bold'), bg='white', fg='black')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, font=('Arial', 11, 'bold'), bd=0, fg='black')
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='black').place(x=470, y=340)

    submitButton=Button(window,text='Submit',font=('Arial',16,'bold '),bg='pink',fg='black'
                   ,bd=0,cursor='hand2',activebackground='white',width=19
                   ,activeforeground='black',command=change_password)
    submitButton.place(x=470,y=390)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required ')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='sureshsara')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'login is sucessful')

def main_page():
    login_window.destroy()
    import main
def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)



login_window=Tk()
login_window.geometry('990x660+70+70')
login_window.resizable(0,0)
login_window.title('LOGIN PAGE')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Arial',23,'bold'),bg='white')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window,width=25,font=('Arial',11,'bold'),bd=0)
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

Frame(login_window,width=250,height=2,bg='black').place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Arial',11,'bold'),bd=0)
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

Frame(login_window,width=250,height=2,bg='black').place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forget Password ?',bd=0,bg='white',cursor='hand2',
                    font=('Arial',9,'bold'),command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='LOGIN',font=('Arial',25,'bold'),fg='black',bg='white'
                   ,cursor='hand2',bd=0,width=13,command=login_user)

loginButton.place(x=578,y=330)


peroButton=Button(login_window,text='OPEN PERO',font=('Arial',25,'bold'),fg='black',bg='white'
                   ,cursor='hand2',bd=0,width=13,command=main_page)

peroButton.place(x=578,y=400)




signupLabel=Label(login_window,text='Dont have an account ?',font=('Arial',10,'bold')
                  ,bg='white',fg='black')
signupLabel.place(x=570,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Arial',10,'bold '),bg='white',fg='blue'
                   ,bd=0,cursor='hand2',activebackground='white'
                   ,activeforeground='blue',command=signup_page)

newaccountButton.place(x=727,y=500)




login_window.mainloop()
