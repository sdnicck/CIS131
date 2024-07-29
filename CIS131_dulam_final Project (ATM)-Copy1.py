#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Satya Dulam
#CIS131
#7/28/24
#CIS131 Final Project Rough draft(ATM machine)

#currently struggling with input validation: trying to loop through certain indexes of 
#multiple tuples and comparing them user input

# attempted input validation for PIN
def getValidPIN(message):
    while True:
        try:
            userInput = int(input(message))
            for tup in bankDataBase:
                if userInput in tup:
                    return userInput
                else:print("Please input a valid PIN:")
        except ValueError:
            print("Incorrect data entered, please re-attempt")
            
#input validation for date of birth needed?


#account class created 
class Account:
    
    def __init__(self, PIN,DOB, balance):

        # if balance is less than 0.00, raise an exception
        if balance < 0.00:
            raise ValueError('Initial balance must be >= to 0.00.')

        self.PIN = PIN
        self.DOB = DOB
        self.balance = balance

    def deposit(self, amount):

        # if amount is less than 0.00, raise an exception
        if amount <= 0.00:
            raise ValueError('Amount deposited must be positive.')

        self.balance += amount
        
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError('Must have enough funds to withdraw.')
            
        self.balance -= amount
        
    def __repr__(self):
        return f"Your account balance is {self.balance:,.2f}"
    
#random fake customers with stored pins, birthdays, and account balances
        
account1=(4567,5/5/23,50.00)
account2=(7654,5/5/23,50.00)

#a storage bank of all accounts in the bank
bankDataBase= [account1,account2]


pinValid=getValidPIN("Please input PIN: ")

dobValid=input("Please input Date of Birth:")


#some input validation I was messing with for the PIN and DOB       
for tup in bankDataBase:
        index = 0
        while index == 0:
            value = print(tup[0])
            index +=1
        
    
for tup in bankDataBase:
        index = 0
        while index == 0:
            value = print(tup[1])
            index +=1


# In[ ]:




