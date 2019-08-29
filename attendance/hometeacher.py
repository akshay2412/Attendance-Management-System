from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
import changepassword
import login
import hometeacher
import updateattendance
import viewattendanceteacher
a='dabb1'


class homewindow(Tk):
    def __init__(self,n, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        con = connect('teacher.db')
        cur = con.cursor()
        query = ("select * from loginteacherdeatils\n"
                 "                                   where Name = '{0}'\n"
                 "                                   ").format(n)
        cur.execute(query)
        row = cur.fetchone()
        con.close()

        self.geometry("3000x3000")
        self.title("Home Teacher")

        self.style = Style()

        self.style.configure('Header.TFrame', background='gold')

        self.header_frame = Frame(self, style='Header.TFrame')
        self.header_frame.pack(side=TOP, fill=X)

        self.style.configure('Header.TLabel', background='gold',
                             foreground='black', font=(None, 25))
        s=row[0]

        self.header_label = Label(self.header_frame,
                                  text="Welcome  "+s+" !!", style='Header.TLabel')
        self.header_label.pack(pady=10)

        self.style.configure('Navigation.TFrame', background='ivory3')

        self.navigation_frame = Frame(self, style='Navigation.TFrame',
                                      width=150)
        self.navigation_frame.pack(side=RIGHT, fill=Y)

        self.style.configure('Navigation.TButton', font=(NONE, 10))

        self.update_button = Button(self.navigation_frame,
                                             text="Update Attendance", style='Navigation.TButton',
                                             width=20, command=self.update_button_click)
        self.update_button.pack(ipady=10)

        self.view_attendance_button = Button(self.navigation_frame,
                                             text="View Attendance", style='Navigation.TButton',
                                             width=20, command=self.view_attendance_button_click)
        self.view_attendance_button.pack(ipady=10)

        self.change_password_button = Button(self.navigation_frame,
                                             text="Change Password", style='Navigation.TButton',
                                             width=20, command=self.change_password_button_click)
        self.change_password_button.pack(ipady=10)
        self.back_button = Button(self.navigation_frame,
                                  text="Back", style='Navigation.TButton',
                                  width=20, command=self.back_button_click)
        self.back_button.pack(ipady=10)

        self.logout_button = Button(self.navigation_frame,
                                    text="Logout", style='Navigation.TButton', width=20,
                                    command=self.logout_button_click)
        self.logout_button.pack(ipady=10)






        self.style.configure('Content.TFrame', background='white')

        self.content_frame = Frame(self, style='Content.TFrame')
        self.content_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

        self.style.configure('Login.TFrame', background='white')
        self.login_frame = Frame(self.content_frame, style='Login.TFrame')
        self.login_frame.place(relx=0, rely=.5, anchor=SW)

        self.style.configure('Login.TLabel', font=('None', 25),
                             background='white')

        self.username_label = Label(self.login_frame, text="NAME:",
                                    style='Login.TLabel')
        self.username_label.grid(row=0, column=0, pady=0)
        self.name_label = Label(self.login_frame, text=str(row[0]),
                                style='Login.TLabel')
        self.name_label.grid(row=0, column=1, pady=10)


        self.password_label = Label(self.login_frame, text="PASSWORD: ",
                                    style='Login.TLabel')
        self.password_label.grid(row=2, column=0, pady=10)
        self.password1_label = Label(self.login_frame, text=str(row[1]),
                                     style='Login.TLabel')
        self.password1_label.grid(row=2, column=1, pady=10)

        self.subject_label = Label(self.login_frame, text="SUBJECT :",
                                style='Login.TLabel')
        self.subject_label.grid(row=3, column=0, pady=10)
        self.subject1_label = Label(self.login_frame, text=str(row[2]),
                                 style='Login.TLabel')
        self.subject1_label.grid(row=3, column=1, pady=10)

        self.joining_year_label = Label(self.login_frame, text="JOINING YEAR :",
                                    style='Login.TLabel')
        self.joining_year_label.grid(row=4, column=0, pady=10)
        self.joining_year1_label = Label(self.login_frame, text=str(row[3]),
                                     style='Login.TLabel')
        self.joining_year1_label.grid(row=4, column=1, pady=10)


        self.phone_number_label = Label(self.login_frame, text="PHONE :",
                                       style='Login.TLabel')
        self.phone_number_label.grid(row=5, column=0, pady=10)
        self.phone_number1_label = Label(self.login_frame, text=str(row[4]),
                                        style='Login.TLabel')
        self.phone_number1_label.grid(row=5, column=1, pady=10)
        global a
        a=n


    def view_attendance_button_click(self):
        global a
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        viewattendanceteacher.ViewAttendanceFrame(self.content_frame)

    def back_button_click(self):
        global a
        self.destroy()
        hometeacher.homewindow(a)

    def change_password_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        changepassword.ChangePasswordFrame(self.content_frame)

    def logout_button_click(self):
        self.destroy()
        login.LoginWindow()

    def update_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        updateattendance.UpdateAttendanceFrame(self.content_frame)




