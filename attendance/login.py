from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from sqlite3 import *
from tkinter import messagebox
import homestudent
import hometeacher

n = 'Sunny'


class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Login Page")
        self.geometry("600x415")

        self.style = Style()
        self.style.configure('Header.TFrame', background='goldenrod1')

        self.header_frame = Frame(self, style='Header.TFrame')
        self.header_frame.pack(side=TOP, fill=X)

        self.style.configure('Header.TLabel', font=('None', 20),
                             background='goldenrod1', foreground='black')

        self.header_label = Label(self.header_frame, text="Jaypee Institute of Information technology",
                                  style='Header.TLabel')
        self.header_label.pack(pady=10)
        self.style.configure('Content.TFrame', background='MistyRose2')
        self.content_frame = Frame(self, style='Content.TFrame')
        self.content_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.style.configure('Photo.TFrame', background='blue')
        load = Image.open("jiit.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.content_frame, image=render)
        img.image = render
        img.place(x=1, y=1)



        self.style.configure('Login.TFrame', background='red')
        self.login_frame = Frame(self.content_frame, style='Login.TFrame')
        self.login_frame.place(relx=.9, rely=.5, anchor=SE)

        self.style.configure('Login.TLabel', font=('None', 10),
                             background='white')

        self.username_label = Label(self.login_frame, text="Username: ",
                                    style='Login.TLabel')
        self.username_label.grid(row=0, column=0, pady=10)

        self.username_entry = Entry(self.login_frame, font=('None', 10))
        self.username_entry.grid(row=0, column=1)
        self.username_entry.focus()

        self.password_label = Label(self.login_frame, text="Password: ",
                                    style='Login.TLabel')
        self.password_label.grid(row=1, column=0, pady=10)

        self.password_entry = Entry(self.login_frame, font=('None', 10),
                                    show='*')
        self.password_entry.grid(row=1, column=1)
        b = IntVar()
        b.set(1)
        teacher_radiobutton = Radiobutton(self.login_frame, text='Teacher', value=1, variable=b)
        teacher_radiobutton.grid(row=2, column=0)
        student_radiobutton = Radiobutton(self.login_frame, text='Student', value=2, variable=b)
        student_radiobutton.grid(row=2, column=1)

        def login_button_click():

            n = self.username_entry.get()
            if b.get() == 1:
                con = connect('teacher.db')
                cur = con.cursor()
                query = """select * from loginteacherdeatils
                    where Name = '{0}'
                    and Password = '{1}'""".format(
                    self.username_entry.get(),
                    self.password_entry.get())
                cur.execute(query)

                row = cur.fetchone()
                con.close()
                if row is not None:
                    self.destroy()
                    hometeacher.homewindow(n)
                else:
                    messagebox.showerror("Login Error",
                                         "Invalid username/password")
            if b.get() == 2:
                con = connect('student.db')
                cur = con.cursor()
                query = """select * from loginstudentdetails
                                      where Name = '{0}'
                                      and Password = '{1}'""".format(
                    self.username_entry.get(),
                    self.password_entry.get())
                cur.execute(query)

                row = cur.fetchone()
                con.close()
                if row is not None:
                    self.destroy()
                    homestudent.homewindow(n)
                else:
                    messagebox.showerror("Login Error",
                                         "Invalid username/password")

        self.login_button = Button(self.login_frame, text="Login",
                                   style='Login.TButton', command=login_button_click)
        self.login_button.grid(row=3, column=1, pady=10)
        self.login_button.bind('<Return>', login_button_click)


if __name__ == '__main__':
    login_window = LoginWindow()

    login_window.mainloop()
