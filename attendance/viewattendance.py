from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from sqlite3 import *
from tkinter import messagebox
import homestudent
import hometeacher
import login


class ViewAttendanceFrame(Frame):
    def __init__(self, parent,n):
        Frame.__init__(self, parent)
        con = connect('student.db')
        cur = con.cursor()
        query = ("select * from loginstudentdetails\n"
                 "                                   where Name = '{0}'\n"
                 "                                   ").format(n)
        cur.execute(query)
        row = cur.fetchone()
        con.close()
        self.place(relx=0.2, rely=.3, anchor=E)

        self.algo_attendance_label= Label(self, text="Algo Attendance:")
        self.algo_attendance_label.grid(row=0, column=0, pady=0)
        self.algo_attendance1_label = Label(self, text=str(row[5]),)
        self.algo_attendance1_label.grid(row=0, column=1, pady=10)

        self.os_attendance_label = Label(self, text="OS Attendance :")
        self.os_attendance_label.grid(row=1, column=0, pady=10)
        self.os_attendancel_label = Label(self, text=str(row[6]))
        self.os_attendancel_label.grid(row=1, column=1, pady=10)


        self.math_attendance_label= Label(self, text="Maths Attendance: ")
        self.math_attendance_label.grid(row=2, column=0, pady=10)
        self.math_attendance1_label = Label(self, text=str(row[7]))
        self.math_attendance1_label.grid(row=2, column=1, pady=10)

        self.evs_attendance_label= Label(self, text="EVS Attendance :")
        self.evs_attendance_label.grid(row=3, column=0, pady=10)
        self.evs_attendance1_label= Label(self, text=str(row[8]))
        self.evs_attendance1_label.grid(row=3, column=1, pady=10)


