################################################################################
#    Author: Austin Stockwell
#    Date: 03-02-2020
#    Description: This file contains all of the Tkinter frames (8 total) and
#                 each form's associated tkinter GUI objects (buttons, labels).
#                 Each form (class) also contains a call to its unique
#                 SUBMIT_x_ENTRY method that is used to retrieve the data
#                 entered on each form and pass it to the entry3.py file for
#                 further processing.
#    File: page_interface3.py
################################################################################
import mysql.connector
from tkinter import *
import tkinter as tk
from entry import *
from MenuFunctions import *
LARGE_FONT= ("Verdana", 32)
################################################################################
class StartPage(tk.Frame):
    """Creates the Main Menu with 7 buttons corresponding to the MySQL tables"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Main Menu", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        buttonAsset = tk.Button(self, text="Asset Table",
                            command=lambda: controller.show_frame(Asset))
        buttonAsset.pack()

        buttonAssetCategory = tk.Button(self, text="Asset_Category Table",
                            command=lambda: controller.show_frame(Asset_Category))
        buttonAssetCategory.pack()

        buttonBankAccount = tk.Button(self, text="Bank_Account Table",
                            command=lambda: controller.show_frame(Bank_Account))
        buttonBankAccount.pack()

        buttonBankTransaction = tk.Button(self, text="Bank_Transaction Table",
                            command=lambda: controller.show_frame(Bank_Transaction))
        buttonBankTransaction.pack()

        buttonBankTransaction = tk.Button(self, text="Credit_Card Table",
                            command=lambda: controller.show_frame(Credit_Card))
        buttonBankTransaction.pack()

        buttonBankTransaction = tk.Button(self, text="Credit_Transaction Table",
                            command=lambda: controller.show_frame(Credit_Transaction))
        buttonBankTransaction.pack()

        buttonBankTransaction = tk.Button(self, text="Liability_Category Table",
                            command=lambda: controller.show_frame(Liability_Category))
        buttonBankTransaction.pack()


################################################################################
## ENTRY FORM WINDOWS
################################################################################
class Asset(tk.Frame):
    """Creates the Asset form for data entry into Asset table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Asset Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self,text="Asset Category ID").pack()
        varAsset_fk_asset_category_ID = StringVar(self)
        varAsset_fk_asset_category_ID.set('(1) Stock') # default value
        optionAsset_fk_asset_category_ID = OptionMenu(self,
                                    varAsset_fk_asset_category_ID,
                                    '(1) Stock',
                                    '(2) Bond',
                                    '(3) Index Fund',
                                    '(4) Mutual Fund',
                                    '(5) IRA',
                                    '(6) Roth IRA',
                                    '(7) 401k',
                                    '(8) Roth 401k',
                                    '(9) CD',
                                    '(10) Commodity',
                                    '(11) Cryptocurrency',
                                    '(12) Real Estate')
        optionAsset_fk_asset_category_ID.pack()

        tk.Label(self,text="Asset Owner").pack()
        varAsset_owner = StringVar(self)
        varAsset_owner.set("Austin") # default value
        optionAsset_owner = OptionMenu(self, varAsset_owner,
                                    "Austin",
                                    "Belle",
                                    "Joint")
        optionAsset_owner.pack()

        tk.Label(self,text="Asset Name").pack()
        entryAsset_name = tk.Entry(self)
        entryAsset_name.pack()

        tk.Label(self,text="Asset Description").pack()
        entryAsset_description = tk.Entry(self)
        entryAsset_description.pack()

        tk.Label(self,text="Asset Date Acquired (yyyy-mm-dd)").pack()
        entryAsset_date_acquired = tk.Entry(self)
        entryAsset_date_acquired.pack()

        tk.Label(self,text="Asset Purchase Cost (xx.xx)").pack()
        entryAsset_purchase_cost = tk.Entry(self)
        entryAsset_purchase_cost.pack()

        buttonAssetCommit      = tk.Button(self, text = 'Submit entries to Asset table',
                            command = lambda: SUBMIT_ASSET_ENTRY())
        buttonAssetCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_ASSET_ENTRY():
            """Retrieves values entered in Asset frame"""
            print("DOING ASSETS")
            #Creates an instance (object) of the Asset_ENTRY class.
            ASSET_INPUT = Asset_ENTRY()
            ASSET_INPUT.set_asset_fk_asset_category_ID(GetAsset_AssetCategoryMenu(varAsset_fk_asset_category_ID))
            ASSET_INPUT.set_asset_owner(varAsset_owner.get())
            ASSET_INPUT.set_asset_name(entryAsset_name.get())
            ASSET_INPUT.set_asset_description(entryAsset_description.get())
            ASSET_INPUT.set_asset_date_acquired(entryAsset_date_acquired.get())
            ASSET_INPUT.set_asset_purchase_cost(entryAsset_purchase_cost.get())
            ASSET_INPUT.SUBMIT_ASSET()



