# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:43:52 2018

@author: bbala
"""
#%%%
#This module provides data encoding and decoding as specified in RFC 3548.
import base64 # Used for encoding
#Read the input from command line – Reference ID 
#Check for validity – it should be 12 digits and allows on number and alphabet 
RefrenceId = input("Enter the reference Id(12 alphanumeric chars):")
if len(RefrenceId) != 12 and sum(char.isalnum() for char in RefrenceId) != 12:
  print("Reference Id should be 12 alphanumeric chars only!")
else:
    RefrenceId_encoded = base64.b64encode(bytes(RefrenceId,"utf-8"))
    print("Congratulations!!! ReferenceID is encrypted (%s), Wow:" % RefrenceId_encoded)
    info = input("You want to decode pass word[y/n]:")
    if info.upper() == 'Y':
        RefrenceId_decoded = base64.b64decode(RefrenceId_encoded).decode("utf-8", "ignore") 
        print("Your Ref Id Decoded:",RefrenceId_decoded)
#123456Abc$d  
#output
#Enter the reference Id(12 alphanumeric chars):#123456Abc$d
#Congratulations!!! ReferenceID is encrypted (b'IzEyMzQ1NkFiYyRk'), Wow:
#
#You want to decode pass word[y/n]:y
#Your Ref Id Decoded: #123456Abc$d
#Enter the reference Id(12 alphanumeric chars):#123456Abc$d
#Congratulations!!! ReferenceID is encrypted (b'IzEyMzQ1NkFiYyRk'), Wow:
#
#You want to decode pass word[y/n]:n        
#%%%
#1.  Allow some special characters in ReferenceID 
     # check for at least 1 letter 
     # check for at least 1 capital letter  
     # check for at least 1 number
     # check for atleast 1 special character($#@)
#2.  Give the option for decryption to user  
import base64 # Used for encoding
import re
def verify_password(password):
    # check for at least 1 letter
    lowercase_error = re.search(r"[a-z]", password) is None

    # check for at least 1 capital letter
    uppercase_error = re.search(r"[A-Z]", password) is None

    # check for at least 1 number
    number_error = re.search(r"\d", password) is None

    # check for atleast 1 special character
    specialCharacter_error = sum(char in password for char in '$#@') == 0

    l = len(password)
    # length check
    minLength_error = (l < 6)
    maxLength_error = (l > 12)

    password_ok = not(lowercase_error or uppercase_error or number_error or specialCharacter_error or minLength_error or maxLength_error)

    return password_ok == True
#Read the input from command line – Reference ID 
#Check for validity – it should be 12 digits and allows on number and alphabet
print ('Enter a password\n\nThe password must be between 6 and 12 characters.\n')
print ('atleast one letter [A-Z],atleast one letter [a-z],atleast one num[0-9]and atleast one char from [$#@] \n')
ReferenceId = input("Enter the pwd now:")
if verify_password(ReferenceId) == 'True':
  print("Check your password")
else:
    ReferenceId_encoded = base64.b64encode(bytes(ReferenceId,"utf-8"))
    print("Congratulations!!! ReferenceID is encrypted (%s), Wow:" % ReferenceId_encoded)
    info = input("You want to decode pass word[y/n]:")
    if info.upper() == 'Y':
        RefrenceId_decoded = base64.b64decode(ReferenceId_encoded).decode("utf-8", "ignore") 
        print("Your Ref Id Decoded:",RefrenceId_decoded)
#Verification:
#Enter the pwd now:Bsde#123
#Congratulations!!! ReferenceID is encrypted (b'QnNkZSMxMjM='), Wow:
#
#You want to decode pass word[y/n]:y
#Your Ref Id Decoded: Bsde#123