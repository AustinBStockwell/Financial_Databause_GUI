################################################################################
#    Author: Austin Stockwell
#    Date: 03-02-2020
#    Description: This file contains classes that are used to enter the data
#                 into the MySQL database.  Each class corresponds to a seperate
#                 table in the database (7 total).
#                 Each class contains:
#                       0) Declaration of all GUI menu variables in each table
#                          as x_ENTRY class attributes.
#                       1) Accessors and Mutators to get and set the values of
#                           the associated GUI menu variables in page_interface
#                           file
#                       2) A message box that declares the entered values and
#                           confirms entry success / failure (with error code)
#                       3) Connection to MySQL database
#                       4) INSERT statement to enter data to associated table.
#    File: entry.py
################################################################################
import numpy as np
import mysql.connector
from tkinter import *
from tkinter import messagebox
################################################################################
class Asset_ENTRY():
    def __init__(self):
        self.entryAsset_fk_asset_category_ID = np.nan
        self.entryAsset_owner                = np.nan
        self.entryAsset_name                 = np.nan
        self.entryAsset_description          = np.nan
        self.entryAsset_purchase_date        = np.nan
        self.entryAsset_purchase_price       = np.nan
        self.entryAsset_sell_date            = np.nan
        self.entryAsset_sell_price           = np.nan
        return

    #### Accessors and Mutators
    def set_asset_fk_asset_category_ID(self, input):
        self.entryAsset_fk_asset_category_ID = input
        return

    def set_asset_owner(self, input):
        self.entryAsset_owner = input
        return

    def set_asset_name(self, input):
        self.entryAsset_name = input
        return

    def set_asset_description(self, input):
        self.entryAsset_description = input
        return

    def set_asset_purchase_date(self, input):
        self.entryAsset_date_acquired = input
        return

    def set_asset_purchase_price(self, input):
        self.entryAsset_purchase_cost = input
        return

    def set_asset_sell_date(self, input):
        self.entryAsset_sell_date = input
        return

    def set_asset_sell_price(self, input):
        self.entryAsset_sell_price = input
        return

    ######################################################################

    def get_asset_fk_asset_cateogry_ID(self):

        return self.entryAsset_fk_asset_category_ID

    def get_asset_owner(self):

        return self.entryAsset_owner

    def get_asset_name(self):

        return self.entryAsset_name

    def get_asset_description(self):

        return self.entryAsset_description

    def get_asset_purchase_date(self):

        return self.entryAsset_purchase_date

    def get_asset_purchase_price(self):

        return self.entryAsset_purchase_price

    def get_asset_sell_date(self):

        return self.entryAsset_sell_date

    def get_asset_sell_price(self):

        return self.entryAsset_sell_price

    ######################################################################

    def SUBMIT_ASSET(self):
        #Print user input from form to console
        print(self.get_asset_fk_asset_cateogry_ID(),
              self.get_asset_owner(),
              self.get_asset_name(),
              self.get_asset_description(),
              self.get_asset_purchase_date(),
              self.get_asset_purchase_price(),
              self.get_asset_sell_date(),
              self.get_asset_sell_price()
              )

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Asset Category: " + self.entryAsset_fk_asset_category_ID
        warningMessage += "\nAsset Owner: " + self.entryAsset_owner
        warningMessage += "\nAsset Name: " + self.entryAsset_name
        warningMessage += "\nAsset Description: " + self.entryAsset_description
        warningMessage += "\nPurchase Date: " + self.entryAsset_purchase_date
        warningMessage += "\nPurchase Price: " + self.entryAsset_purchase_cost
        warningMessage += "\nSell Date: " + self.entryAsset_purchase_date
        warningMessage += "\nSell Price: " + self.entryAsset_purchase_cost
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Asset Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            mySql_insert_query = """INSERT INTO Asset (idAsset,
                                                      fk_asset_category_ID,
                                                      owner,
                                                      name,
                                                      description,
                                                      date_acquired,
                                                      purchase_cost,
                                                      sell_date,
                                                      sell_price)
                                   VALUES
                                   (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL, NULL)""" % (str(self.get_asset_fk_asset_cateogry_ID()),
                                                                                str(self.get_asset_owner()),
                                                                                str(self.get_asset_name()),
                                                                                str(self.get_asset_description()),
                                                                                str(self.get_asset_purchase_date()),
                                                                                str(self.get_asset_purchase_price()),
                                                                                str(self.get_asset_sell_date()),
                                                                                str(self.get_asset_sell_price())
                                                                                )
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Asset table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Asset table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Asset table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return