######################################################################
class Asset_Category(tk.Frame):
    """Creates the Asset_Category form for data entry into Asset_Category table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Asset Category Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self,text="Asset Category Name").pack()
        entryAsset_Category_name = tk.Entry(self)
        entryAsset_Category_name.pack()

        buttonAsset_CategoryCommit = tk.Button(self, text="Submit entries to Asset_Category table",
                            command=lambda: SUBMIT_ASSET_CATEGORY_ENTRY())
        buttonAsset_CategoryCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_ASSET_CATEGORY_ENTRY():
            """Retrieves values entered in Asset_Category frame"""
            print("DOING ASSET CATEGORIES")
            ASSET_INPUT = AssetCategory_ENTRY()
            ASSET_INPUT.set_asset_category_name(entryAsset_Category_name.get())
            ASSET_INPUT.SUBMIT_ASSET_CATEGORY()



######################################################################
class Bank_Account(tk.Frame):
    """Creates the Bank_Account form for data entry into Bank_Account table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bank Account Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self,text="Bank Account Owner").pack()
        varBank_Account_owner = StringVar(self)
        varBank_Account_owner.set("Austin") # default value
        optionBank_Account_owner = OptionMenu(self,
                                    varBank_Account_owner,
                                    "Austin",
                                    "Belle",
                                    "Joint")
        optionBank_Account_owner.pack()

        tk.Label(self,text="Bank Account Type").pack()
        varBank_Account_type = StringVar(self)
        varBank_Account_type.set("Checking") # default value
        optionBank_Account_type = OptionMenu(self,
                                    varBank_Account_type,
                                    "Checking",
                                    "Saving")
        optionBank_Account_type.pack()

        tk.Label(self,text="Bank Account Brand").pack()
        entryBank_Account_brand = tk.Entry(self)
        entryBank_Account_brand.pack()

        tk.Label(self,text="Bank Account Description").pack()
        entryBank_Account_description = tk.Entry(self)
        entryBank_Account_description.pack()

        tk.Label(self,text="Bank Account Interest Rate (xx.xx)").pack()
        entryBank_Account_interest_rate = tk.Entry(self)
        entryBank_Account_interest_rate.pack()

        tk.Label(self,text="Bank Account Date Acquired (yyyy-mm-dd)").pack()
        entryBank_Account_date_acquired = tk.Entry(self)
        entryBank_Account_date_acquired.pack()

        tk.Label(self,text="Bank Account Balance (xx.xx)").pack()
        entryBank_Account_balance = tk.Entry(self)
        entryBank_Account_balance.pack()

        buttonBank_AccountCommit = tk.Button(self, text="Insert data Into Bank_Account table",
                            command=lambda: SUBMIT_BANK_ACCOUNT_ENTRY())
        buttonBank_AccountCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_BANK_ACCOUNT_ENTRY():
            """Retrieves values entered in Bank_Account frame"""
            print("DOING BANK ACCOUNTS")
            ASSET_INPUT = BankAccount_ENTRY()
            ASSET_INPUT.set_bank_account_owner(varBank_Account_owner.get())
            ASSET_INPUT.set_bank_account_type(varBank_Account_type.get())
            ASSET_INPUT.set_bank_account_brand(entryBank_Account_brand.get())
            ASSET_INPUT.set_bank_account_description(entryBank_Account_description.get())
            ASSET_INPUT.set_bank_account_interest_rate(entryBank_Account_interest_rate.get())
            ASSET_INPUT.set_bank_account_date_acquired(entryBank_Account_date_acquired.get())
            ASSET_INPUT.set_bank_account_balance(entryBank_Account_balance.get())
            ASSET_INPUT.SUBMIT_BANK_ACCOUNT()



