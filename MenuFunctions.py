################################################################################
#    Author: Austin Stockwell
#    Date: 03-02-2020
#    Description:  This file contains methods that recieve the appropriate
#                   selected value of the GUIs menu objects and returns
#                   a single number that the MySQL database can understand.
#    File: MenuFunctions.py
################################################################################
from entry import *
from page_interface import *
####################### ####################### ###############################
#Asset_Category Table Functions
####################### ####################### ################################
def GetAsset_AssetCategoryMenu(varAsset_fk_asset_category_ID):
    if  varAsset_fk_asset_category_ID.get() == '(1) Stock':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '1'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(2) Bond':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '2'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(3) Index Fund':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '3'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(4) Mutual Fund':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '4'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(5) IRA':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '5'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(6) Roth IRA':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '6'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(7) 401k':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '7'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(8) Roth 401k':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '8'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(9) CD':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '9'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(10) Commodity':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '10'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(11) Cryptocurrency':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '11'
        return passThis
    if  varAsset_fk_asset_category_ID.get() == '(12) Real Estate':
        passThis = varAsset_fk_asset_category_ID.get()
        passThis = '12'
        return passThis

####################### ####################### ################################
# Bank_Transaction Table Functions
####################### ####################### ################################
def GetBankTransaction_BankAccountMenu(varBank_Transaction_fk_bank_account_ID):
    if  varBank_Transaction_fk_bank_account_ID.get() == '(1) Austin Centier Saving':
        passThis = varBank_Transaction_fk_bank_account_ID.get()
        passThis = '1'
        return passThis
    if  varBank_Transaction_fk_bank_account_ID.get() == '(2) Austin Centier Checking':
        passThis = varBank_Transaction_fk_bank_account_ID.get()
        passThis = '2'
        return passThis
    if  varBank_Transaction_fk_bank_account_ID.get() == '(3) Belle CHASE Saving':
        passThis = varBank_Transaction_fk_bank_account_ID.get()
        passThis = '3'
        return passThis
    if  varBank_Transaction_fk_bank_account_ID.get() == '(4) Joint CHASE Checking':
        passThis = varBank_Transaction_fk_bank_account_ID.get()
        passThis = '4'
        return passThis
    if  varBank_Transaction_fk_bank_account_ID.get() == '(5) Joint CHASE EMERGENCY SAVING':
        passThis = varBank_Transaction_fk_bank_account_ID.get()
        passThis = '5'
        return passThis

def GetBankTransaction_AssetMenu(varBank_Transaction_fk_asset_ID):
    if  varBank_Transaction_fk_asset_ID.get() == "None":
        passThis = varBank_Transaction_fk_asset_ID.get()
        passThis = "None"
        return passThis
    if  varBank_Transaction_fk_asset_ID.get() == '(1) Ethereum':
        passThis = varBank_Transaction_fk_asset_ID.get()
        passThis = '1'
        return passThis
    if  varBank_Transaction_fk_asset_ID.get() == '(2) Ripple':
        passThis = varBank_Transaction_fk_asset_ID.get()
        passThis = '2'
        return passThis

def GetBankTransaction_AssetCategoryMenu(varBank_Transaction_fk_asset_category_ID):
    if  varBank_Transaction_fk_asset_category_ID.get() == "None":
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = "None"
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(1) Stock':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '1'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(2) Bond':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '2'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(3) Index Fund':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '3'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(4) Mutual Fund':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '4'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(5) IRA':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '5'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(6) Roth IRA':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '6'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(7) 401k':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '7'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(8) Roth 401k':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '8'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(9) CD':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '9'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(10) Commodity':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '10'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(11) Cryptocurrency':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '11'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(12) Real Estate':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '12'
        return passThis
    if  varBank_Transaction_fk_asset_category_ID.get() == '(100) Paycheck':
        passThis = varBank_Transaction_fk_asset_category_ID.get()
        passThis = '100'
        return passThis

