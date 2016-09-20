from tkinter import *
from tkinter import ttk
import GUIlogin
import GUImain


class main():
    GUIlogin.LoginFrame(Frame)
    if GUIlogin.validLogin:
        GUImain.MainFrame(Frame)
        GUIMain.main()