######################################################################
class Bank_Transaction(tk.Frame):
    """Creates the Bank_Transaction form for data entry into Bank_Transaction table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bank Transaction Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self,text="Bank Account ID").pack()
        varBank_Transaction_fk_bank_account_ID = StringVar(self)
        varBank_Transaction_fk_bank_account_ID.set('(1) Austin Centier Saving')
        optionBank_Transaction_fk_bank_account_ID = tk.OptionMenu(self,
                                        varBank_Transaction_fk_bank_account_ID,
                                        '(1) Austin Centier Saving',
                                        '(2) Austin Centier Checking',
                                        '(3) Belle CHASE Saving',
                                        '(4) Joint CHASE Checking',
                                        '(5) Joint CHASE EMERGENCY SAVING')
        optionBank_Transaction_fk_bank_account_ID.pack()

        tk.Label(self,text="Bank Transaction Date (yyyy-mm-dd)").pack()
        entryBank_Transaction_date = tk.Entry(self)
        entryBank_Transaction_date.pack()

        tk.Label(self, text="Bank Transaction Description").pack()
        entryBank_Transaction_description = tk.Entry(self)
        entryBank_Transaction_description.pack()

        tk.Label(self, text="Deposit Amount (xx.xx)").pack()
        entryBank_Transaction_deposit= tk.Entry(self)
        entryBank_Transaction_deposit.pack()

        tk.Label(self,text="Asset ID").pack()
        varBank_Transaction_fk_asset_ID = StringVar(self)
        varBank_Transaction_fk_asset_ID.set("None")
        optionBank_Transaction_fk_asset_ID = OptionMenu(self,
                                                varBank_Transaction_fk_asset_ID,
                                                "None",
                                                '(1) Ethereum',
                                                '(2) Ripple')
        optionBank_Transaction_fk_asset_ID.pack()

        tk.Label(self,text="Asset Category ID").pack()
        varBank_Transaction_fk_asset_category_ID = StringVar(self)
        varBank_Transaction_fk_asset_category_ID.set("None") # default value
        optionBank_Transaction_fk_asset_category_ID = OptionMenu(self,
                                    varBank_Transaction_fk_asset_category_ID,
                                    "None",
                                    '(1) Stock',
                                    '(2) Bond',
                                    '(3) Index Fund',
                                    '(4) Mutual Fund',
                                    '(5) IRA',
                                    '(6) Roth IRA',
                                    '(7) 401k',
                                    '(8) Roth 401k',
                                    '(9) CD',
                                    '(10) Commodity',
                                    '(11) Cryptocurrency',
                                    '(12) Real Estate',
                                    '(100) Paycheck')
        optionBank_Transaction_fk_asset_category_ID.pack()

        tk.Label(self, text="Withdrawal Amount (xx.xx)").pack()
        entryBank_Transaction_withdrawal = tk.Entry(self)
        entryBank_Transaction_withdrawal.pack()

        tk.Label(self, text="Liability Category").pack()
        varBank_Transaction_fk_liability_category_ID = StringVar(self)
        varBank_Transaction_fk_liability_category_ID.set("None") # default value
        optionBank_Transaction_fk_liability_category_ID = OptionMenu(self,
                                varBank_Transaction_fk_liability_category_ID,
                                "None",
                                '(1) Rent',
                                '(2) Mortgage',
                                '(3) Water',
                                '(4) Electricity',
                                '(5) Home Insurance',
                                '(6) Trash',
                                '(7) Gas Bill',
                                '(8) Car Payment',
                                '(9) Car Insurance',
                                '(10) Gasoline',
                                '(11) Car Repairs',
                                '(12) Groceries',
                                '(13) Cellphone',
                                '(14) Wifi',
                                '(15) Bachelor Degree Loan',
                                '(16) Credit Card Payment',
                                '(17) Books',
                                '(18) Hobbies',
                                '(19) Music',
                                '(20) Restaurant',
                                '(21) Entertainment',
                                '(22) Clothing',
                                '(23) Travel',
                                '(24) Jewelery',
                                '(25) Home Improvement',
                                '(26) Self Improvement')
        optionBank_Transaction_fk_liability_category_ID.pack()

        tk.Label(self, text="Credit Card ID").pack()
        varBank_Transaction_fk_credit_card_ID = StringVar(self)
        varBank_Transaction_fk_credit_card_ID.set("None") # default value
        optionBank_Transaction_fk_credit_card_ID = OptionMenu(self,
                                        varBank_Transaction_fk_credit_card_ID,
                                        "None",
                                        '(1) Austin: Sweetwater',
                                        '(2) Austin: Discover',
                                        '(3) Austin: CHASE Freedom',
                                        '(4) Austin: Citi',
                                        '(5) Belle: CHASE Freedom')
        optionBank_Transaction_fk_credit_card_ID.pack()

        buttonBank_TransactionCommit = tk.Button(self, text="Insert data Into Bank_Transaction table",
                            command=lambda: SUBMIT_BANK_TRANSACTION_ENTRY())
        buttonBank_TransactionCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_BANK_TRANSACTION_ENTRY():
            """Retrieves values entered in Bank_Transaction frame"""
            print("DOING BANK TRANSACTIONS")
            ASSET_INPUT = BankTransaction_ENTRY()
            ASSET_INPUT.set_bank_transaction_fk_bank_account_ID(GetBankTransaction_BankAccountMenu(varBank_Transaction_fk_bank_account_ID))
            ASSET_INPUT.set_bank_transaction_date(entryBank_Transaction_date.get())
            ASSET_INPUT.set_bank_transaction_description(entryBank_Transaction_description.get())
            ASSET_INPUT.set_bank_transaction_deposit(entryBank_Transaction_deposit.get())
            ASSET_INPUT.set_bank_transaction_fk_asset_ID(GetBankTransaction_AssetMenu(varBank_Transaction_fk_asset_ID))
            ASSET_INPUT.set_bank_transaction_fk_asset_category_ID(GetBankTransaction_AssetCategoryMenu(varBank_Transaction_fk_asset_category_ID))
            ASSET_INPUT.set_bank_transaction_withdrawal(entryBank_Transaction_withdrawal.get())
            ASSET_INPUT.set_bank_transaction_fk_liability_category_ID(GetBankTransaction_LiabilityCategoryMenu(varBank_Transaction_fk_liability_category_ID))
            ASSET_INPUT.set_bank_transaction_fk_credit_card_ID(GetBankTransaction_CreditCardMenu(varBank_Transaction_fk_credit_card_ID))
            ASSET_INPUT.SUBMIT_BANK_TRANSACTION()



######################################################################
class Credit_Card(tk.Frame):
    """Creates the Credit_Card form for data entry into Credit_Card table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Credit Card Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self,text="Credit Card Holder").pack()
        varCredit_Card_owner = StringVar(self)
        varCredit_Card_owner.set("Austin") # default value
        optionCredit_Card_owner = OptionMenu(self,
                                    varCredit_Card_owner,
                                    "Austin",
                                    "Belle",
                                    "Joint")
        optionCredit_Card_owner.pack()

        tk.Label(self, text="Credit Card Brand").pack()
        entryCredit_Card_brand = tk.Entry(self)
        entryCredit_Card_brand.pack()

        tk.Label(self, text="Credit Card Description").pack()
        entryCredit_Card_description = tk.Entry(self)
        entryCredit_Card_description.pack()

        tk.Label(self, text="Credit Card Interest Rate (xx.xx)").pack()
        entryCredit_Card_interest_rate = tk.Entry(self)
        entryCredit_Card_interest_rate.pack()

        tk.Label(self, text="Credit Card Date Acquired (yyyy-mm-dd)").pack()
        entryCredit_Card_date_acquired = tk.Entry(self)
        entryCredit_Card_date_acquired.pack()

        tk.Label(self, text="Credit Card Date Expires (yyyy-mm-dd)").pack()
        entryCredit_Card_date_expires = tk.Entry(self)
        entryCredit_Card_date_expires.pack()

        tk.Label(self, text="Credit Card Balance (xx.xx)").pack()
        entryCredit_Card_balance = tk.Entry(self)
        entryCredit_Card_balance.pack()

        tk.Label(self, text="Credit Card Credit Limit (xx.xx)").pack()
        entryCredit_Card_credit_limit = tk.Entry(self)
        entryCredit_Card_credit_limit.pack()

        buttonCredit_CardCommit = tk.Button(self, text="Insert data Into Credit_Card table",
                            command=lambda: SUBMIT_CREDIT_CARD_ENTRY())
        buttonCredit_CardCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_CREDIT_CARD_ENTRY():
            """Retrieves values entered in Credit_Card frame"""
            print("DOING CREDIT CARDS")
            ASSET_INPUT = CreditCard_ENTRY()
            ASSET_INPUT.set_credit_card_owner(varCredit_Card_owner.get())
            ASSET_INPUT.set_credit_card_brand(entryCredit_Card_brand.get())
            ASSET_INPUT.set_credit_card_description(entryCredit_Card_description.get())
            ASSET_INPUT.set_credit_card_interest_rate(entryCredit_Card_interest_rate.get())
            ASSET_INPUT.set_credit_card_date_acquired(entryCredit_Card_date_acquired.get())
            ASSET_INPUT.set_credit_card_date_expires(entryCredit_Card_date_expires.get())
            ASSET_INPUT.set_credit_card_balance(entryCredit_Card_balance.get())
            ASSET_INPUT.set_credit_card_limit(entryCredit_Card_credit_limit.get())
            ASSET_INPUT.SUBMIT_CREDIT_CARD()