################################################################################
class AssetCategory_ENTRY():
    def __init__(self):
        self.entryAsset_Category_name = np.nan
        return

    #### Accessors and Mutators are legit
    def set_asset_category_name(self, input):
        self.entryAsset_Category_name = input
        return

    ######################################################################

    def get_asset_category_name(self):

        return self.entryAsset_Category_name

    ######################################################################

    def SUBMIT_ASSET_CATEGORY(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_asset_category_name())

        #POPUP CONFIRMATION WINDOW
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Asset_Category Entry',
        'Category Name: ' + self.entryAsset_Category_name)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            mySql_insert_query = """INSERT INTO Asset_Category (idAsset_Category, name)
                                   VALUES
                                   (NULL, '%s')""" % (str(self.get_asset_category_name()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Asset_Category table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Asset Category table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Asset_Category table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return


################################################################################
class BankAccount_ENTRY():
    def __init__(self):
        self.entryBank_Account_owner                = np.nan
        self.entryBank_Account_type                 = np.nan
        self.entryBank_Account_bank_name            = np.nan
        self.entryBank_Account_account_number       = np.nan
        self.entryBank_Account_description          = np.nan
        self.entryBank_Account_interest_rate        = np.nan
        self.entryBank_Account_balance              = np.nan
        return

    #### Accessors and Mutators
    def set_bank_account_owner(self, input):
        self.entryBank_Account_owner = input
        return

    def set_bank_account_type(self, input):
        self.entryBank_Account_type  = input
        return

    def set_bank_account_bank_name(self, input):
        self.entryBank_Account_bank_name = input
        return

    def set_bank_account_account_number(self, input):
        self.entryBank_Account_account_number  = input
        return

    def set_bank_account_description(self, input):
        self.entryBank_Account_description = input
        return

    def set_bank_account_interest_rate(self, input):
        self.entryBank_Account_interest_rate = input
        return

    def set_bank_account_balance(self, input):
        self.entryBank_Account_balance = input
        return

    ######################################################################

    def get_bank_account_owner(self):

        return self.entryBank_Account_owner

    def get_bank_account_type(self):

        return self.entryBank_Account_type

    def get_bank_account_brand(self):

        return self.entryBank_Account_bank_name

    def get_bank_account_description(self):

        return self.entryBank_Account_description

    def get_bank_account_interest_rate(self):

        return self.entryBank_Account_interest_rate

    def get_bank_account_date_acquired(self):

        return self.entryBank_Account_date_acquired

    def get_bank_account_balance(self):

        return self.entryBank_Account_balance

    ######################################################################

    def SUBMIT_BANK_ACCOUNT(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_bank_account_owner(),
              self.get_bank_account_type(),
              self.get_bank_account_brand(),
              self.get_bank_account_description(),
              self.get_bank_account_interest_rate(),
              self.get_bank_account_date_acquired(),
              self.get_bank_account_balance())

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Bank Account Owner: " + self.entryBank_Account_owner
        warningMessage += "\nBank Account Type: " + self.entryBank_Account_type
        warningMessage += "\nBank Account Brand: " + self.entryBank_Account_bank_name
        warningMessage += "\nBank Account Description: " + self.entryBank_Account_description
        warningMessage += "\nInterest Rate: " + self.entryBank_Account_interest_rate
        warningMessage += "\nDate Acquired: " + self.entryBank_Account_date_acquired
        warningMessage += "\nAcount Balance: " + self.entryBank_Account_balance
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Bank Account Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            mySql_insert_query = """INSERT INTO Bank_Account (idBank_Account, owner,
                                                            type, brand, description,
                                                            interest_rate, date_acquired,
                                                            balance)
                                       VALUES
                                       (NULL, '%s', '%s', '%s', '%s', '%s', '%s','%s') """ % (str(self.get_bank_account_owner()),
                                                                                        str(self.get_bank_account_type()),
                                                                                        str(self.get_bank_account_brand()),
                                                                                        str(self.get_bank_account_description()),
                                                                                        str(self.get_bank_account_interest_rate()),
                                                                                        str(self.get_bank_account_date_acquired()),
                                                                                        str(self.get_bank_account_balance()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Bank_Account table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Bank Account table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Bank_Account table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return


################################################################################
class BankTransaction_ENTRY():
    def __init__(self):
        self.entryBank_Transaction_fk_bank_account_ID                = np.nan
        self.entryBank_Transaction_date                              = np.nan
        self.entryBank_Transaction_description                       = np.nan
        self.entryBank_Transaction_deposit                           = np.nan
        self.entryBank_Transaction_fk_asset_ID                       = np.nan
        self.entryBank_Transaction_fk_asset_category_ID              = np.nan
        self.entryBank_Transaction_withdrawal                        = np.nan
        self.entryBank_Transaction_fk_expense_category_ID          = np.nan
        self.entryBank_Transaction_fk_credit_card_ID                 = np.nan
        return

    #### Accessors and Mutators
    def set_bank_transaction_fk_bank_account_ID(self, input):
        self.entryBank_Transaction_fk_bank_account_ID = input
        return

    def set_bank_transaction_date(self, input):
        self.entryBank_Transaction_date  = input
        return

    def set_bank_transaction_description(self, input):
        self.entryBank_Transaction_description = input
        return

    def set_bank_transaction_deposit(self, input):
        self.entryBank_Transaction_deposit = input
        return

    def set_bank_transaction_fk_asset_category_ID(self, input):
        self.entryBank_Transaction_fk_asset_category_ID = input
        return

    def set_bank_transaction_withdrawal(self, input):
        self.entryBank_Transaction_withdrawal = input
        return

    def set_bank_transaction_fk_expense_category_ID(self, input):
        self.entryBank_Transaction_fk_expense_category_ID = input
        return

    def set_bank_transaction_fk_credit_card_ID(self, input):
        self.entryBank_Transaction_fk_credit_card_ID = input
        return

    ######################################################################

    def get_bank_transaction_fk_bank_account_ID(self):

        return self.entryBank_Transaction_fk_bank_account_ID

    def get_bank_transaction_date(self):

        return self.entryBank_Transaction_date

    def get_bank_transaction_description(self):

        return self.entryBank_Transaction_description

    def get_bank_transaction_deposit(self):

        return self.entryBank_Transaction_deposit

    def get_bank_transaction_fk_asset_ID(self):

        return self.entryBank_Transaction_fk_asset_ID

    def get_bank_transaction_fk_asset_category_ID(self):

        return self.entryBank_Transaction_fk_asset_category_ID

    def get_bank_transaction_withdrawal(self):

        return self.entryBank_Transaction_withdrawal

    def get_bank_transaction_fk_expense_category_ID(self):

        return self.entryBank_Transaction_fk_expense_category_ID

    def get_bank_transaction_fk_credit_card_ID(self):

        return self.entryBank_Transaction_fk_credit_card_ID

    ######################################################################
    def SUBMIT_BANK_TRANSACTION(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_bank_transaction_fk_bank_account_ID(),
              self.get_bank_transaction_date(),
              self.get_bank_transaction_description(),
              self.get_bank_transaction_deposit(),
              self.get_bank_transaction_fk_asset_ID(),
              self.get_bank_transaction_fk_asset_category_ID(),
              self.get_bank_transaction_withdrawal(),
              self.get_bank_transaction_fk_expense_category_ID(),
              self.get_bank_transaction_fk_credit_card_ID())

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Bank Account ID: " + self.entryBank_Transaction_fk_bank_account_ID
        warningMessage += "\nTransacction Date: " + self.entryBank_Transaction_date
        warningMessage += "\nTransaction Description: " + self.entryBank_Transaction_description
        warningMessage += "\nDeposit: " + self.entryBank_Transaction_deposit
        warningMessage += "\nAsset ID: " + self.entryBank_Transaction_fk_asset_ID
        warningMessage += "\nAsset Category ID: " + self.entryBank_Transaction_fk_asset_category_ID
        warningMessage += "\nWithdrawal: " + self.entryBank_Transaction_withdrawal
        warningMessage += "\nExpense Category ID: " + self.entryBank_Transaction_fk_expense_category_ID
        warningMessage += "\nCredit Card ID: " + self.entryBank_Transaction_fk_credit_card_ID
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Bank Transaction Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            #THIS IS ENTERING WITHDRAWALS
            if(self.entryBank_Transaction_fk_asset_ID == "None") & (self.entryBank_Transaction_fk_asset_category_ID == "None"):
                    mySql_insert_query = """INSERT INTO Bank_Transaction (idBank_Transaction,
                                                fk_bank_account_ID, date, description, deposit,
                                                fk_asset_ID, fk_asset_category_ID, withdrawal,
                                                fk_expense_category_ID, fk_credit_card_ID)
                                               VALUES
                                               (NULL, '%s', '%s', '%s', 00.00, NULL, NULL, '%s', '%s', '%s') """ % (str(self.get_bank_transaction_fk_bank_account_ID()),
                                                                                                str(self.get_bank_transaction_date()),
                                                                                                str(self.get_bank_transaction_description()),
                                                                                                str(self.get_bank_transaction_withdrawal()),
                                                                                                str(self.get_bank_transaction_fk_expense_category_ID()),
                                                                                                str(self.get_bank_transaction_fk_credit_card_ID()))
            if(self.entryBank_Transaction_fk_asset_ID == "None") & (self.entryBank_Transaction_fk_asset_category_ID == "None") & (self.entryBank_Transaction_fk_credit_card_ID == "None"):
                    mySql_insert_query = """INSERT INTO Bank_Transaction (idBank_Transaction,
                                                fk_bank_account_ID, date, description, deposit,
                                                fk_asset_ID, fk_asset_category_ID, withdrawal,
                                                fk_expense_category_ID, fk_credit_card_ID)
                                               VALUES
                                               (NULL, '%s', '%s', '%s', 00.00, NULL, NULL, '%s', '%s', NULL) """ % (str(self.get_bank_transaction_fk_bank_account_ID()),
                                                                                                str(self.get_bank_transaction_date()),
                                                                                                str(self.get_bank_transaction_description()),
                                                                                                str(self.get_bank_transaction_withdrawal()),
                                                                                                str(self.get_bank_transaction_fk_expense_category_ID()))
            #THIS IS ENTERING DEPOSITS
            if(self.entryBank_Transaction_fk_expense_category_ID == "None") & (self.entryBank_Transaction_fk_credit_card_ID == "None"):
                    mySql_insert_query = """INSERT INTO Bank_Transaction (idBank_Transaction,
                                                    fk_bank_account_ID, date, description, deposit,
                                                    fk_asset_ID, fk_asset_category_ID, withdrawal,
                                                    fk_expense_category_ID, fk_credit_card_ID)
                                                   VALUES
                                                   (NULL, '%s', '%s', '%s', '%s', '%s', '%s', 00.00, NULL, NULL) """ % (str(self.get_bank_transaction_fk_bank_account_ID()),
                                                                                                    str(self.get_bank_transaction_date()),
                                                                                                    str(self.get_bank_transaction_description()),
                                                                                                    str(self.get_bank_transaction_deposit()),
                                                                                                    str(self.get_bank_transaction_fk_asset_ID()),
                                                                                                    str(self.get_bank_transaction_fk_asset_category_ID()))
            if(self.entryBank_Transaction_fk_expense_category_ID == "None") & (self.entryBank_Transaction_fk_credit_card_ID == "None") & (self.entryBank_Transaction_fk_asset_ID == "None"):
                    mySql_insert_query = """INSERT INTO Bank_Transaction (idBank_Transaction,
                                                    fk_bank_account_ID, date, description, deposit,
                                                    fk_asset_ID, fk_asset_category_ID, withdrawal,
                                                    fk_expense_category_ID, fk_credit_card_ID)
                                                   VALUES
                                                   (NULL, '%s', '%s', '%s', '%s', NULL, '%s', 00.00, NULL, NULL) """ % (str(self.get_bank_transaction_fk_bank_account_ID()),
                                                                                                    str(self.get_bank_transaction_date()),
                                                                                                    str(self.get_bank_transaction_description()),
                                                                                                    str(self.get_bank_transaction_deposit()),
                                                                                                    str(self.get_bank_transaction_fk_asset_category_ID()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Bank_Transaction table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Bank Transaction table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Bank_Transaction table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return


################################################################################
class CreditCard_ENTRY():
    def __init__(self):
        self.entryCredit_Card_owner                 = np.nan
        self.entryCredit_Card_brand                 = np.nan
        self.entryCredit_Card_description           = np.nan
        self.entryCredit_Card_interest_rate         = np.nan
        self.entryCredit_Card_date_acquired         = np.nan
        self.entryCredit_Card_date_expires          = np.nan
        self.entryCredit_Card_balance               = np.nan
        self.entryCredit_Card_credit_limit          = np.nan
        return

    #### Accessors and Mutators
    def set_credit_card_owner(self, input):
        self.entryCredit_Card_owner = input
        return

    def set_credit_card_brand(self, input):
        self.entryCredit_Card_brand  = input
        return

    def set_credit_card_description(self, input):
        self.entryCredit_Card_description = input
        return

    def set_credit_card_interest_rate(self, input):
        self.entryCredit_Card_interest_rate = input
        return

    def set_credit_card_balance(self, input):
        self.entryCredit_Card_balance = input
        return

    def set_credit_card_limit(self, input):
        self.entryCredit_Card_credit_limit = input
        return

    ######################################################################

    def get_credit_card_owner(self):

        return self.entryCredit_Card_owner

    def get_credit_card_brand(self):

        return self.entryCredit_Card_brand

    def get_credit_card_description(self):

        return self.entryCredit_Card_description

    def get_credit_card_interest_rate(self):

        return self.entryCredit_Card_interest_rate

    def get_credit_card_date_acquired(self):

        return self.entryCredit_Card_date_acquired

    def get_credit_card_date_expires(self):

        return self.entryCredit_Card_date_expires

    def get_credit_card_balance(self):

        return self.entryCredit_Card_balance

    def get_credit_card_credit_limit(self):

        return self.entryCredit_Card_credit_limit

    ######################################################################
    def SUBMIT_CREDIT_CARD(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_credit_card_owner(),
              self.get_credit_card_brand(),
              self.get_credit_card_description(),
              self.get_credit_card_interest_rate(),
              self.get_credit_card_date_acquired(),
              self.get_credit_card_date_expires(),
              self.get_credit_card_balance(),
              self.get_credit_card_credit_limit())

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Credit Card Owner: " + self.entryCredit_Card_owner
        warningMessage += "\nCredit Card Brand:  " + self.entryCredit_Card_brand
        warningMessage += "\nCredit Card Description : " + self.entryCredit_Card_description
        warningMessage += "\nCredit Card Interest Rate: " + self.entryCredit_Card_interest_rate
        warningMessage += "\nDate Acquired: " + self.entryCredit_Card_date_acquired
        warningMessage += "\nDate Expires: " + self.entryCredit_Card_date_expires
        warningMessage += "\nCard Balance: " + self.entryCredit_Card_balance
        warningMessage += "\nCredit Limit: " + self.entryCredit_Card_credit_limit
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Credit Card Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            mySql_insert_query = """INSERT INTO Credit_Card (idCredit_Card,
                                        owner, brand, description, interest_rate,
                                        date_acquired, date_expires, balance,
                                        credit_limit)
                                       VALUES
                                       (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') """ % (str(self.get_credit_card_owner()),
                                                                                        str(self.get_credit_card_brand()),
                                                                                        str(self.get_credit_card_description()),
                                                                                        str(self.get_credit_card_interest_rate()),
                                                                                        str(self.get_credit_card_date_acquired()),
                                                                                        str(self.get_credit_card_date_expires()),
                                                                                        str(self.get_credit_card_balance()),
                                                                                        str(self.get_credit_card_credit_limit()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Credit_Card table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Credit Card table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Credit_Card table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return


################################################################################
class CreditTransaction_ENTRY():
    def __init__(self):
        self.entryCredit_Transaction_fk_credit_card_ID           = np.nan
        self.entryCredit_Transaction_description                 = np.nan
        self.entryCredit_Transaction_fk_expense_category_ID      = np.nan
        self.entryCredit_Transaction_charge_date                 = np.nan
        self.entryCredit_Transaction_charge                      = np.nan
        return

    #### Accessors and Mutators
    def set_credit_transaction_fk_credit_card_ID(self, input):
        self.entryCredit_Transaction_fk_credit_card_ID = input
        return

    def set_credit_transaction_description(self, input):
        self.entryCredit_Transaction_description  = input
        return

    def set_credit_transaction_fk_expense_category_ID(self, input):
        self.entryCredit_Transaction_fk_expense_category_ID = input
        return

    def set_credit_transaction_charge_date(self, input):
        self.entryCredit_Transaction_charge_date = input
        return

    def set_credit_transaction_charge(self, input):
        self.entryCredit_Transaction_charge = input
        return

    ######################################################################

    def get_credit_transaction_fk_credit_card_ID(self):

        return self.entryCredit_Transaction_fk_credit_card_ID

    def get_credit_transaction_description(self):

        return self.entryCredit_Transaction_description

    def get_credit_transaction_fk_expense_category_ID(self):

        return self.entryCredit_Transaction_fk_expense_category_ID

    def get_credit_transaction_charge_date(self):

        return self.entryCredit_Transaction_charge_date

    def get_credit_transaction_charge(self):

        return self.entryCredit_Transaction_charge

    ######################################################################
    def SUBMIT_CREDIT_TRANSACTION(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_credit_transaction_fk_credit_card_ID(),
              self.get_credit_transaction_description(),
              self.get_credit_transaction_fk_expense_category_ID(),
              self.get_credit_transaction_charge_date(),
              self.get_credit_transaction_charge())

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Credit Card ID: " + self.entryCredit_Transaction_fk_credit_card_ID
        warningMessage += "\nCredit Transaction Description:  " + self.entryCredit_Transaction_description
        warningMessage += "\nExpense Category: " + self.entryCredit_Transaction_fk_expense_category_ID
        warningMessage += "\nTransaction Date: " + self.entryCredit_Transaction_charge_date
        warningMessage += "\nCharge Amount: " + self.entryCredit_Transaction_charge
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Credit Transaction Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')


            mySql_insert_query = """INSERT INTO Credit_Transaction (idCredit_Transaction,
                                        fk_credit_card_ID, description,
                                        fk_expense_category_ID, charge_date, charge)
                                       VALUES
                                       (NULL, '%s', '%s', '%s', '%s', '%s') """ % (str(self.get_credit_transaction_fk_credit_card_ID()),
                                                                                        str(self.get_credit_transaction_description()),
                                                                                        str(self.get_credit_transaction_fk_expense_category_ID()),
                                                                                        str(self.get_credit_transaction_charge_date()),
                                                                                        str(self.get_credit_transaction_charge()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Credit_Transaction table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Credit Transaction table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Credit_Transaction table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return


################################################################################
class ExpenseCategory_ENTRY():
    def __init__(self):
        self.entryExpense_Category_name = np.nan
        return

    #### Accessors and Mutators are legit
    def set_expense_category_name(self, input):
        self.entryExpense_Category_name = input
        return

    ######################################################################

    def get_expense_category_name(self):

        return self.entryInvestment_Account_name

    ######################################################################

    def SUBMIT_EXPENSE_CATEGORY(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_expense_category_name())

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Expense Category Name: " + self.entryExpense_Category_name
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Expense Category Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            mySql_insert_query = """INSERT INTO Expense_Category (idExpense_Category,
                                        name)
                                       VALUES
                                       (NULL, '%s') """ % (str(self.get_expense_category_name()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Expense_Category table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Expense Category table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Expense_Category table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return



################################################################################
class InvestmentAccount_ENTRY():
    def __init__(self):
        self.entryInvestment_Account_owner          = np.nan
        self.entryInvestment_Account_institution    = np.nan
        self.entryInvestment_Account_type           = np.nan      
        self.entryInvestment_Account_date_opened    = np.nan
        self.entryInvestment_Account_balance        = np.nan        
        return

    #### Accessors and Mutators are legit
    def set_investment_account_owner(self, input):
        self.entryInvestment_Account_owner = input
        return

    def set_investment_account_institution(self, input):
        self.entryInvestment_Account_institution = input
        return

    def set_investment_account_type(self, input):
        self.entryInvestment_Account_type = input
        return

    def set_investment_account_date_opened(self, input):
        self.entryInvestment_Account_date_opened = input
        return

    def set_investment_account_balance(self, input):
        self.entryInvestment_Account_balance = input
        return

    ######################################################################
    
    def get_investment_account_owner(self):
        return self.entryInvestment_Account_owner

    def get_investment_account_institution(self):
        return self.entryInvestment_Account_institution

    def get_investment_account_type(self):
        return self.entryInvestment_Account_type

    def get_investment_account_date_opened(self):
        return self.entryInvestment_Account_date_opened

    def get_investment_account_balance(self):
        return self.entryInvestment_Account_balance

    ######################################################################

    def SUBMIT_INVESTMENT_ACCOUNT(self):
        ### THIS IS THE FUNCTION THAT WILL WRRITE THE MEMBER DATA OUT TO SQL
        print(self.get_investment_account_owner(),
                self.get_investment_account_institution(),
                self.get_investment_account_type(),
                self.get_investment_account_date_opened(),
                self.get_investment_account_balance())

        #POPUP CONFIRMATION WINDOW
        warningMessage = "Investment Account Owner: " + self.entryInvestment_Account_owner
        warningMessage += "\nInstitution:  " + self.entryInvestment_Account_institution
        warningMessage += "\nType: " + self.entryInvestment_Account_type
        warningMessage += "\nDate Opened: " + self.entryInvestment_Account_date_opened
        warningMessage += "\nBalance: " + self.entryInvestment_Account_balance
        window = Tk()
        window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
        window.withdraw()
        messagebox.showwarning('Stockwell_Financial Database Investment Account Entry', warningMessage)
        window.deiconify()
        window.destroy()

        #INPUTS ASSET DATA FROM GUI INTO MYSQL
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='Stockwell_Financial',
                                                 user='root',
                                                 password='Th3T3chBoy$')

            mySql_insert_query = """INSERT INTO Investment_Account (idInvestment_Account,
                                        owner, institution, type, date_opened, balance)
                                       VALUES
                                       (NULL, '%s', '%s', '%s', '%s', '%s') """ % (str(self.get_investment_account_owner()),
                                                                                        str(self.get_investment_account_institution()),
                                                                                        str(self.get_investment_account_type()),
                                                                                        str(self.get_investment_account_date_opened()),
                                                                                        str(self.get_investment_account_balance()))
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Investment_Account table")
            cursor.close()

        except mysql.connector.Error as error:
            messagebox.showwarning('WARNING: ', "Failed to insert data into Investment Account table.\nTry again.\nError Code: {}".format(error))
            print("Failed to insert data into Investment Account table {}".format(error))

        finally:
            if (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")
        return