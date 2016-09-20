###############################################################################
from tkinter import *
import tkinter.messagebox as tm



class LoginFrame(Frame):

    validLogin = False

    def __init__(self, master):
        super().__init__(master)

        self.usernameLabel = Label(self, text="Username")
        self.passwordLabel = Label(self, text="Password")

        self.usernameEntry = Entry(self)
        self.passwordEntry = Entry(self, show="*")

        self.usernameLabel.grid(row=0, sticky=E)
        self.passwordLabel.grid(row=1, sticky=E)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordEntry.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        userLoginDetails = [username, password]
        self.db = MySQLDatabase(userLoginDetails)
        validLogin = self.db.login() # Returns bool True if valid


        #sql input here instead of variables
        if username == "darrell" and password == "password":
            tm.showinfo("Login info", "Welcome darrell")
            validLogin = True

        else:
            tm.showerror("Login error", "Incorrect username or password")
            validLogin = False


#### needs to be on for GUI
root = Tk()
root.title("login")

#### brings up the frame
lf = LoginFrame(root)

#### needs to be on for GUI
root.mainloop()
