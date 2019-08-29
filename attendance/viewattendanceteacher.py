from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from sqlite3 import *
from tkinter import messagebox
import homestudent
import hometeacher
import login


class ViewAttendanceFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()
        self.style.configure('TFrame', background='white')

        self.pack(side =  TOP, fill = BOTH, expand = TRUE)

        self.con = connect('student.db')
        self.cur = self.con.cursor()

        self.create_view_all_student_frame()

    def create_view_all_student_frame(self):
        self.style.configure('TFrame', background='white')

        self.view_all_contacts_frame = Frame(self)
        self.view_all_contacts_frame.place(relx=0.5, rely=.5,
                                           anchor=CENTER)

        self.style.configure('TLabel', font=(NONE, 25))
        self.contacts_tree_view = Treeview(self.view_all_contacts_frame,
                                           columns=('col1', 'col2', 'col3', 'col4','col5','col6','col7','col8','col9'), show='headings')
        self.contacts_tree_view.grid(row=1, column=1, columnspan=3,
                                     sticky=W)
        self.contacts_tree_view.heading('col1', text='Name', anchor=W)
        self.contacts_tree_view.heading('col2', text='Roll no.',
                                        anchor=W)
        self.contacts_tree_view.heading('col3', text='Password',
                                        anchor=W)
        self.contacts_tree_view.heading('col4', text='CGPA', anchor=W)
        self.contacts_tree_view.heading('col5', text='Semester', anchor=W)
        self.contacts_tree_view.heading('col6', text='Algo Attendance',
                                        anchor=W)
        self.contacts_tree_view.heading('col7', text='Os Attendance',
                                        anchor=W)
        self.contacts_tree_view.heading('col8', text='Maths Attendance', anchor=W)
        self.contacts_tree_view.heading('col9', text='EVS Attendance', anchor=W)
        self.contacts_tree_view.column('col1', width=75)
        self.contacts_tree_view.column('col2', width=75)
        self.contacts_tree_view.column('col3', width=75)
        self.contacts_tree_view.column('col4', width=75)
        self.contacts_tree_view.column('col5', width=75)
        self.contacts_tree_view.column('col1', width=75)
        self.contacts_tree_view.column('col2', width=75)
        self.contacts_tree_view.column('col3', width=75)
        self.contacts_tree_view.column('col4', width=75)

        self.contacts_tree_view.bind('<<TreeviewSelect>>',
                                     self.tree_view_selection_changed)

        query = "select * from loginstudentdetails"
        self.fill_student_tree_view(query)

        self.con.close()

    def fill_student_tree_view(self, query):
            for record in self.contacts_tree_view.get_children():
                self.contacts_tree_view.delete(record)

            self.cur.execute(query)
            records = self.cur.fetchall()
            for record in records:
                self.contacts_tree_view.insert("", END, values=record)

    def tree_view_selection_changed(self, event):
            record = self.contacts_tree_view.item(
                self.contacts_tree_view.selection())['values']

            self.view_all_contacts_frame.destroy()
            self.create_update_delete_contact_frame(record)