def GetBankTransaction_LiabilityCategoryMenu(varBank_Transaction_fk_liability_category_ID):
    if  varBank_Transaction_fk_liability_category_ID.get() == "None":
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = "None"
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(1) Rent':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '1'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(2) Mortgage':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '2'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(3) Water':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '3'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(4) Electricity':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '4'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(5) Home Insurance':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '5'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(6) Trash':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '6'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(7) Gas Bill':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '7'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(8) Car Payment':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '8'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(9) Car Insurance':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '9'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(10) Gasoline':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '10'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(11) Car Repairs':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '11'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(12) Groceries':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '12'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(13) Cellphone':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '13'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(14) Wifi':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '14'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(15) Bachelor Degree Loan':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '15'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(16) Credit Card Payment':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '16'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(17) Books':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '17'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(18) Hobbies':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '18'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(19) Music':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '19'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(20) Restaurant':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '20'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(21) Entertainment':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '21'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(22) Clothing':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '22'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(23) Travel':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '23'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(24) Jewelery':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '24'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(25) Home Improvement':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '25'
        return passThis
    if  varBank_Transaction_fk_liability_category_ID.get() == '(26) Self Improvement':
        passThis = varBank_Transaction_fk_liability_category_ID.get()
        passThis = '26'
        return passThis

def GetBankTransaction_CreditCardMenu(varBank_Transaction_fk_credit_card_ID):
    if  varBank_Transaction_fk_credit_card_ID.get() == "None":
        passThis = varBank_Transaction_fk_credit_card_ID.get()
        passThis = "None"
        return passThis
    if  varBank_Transaction_fk_credit_card_ID.get() == '(1) Austin: Sweetwater':
        passThis = varBank_Transaction_fk_credit_card_ID.get()
        passThis = '1'
        return passThis
    if  varBank_Transaction_fk_credit_card_ID.get() == '(2) Austin: Discover':
        passThis = varBank_Transaction_fk_credit_card_ID.get()
        passThis = '2'
        return passThis
    if  varBank_Transaction_fk_credit_card_ID.get() == '(3) Austin: CHASE Freedom':
        passThis = varBank_Transaction_fk_credit_card_ID.get()
        passThis = '3'
        return passThis
    if  varBank_Transaction_fk_credit_card_ID.get() == '(4) Austin: Citi':
        passThis = varBank_Transaction_fk_credit_card_ID.get()
        passThis = '4'
        return passThis
    if  varBank_Transaction_fk_credit_card_ID.get() == '(5) Belle: CHASE Freedom':
        passThis = varBank_Transaction_fk_credit_card_ID.get()
        passThis = '5'
        return passThis

####################### ####################### ################################
# Credit_Transaction Table
####################### ####################### ################################
def GetCreditTransaction_CreditCardMenu(varCredit_Transaction_fk_credit_card_ID):
    if  varCredit_Transaction_fk_credit_card_ID.get() == '(1) Austin: Sweetwater':
        passThis = varCredit_Transaction_fk_credit_card_ID.get()
        passThis = '1'
        return passThis
    if  varCredit_Transaction_fk_credit_card_ID.get() == '(2) Austin: Discover':
        passThis = varCredit_Transaction_fk_credit_card_ID.get()
        passThis = '2'
        return passThis
    if  varCredit_Transaction_fk_credit_card_ID.get() == '(3) Austin: CHASE Freedom':
        passThis = varCredit_Transaction_fk_credit_card_ID.get()
        passThis = '3'
        return passThis
    if  varCredit_Transaction_fk_credit_card_ID.get() == '(4) Austin: Citi':
        passThis = varCredit_Transaction_fk_credit_card_ID.get()
        passThis = '4'
        return passThis
    if  varCredit_Transaction_fk_credit_card_ID.get() == '(5) Belle: CHASE Freedom':
        passThis = varCredit_Transaction_fk_credit_card_ID.get()
        passThis = '5'
        return passThis

def GetCreditTransaction_LiabilityCategoryMenu(varCredit_Transaction_fk_liability_category_ID):
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(1) Rent':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '1'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(2) Mortgage':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '2'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(3) Water':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '3'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(4) Electricity':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '4'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(5) Home Insurance':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '5'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(6) Trash':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '6'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(7) Gas Bill':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '7'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(8) Car Payment':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '8'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(9) Car Insurance':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '9'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(10) Gasoline':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '10'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(11) Car Repairs':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '11'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(12) Groceries':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '12'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(13) Cellphone':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '13'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(14) Wifi':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '14'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(15) Bachelor Degree Loan':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '15'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(16) Credit Card Payment':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '16'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(17) Books':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '17'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(18) Hobbies':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '18'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(19) Music':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '19'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(20) Restaurant':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '20'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(21) Entertainment':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '21'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(22) Clothing':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '22'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(23) Travel':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '23'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(24) Jewelery':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '24'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(25) Home Improvement':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '25'
        return passThis
    if  varCredit_Transaction_fk_liability_category_ID.get() == '(26) Self Improvement':
        passThis = varCredit_Transaction_fk_liability_category_ID.get()
        passThis = '26'
        return passThis