######################################################################
class Credit_Transaction(tk.Frame):
    """Creates the Credit_Transaction form for data entry into Credit_Transaction table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Credit Transaction Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self, text="Credit Card ID").pack()
        varCredit_Transaction_fk_credit_card_ID = StringVar(self)
        varCredit_Transaction_fk_credit_card_ID.set('(1) Austin: Sweetwater') # default value
        optionCredit_Transaction_fk_credit_card_ID = OptionMenu(self,
                                        varCredit_Transaction_fk_credit_card_ID,
                                        '(1) Austin: Sweetwater',
                                        '(2) Austin: Discover',
                                        '(3) Austin: CHASE Freedom',
                                        '(4) Austin: Citi',
                                        '(5) Belle: CHASE Freedom')
        optionCredit_Transaction_fk_credit_card_ID.pack()

        tk.Label(self, text="Credit Transaction Description").pack()
        entryCredit_Transaction_description = tk.Entry(self)
        entryCredit_Transaction_description.pack()

        tk.Label(self, text="Liability Category").pack()
        varCredit_Transaction_fk_liability_category_ID = StringVar(self)
        varCredit_Transaction_fk_liability_category_ID.set('(1) Rent') # default value
        optionCredit_Transaction_fk_liability_category_ID = OptionMenu(self,
                                varCredit_Transaction_fk_liability_category_ID,
                                '(1) Rent',
                                '(2) Mortgage',
                                '(3) Water',
                                '(4) Electricity',
                                '(5) Home Insurance',
                                '(6) Trash',
                                '(7) Gas Bill',
                                '(8) Car Payment',
                                '(9) Car Insurance',
                                '(10) Gasoline',
                                '(11) Car Repairs',
                                '(12) Groceries',
                                '(13) Cellphone',
                                '(14) Wifi',
                                '(15) Bachelor Degree Loan',
                                '(16) Credit Card Payment',
                                '(17) Books',
                                '(18) Hobbies',
                                '(19) Music',
                                '(20) Restaurant',
                                '(21) Entertainment',
                                '(22) Clothing',
                                '(23) Travel',
                                '(24) Jewelery',
                                '(25) Home Improvement',
                                '(26) Self Improvement')
        optionCredit_Transaction_fk_liability_category_ID.pack()

        tk.Label(self, text="Credit Transaction Date (yyyy-mm-dd)").pack()
        entryCredit_Transaction_charge_date = tk.Entry(self)
        entryCredit_Transaction_charge_date.pack()

        tk.Label(self, text="Credit Transaction Charge Amount (xx.xx)").pack()
        entryCredit_Transaction_charge = tk.Entry(self)
        entryCredit_Transaction_charge.pack()

        buttonCredit_TransactionCommit = tk.Button(self, text="Insert data Into Credit_Transaction table",
                            command=lambda: SUBMIT_CREDIT_TRANSACTION_ENTRY())
        buttonCredit_TransactionCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_CREDIT_TRANSACTION_ENTRY():
            """Retrieves values entered in Credit_Transaction frame"""
            print("DOING CREDIT CARDS")
            ASSET_INPUT = CreditTransaction_ENTRY()
            ASSET_INPUT.set_credit_transaction_fk_credit_card_ID(GetCreditTransaction_CreditCardMenu(varCredit_Transaction_fk_credit_card_ID))
            ASSET_INPUT.set_credit_transaction_description(entryCredit_Transaction_description.get())
            ASSET_INPUT.set_credit_transaction_fk_liability_category_ID(GetCreditTransaction_LiabilityCategoryMenu(varCredit_Transaction_fk_liability_category_ID))
            ASSET_INPUT.set_credit_transaction_charge_date(entryCredit_Transaction_charge_date.get())
            ASSET_INPUT.set_credit_transaction_charge(entryCredit_Transaction_charge.get())
            ASSET_INPUT.SUBMIT_CREDIT_TRANSACTION()



######################################################################
class Liability_Category(tk.Frame):
    """Creates the Liability_Category form for data entry into Liability_Category table"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Liability Category Table", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        # GUI OBJECTS CREATION (LABELS, BUTTONS, MENUS, ETC)
        tk.Label(self, text="Liability Category Name").pack()
        entryLiability_Category_name = tk.Entry(self)
        entryLiability_Category_name.pack()

        buttonLiability_CategoryCommit = tk.Button(self, text="Insert data Into Liability_Category table",
                            command=lambda: SUBMIT_LIABILITY_CATEGORY_ENTRY())
        buttonLiability_CategoryCommit.pack()

        button1 = tk.Button(self, text="Back to Main Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


        def SUBMIT_LIABILITY_CATEGORY_ENTRY():
            """Retrieves values entered in Liability_Category frame"""
            print("DOING LIABILITY CATEGORIES")
            ASSET_INPUT = LiabilityCategory_ENTRY()
            ASSET_INPUT.set_liability_category_name(entryLiability_Category_name.get())
            ASSET_INPUT.SUBMIT_LIABILITY_CATEGORY()
