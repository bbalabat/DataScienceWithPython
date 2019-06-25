#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:33:19 2018

@author: bhadraiahbalabathuni
"""

#%%%
"""
Write a program which will find factors of given number and find whether 
the factor is even or odd.Hint: Use Loop with if-else statements
"""
def factorsOfnum(num):
    print("Given number :", num)
    N = int(num/2)
    lst = list()
    # ignoring 1 and the number itself
    for x in range(2,N+1):
        if num % x == 0:
            lst.append(x) 
            #print(x)
        else:
            pass
    print(lst)
    #print ([x for x in lst])
    print(list(map(lambda x: 'even' if (x % 2 == 0) else 'odd',lst)))
    
    even_nos = list(filter(lambda x: (x % 2 == 0), lst))
    print("Even numbers in the list: ", even_nos)
    odd_nos = list(filter(lambda x: ( x % 2 != 0 ),lst))   
    print("Odd numbers of the list: ", odd_nos)

while True:
    num = input ("Enter number:")
    try:
         num = int(num)
         factorsOfnum(num)
    except:
        break
#output:        
#Enter number:100
#Given number : 100
#[2, 4, 5, 10, 20, 25, 50]
#['even', 'even', 'odd', 'even', 'even', 'odd', 'even']
#Even numbers in the list:  [2, 4, 10, 20, 50]
#Odd numbers of the list:  [5, 25]
#
#Enter number: 
#
#In [15]: 
#%%%
"""
Write a code which accepts a sequence of words as input and prints the words 
in a sequence after sorting them alphabetically. Hint: In case of input 
data being supplied to the question, it should be assumed to be a console input
"""        
str_arr = input("Enter input sequence")
# conver sequnce of strinf into words
words = str_arr.split()
print(words)
# sort based on ASCII
#words.sort()
words = sorted(words)
print(words)
for word in words:
    print(word)
#output
#Enter input sequence This is a sample word
#['This', 'is', 'a', 'sample', 'word']
#['This', 'a', 'is', 'sample', 'word']
#This
#a
#is
#sample
#word
#%%%
"""
Write a program, whichwill find all the numbers between 1000 and 3000 (both
included) such that each digit of a number is an even number.
The numbers obtained should be printed in a comma separated sequence 
on a single line.
Hint: In case of input data being supplied to the question, it should be 
assumed to be a console input.Divide each digit with 2 and verify 
is it even or not.
"""
numbers = list(range(1000,3001))
#print(numbers)
all_even_digits = []    # store all even digit numbers
for num in numbers:
    if all(int(b) % 2 == 0 for b in str(num)):
        all_even_digits.append(num)
print(all_even_digits)
print ("Total  even digit numbers in between 1000-3000:", len(all_even_digits))  

#output
#[2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028, 2040, 2042, 2044,
# 2046, 2048, 2060, 2062, 2064, 2066, 2068, 2080, 2082, 2084, 2086, 2088, 2200,
# 2202, 2204, 2206, 2208, 2220, 2222, 2224, 2226, 2228, 2240, 2242, 2244, 2246,
# 2248, 2260, 2262, 2264, 2266, 2268, 2280, 2282, 2284, 2286, 2288, 2400, 2402,
# 2404, 2406, 2408, 2420, 2422, 2424, 2426, 2428, 2440, 2442, 2444, 2446, 2448,
# 2460, 2462, 2464, 2466, 2468, 2480, 2482, 2484, 2486, 2488, 2600, 2602, 2604,
# 2606, 2608, 2620, 2622, 2624, 2626, 2628, 2640, 2642, 2644, 2646, 2648, 2660,
# 2662, 2664, 2666, 2668, 2680, 2682, 2684, 2686, 2688, 2800, 2802, 2804, 2806,
# 2808, 2820, 2822, 2824, 2826, 2828, 2840, 2842, 2844, 2846, 2848, 2860, 2862,
# 2864, 2866, 2868, 2880, 2882, 2884, 2886, 2888]
#Total  even digit numbers in between 1000-3000: 125  
#%%%

while True:
    num = input("Enter a num [1000-3000] to find it has all even digits:")
    try:
        if (int(num) > 1999 and int(num) < 3001) and all(int(b) % 2 == 0 for b in num):
            print("All digits are even in:",num)
        else:
            print("Try another number")
    except:
        break
#output
#Enter a num [1000-3000] to find it has all even digits:888
#Try another number
#
#Enter a num [1000-3000] to find it has all even digits:2080
#All digits are even in: 2080
#
#Enter a num [1000-3000] to find it has all even digits:
#%%%
"""
Write a program that accepts a sentence and calculate the number of letters 
and digits.Suppose if the entered string is: Python0325
Then the output will be:LETTERS: 6 DIGITS:4
Hint: Use built-in functions of string
"""        
#text = "Python0325"
text = " This is a 1234 sample string345"
lst = list(text)
print(text)
print(lst)
num_digits = 0
num_alphabets = 0
for i in range(len(lst)):
    print(lst[i],ord(lst[i]))
    if ord(lst[i]) > 47 and ord(lst[i]) < 58:
        num_digits += 1
    elif ord(lst[i]) > 64 and ord(lst[i]) < 91:
        num_alphabets  += 1
    elif ord(lst[i]) > 96 and ord(lst[i]) < 123:
        num_alphabets  += 1 
    else:
        continue
print("DIGITS:",num_digits)
print("LETTERS:",num_alphabets)

#output
#T 84
#h 104
#i 105
#s 115
#  32
#i 105
#s 115
#  32
#a 97
#  32
#1 49
#2 50
#3 51
#4 52
#  32
#s 115
#a 97
#m 109
#p 112
#l 108
#e 101
#  32
#s 115
#t 116
#r 114
#i 105
#n 110
#g 103
#3 51
#4 52
#5 53
#DIGITS: 7
#LETTERS: 19
#%%
"""
Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.
"""
while True:
    #num = input("Enter a number:")
    try:
        num = input("Enter a number:")
        if int(num):    
            num_s = list(num)
            print(num_s)
            num_rev = num_s[::-1] # another way to reverse string
            #num_rev = reversed(num_s) # another way to reverse string
            print(num_rev)
            if num_s == num_rev:
                print("%s is polydrome" %num)
            else:
                print("Try another number")
            #break
    except:
        break
#output
#Enter a number:121
#['1', '2', '1']
#['1', '2', '1']
#121 is polydrome
#
#Enter a number:345
#['3', '4', '5']
#['5', '4', '3']
#Try another number
#
#Enter a number:
#%%
    
    
            