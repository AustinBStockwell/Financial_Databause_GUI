################################################################################
#    Author: Austin Stockwell
#    Date: 03-02-2020
#    Description: Data entry program for Stockwell_Financial MySQL database.
#    File: V3_GUI_Shell.py
################################################################################
import mysql.connector
from tkinter import *
import tkinter as tk
from page_interface import *
LARGE_FONT = ("Verdana", 32)
################################################################################
class Stockwell_FinancialApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Asset, Asset_Category, Bank_Account,
                    Bank_Transaction, Credit_Card, Credit_Transaction,
                    Expense_Category, Investment_Account):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

################################################################################
## RUN APPLICATION
################################################################################
app = Stockwell_FinancialApp()
app.mainloop()
