from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *
import hometeacher

class UpdateAttendanceFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.place(relx=.5, rely=.5, anchor=CENTER)

        self.name_label = Label(self, text="Name: ")
        self.name_label.grid(row=0, column=0, pady=10)

        self.name_entry = Entry(self, font=('None', 10))
        self.name_entry.grid(row=0, column=1)
        self.name_entry.focus()
        self.percentage_label = Label(self, text="Percentage: ")
        self.percentage_label.grid(row=1, column=0, pady=10)

        self.percentage_entry = Entry(self, font=('None', 10))
        self.percentage_entry.grid(row=1, column=1)
        self.percentage_entry.focus()

        self.subject_label = Label(self, text="Subject: ")
        self.subject_label.grid(row=2, column=0, pady=10)

        self.subject_entry = Entry(self, font=('None', 10))
        self.subject_entry.grid(row=2, column=1)
        self.subject_entry.focus()


        self.login_button = Button(self, text="Submit",
                                   command=self.update_attendance_button_click)
        self.login_button.grid(row=3, column=1, pady=10)
        self.login_button.bind('<Return>', self.update_attendance_button_click)

    def update_attendance_button_click(self):
        con = connect('student.db')
        cur = con.cursor()
        query = """UPDATE loginstudentdetails 
                    SET '{0}'='{1}'
                where Name = '{2}'""".format(
            self.subject_entry.get(),
            self.percentage_entry.get(),
            self.name_entry.get())

        cur.execute(query)
        con.commit()
        messagebox.showinfo("Success Message",
                            "Your Attendance has been updated successfully")
        self.destroy()
        con.close()