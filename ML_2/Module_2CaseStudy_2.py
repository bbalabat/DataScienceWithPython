#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:33:19 2018

@author: bhadraiahbalabathuni
"""

#%%%
"""
What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
Hint:Set consists unique element
"""
4,
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
#output
#4
#%%%
"""
What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))
Hint:d.keys()isthefunctionwhichwillshowkeys.

"""        
["john","peter"]
#output
#d ={"john":40, "peter":45}
#print(list(d.keys()))
#['john', 'peter']
#%%%
"""
A website requires a user to input username and password to register. 
Write a program to check the validity of password given by user. 
Following are the criteria for checking password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    Hint: In case of input data being suppliedto the question, 
          it should be assumed to be a console input
"""
def verifyPassword(pwd):
    checks = 0 # each bit for eachcondition check
    if len(pwd) > 13 or len(pwd) < 6:
        return "invalid length(6-13)"

    for i in pwd:
        #print(i)
        # verify [0-9]
        if ord(i) > 47 and ord(i) < 58:
            checks |= 1
            continue
        # verify [A-Z]
        elif ord(i) > 64 and ord(i) < 91:
            checks |= 2
            continue
        # verify [a-z]
        elif ord(i) > 96 and ord(i) < 123:
            checks |= 4
            continue
        elif ord(i) == 36 or ord(i) == 35 or ord(i) == 64:
            checks |= 8
            continue
        else:
            return "invalid pwd"
    # verufy all check are met or not
    return( 'Valid' if checks == 15 else 'InValid')
while True:
    name = input("Enter a name:")
    #pwd = input("Enter a pwd:")
    if name:
        pwd = input("Enter a pwd:")
        print(name,",pwd",verifyPassword(pwd) )
    else:
        break
#output
#Enter a name:Anish
#
#Enter a pwd:234#$asD
#Anish ,pwd Valid
#
#Enter a name:Anish
#
#Enter a pwd:asasasas
#Anish ,pwd InValid
#
#Enter a name:Anish
#
#Enter a pwd:qwe
#Anish ,pwd invalid length(6-13)
#
#Enter a name:

        

#%%%
"""
Write a for loop that prints all elements of a list and their position in the 
list.a = [4,7,3,2,5,9] Hint: Use Loop to iterate through list elements.
"""

a = [4, 7, 3, 2, 5, 9]
print("position| element")
for i in range(len(a)):
    print(i,'\t|\t',a[i])
#output
#position| element
#0       |        4
#1       |        7
#2       |        3
#3       |        2
#4       |        5
#5       |        9
#%%%
"""
Please   write   a   program   which accepts  a   string   from   console  
and   print   the characters that have even indexes.
Example: If the following string is given as input to the 
program:H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:Helloworld
"""
while True:
    str_input = input ("Enter string:")
    if str_input:
        str_out ="" # output string
        for i, char in enumerate(str_input):
            if i % 2 == 0:  #check even index
                str_out += char
        print(str_out)
    else:
        break
    
#output
#Enter string:H1e2l3l4o5w6o7r8l9d
#Helloworld
#
#Enter string:
#%%
"""
Please write a program which accepts a string from console 
and print it in reverse order.
Ex: If the following string is given as input to the program: rise to vote sir
Then, the output of the program should be:ris etov ot esir
"""
def reverse(s):
    new_str = ""
    for ch in s:
        new_str = ch + new_str
    return(new_str)

while True:
    str_input = input ("Enter string:")
    if str_input:
        print("The original string:%s" %(str_input))
        print("The reverse string:%s" %(reverse(str_input)))
        print("Another method for reverse string:%s" %(str_input[::-1]))       
    else:
        break
#output
#Enter string:Hello world
#The original string:Hello world
#The reverse string:dlrow olleH
#The reverse string:dlrow olleH
#
#Enter string:

#In [6]: 
#%%
"""
Please write a program which count and print the numbers of each character 
in a string input by console.
Example: If the following string is given as input to the program:abcdefgabc
Then, the output of the program should be
"""
while True:
    str_input = input ("Enter string:")
    if str_input:
        alphaChar = sorted(set(str_input))
        cnt = [0]*len(alphaChar) # initialise counter for each char
        print(alphaChar)         # uniqye alphabets
        #print(sorted(str_input))
        str_input = sorted(str_input)
        j = 0 # index in set
        for i in range(len(str_input)):
            if str_input[i] == alphaChar[j] :
               cnt[j] += 1
            else:
                j += 1
                cnt[j] += 1
        # print each alphabet and count
        for i in range(len(alphaChar)):
            print(alphaChar[i],":",cnt[i])
    else:
        break   
#output
#Enter string:asdfghjt
#['a', 'd', 'f', 'g', 'h', 'j', 's', 't']
#a : 1
#d : 1
#f : 1
#g : 1
#h : 1
#j : 1
#s : 1
#t : 1
#
#Enter string:asedfdefdfdfeefef
#['a', 'd', 'e', 'f', 's']
#a : 1
#d : 4
#e : 5
#f : 6
#s : 1
#
#Enter string:
#%%%
"""
With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
write   a program to make a list whose elements are 
intersection of the above given lists
"""
A =  [1,3,6,78,35,55]
B =  [12,24,35,24,88,120,155]
# convert A and B to sets
# intersection to be performed on sets
C = set(A) & set(B)
print(C,type(C)) 

#output
#{35} <class 'set'> 
#%%%
"""
By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155]
"""           
A = [12,24,35,24,88,120,155]
#list comprehension
B = [x for x in A if x != 24]
print(A)
print(B)
# using lambda function
new_list = list(filter(lambda x: (x != 24) , A))
print("using lamdda",new_list)

#output
#[12, 24, 35, 24, 88, 120, 155]
#[12, 35, 88, 120, 155]
#using lamdda [12, 35, 88, 120, 155]
#%%
"""
By using list comprehension, please write a program to print the list after
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
"""
X = [12,24,35,70,88,120,155]
#Y = [X[n] for n in range(len(X)) if (n != 0 and n != 4 and n != 5)]
#another way
Y = [X[n] for n in range(len(X)) if n != 0 if n != 4 if n != 5]
print(X)
print(Y)
#output
#[12, 24, 35, 70, 88, 120, 155]
#[24, 35, 70, 155]
#%%%
"""
By using list comprehension, please write a program to print the list after 
removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155] 
"""

A = [12,24,35,70,88,120,155]
B = [x for x in A if x % 5 == 0 if x % 7 == 0 ]
print(A)
print(B)
#output
#[12, 24, 35, 70, 88, 120, 155]
#[35, 70]
#%%%
"""
Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  
given  n  input  by console (n>0)
"""
# using a recursie function concept
def custom_out(n):
    if n == 0:
        return 0
    else:
        #print(n/(n+1))
        return ((n/(n+1))+custom_out(n-1))

while True:
    num = input("Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:")
    try:
        if int(num) > 0:
            print("Output:",custom_out(int(num)))
        else:
            print("Try another number")
    except:
        break
#output
#Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:0
#Try another number
#
#Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:7
#Output: 5.2821428571428575
#
#Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:8
#Output: 6.171031746031746
#
#Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:2
#Output: 1.1666666666666665
#
#Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:1
#Output: 0.5
#
#Enter a num [>0] to find its1/2+2/3+3/4+...+n/n+1:    
