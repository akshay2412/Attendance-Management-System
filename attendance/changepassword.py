
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *
import homestudent



class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.place(relx=.5,rely=.5,anchor=CENTER)

        self.old_password_label = Label(self, text = "Old Password: ")
        self.old_password_label.grid(row=0,column=0,pady=10)

        self.old_password_entry = Entry(self,show='*')
        self.old_password_entry.grid(row=0,column=1)

        self.new_password_label = Label(self, text="New Password: ")
        self.new_password_label.grid(row=1, column=0, pady=10)

        self.new_password_entry = Entry(self, show='*')
        self.new_password_entry.grid(row=1, column=1)

        self.confirm_password_label = Label(self, text="Confirm Password: ")
        self.confirm_password_label.grid(row=2, column=0, pady=10)

        self.confirm_password_entry = Entry(self, show='*')
        self.confirm_password_entry.grid(row=2, column=1)

        self.change_password_button = Button(self, text = "Change Password",
        command = self.change_password_button_click)
        self.change_password_button.grid(row=3,column=1)


    def change_password_button_click(self):
        con = connect('teacher.db')
        cur = con.cursor()
        query = """select * from loginteacherdeatils 
        where Password = '{0}'""".format(
        self.old_password_entry.get())

        cur.execute(query)
        row = cur.fetchone()
        con.close()
        con = connect('student.db')
        cur = con.cursor()
        query1 = """select * from loginstudentdetails 
        where Password = '{0}'""".format(
        self.old_password_entry.get())
        cur.execute(query1)
        row1 = cur.fetchone()
        con.close()


        if row is not None:
            new_password = self.new_password_entry.get()
            confirm_password = self.confirm_password_entry.get()

            if new_password == confirm_password:
                con = connect('teacher.db')
                cur = con.cursor()
                query2 = """update loginteacherdeatils set Password = '{0}'
                where Password = '{1}'""".format(
                    self.new_password_entry.get(),
                    self.old_password_entry.get()
                )
                cur.execute(query2)
                con.commit()
                con.close()

                messagebox.showinfo("Success Message",
                "Your password is changed successfully")
                self.destroy()



            else:
                messagebox.showerror("Error Message",
                "New password and confirm password did not match")


        if row1 is not None:
            new_password = self.new_password_entry.get()
            confirm_password = self.confirm_password_entry.get()
            if new_password == confirm_password:
                con = connect('student.db')
                cur = con.cursor()

                query3 = """update loginstudentdetails set Password = '{0}'
                where Password = '{1}'""".format(
                    self.new_password_entry.get(),
                    self.old_password_entry.get()
                )
                cur.execute(query3)
                con.commit()
                con.close()

                messagebox.showinfo("Success Message",
                "Your password is changed successfully")
                self.destroy()



            else:
                messagebox.showerror("Error Message",
                "New password and confirm password did not match")
                self.destroy()

        else :
            messagebox.showerror("Error Message",
            "incorrect old password ")
            self.destroy()


        con.close()



