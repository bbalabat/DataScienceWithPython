# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:39:41 2018

@author: NAEEN REDDY
"""


#Input Function

var=input('Enter your age(0-120):')
print(var, type(var))

age = int(var)

if age > 0 and age <= 120:
    print('You entered valid age')
else:
    print('Hello , You have entered invalid AGE  {}!'.format(var))
    
    
    
##DICT DIFF

d1 = {'fname': 'Steve', 'lname': 'Jobs'}
d2 = {'fname': 'Steve', 'lname': 'Jobs', 'age': 21}

is_equal = True
diff = set(d1.keys()).symmetric_difference(set(d2.keys()))
print(diff)


#The most common use for break is when some external condition is triggered requiring a 
#hasty exit from a loop. The break statement can be used in both while and for loops. 
#The pass statement in Python is used when a statement is required syntactically but you do 
#not want any command or code to execute.

if len(set(d1.keys()).symmetric_difference(set(d2.keys()))) == 0:
    print('Same number and set of keys')
    for k in d1:
        print('Key is:', k)
        if k in d2:
            print(d1[k], d2[k])
            if d1[k] == d2[k]:
                pass
            else:
                is_equal = False
                break
        else:
            is_equal = False
            break
else:
    is_equal = False
print(is_equal)



import os
newfile=open("Edureka_Py.txt","w+")

for i in range(1,10):
    newfile.write("\n Hello, welcome to Python:")

newfile.close()

newfile=open("Edureka_Py.txt","r")

for i in range(1,10):
    print(newfile.read())

newfile.seek(5)
print(newfile.tell())
os.rename("Edureka_Py.txt","Python1.txt")
os.remove("Python1.txt")

newfile.close()






#import os

os.getcwd()

#os.curdir

os.listdir(os.getcwd())

#os.mkdir('new')


fp = open("USArrests.csv", "r")
for line in fp:
    print(line)
# print(fp.read())
fp.close()


fp = open('Misc/USArrests.txt', 'r')
for line in fp:
    print(line)
# print(fp.read())
fp.close()









import codecs

fp = codecs.open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2','worldcities.csv'), 'r', 'utf-8')
cnt = 0
for line in fp:
    if cnt <= 10:
        print(line)
    else:
        break
    cnt += 1
fp.close()


os.rename('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2\\worldcities.csv', os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\','County.csv'))






wp = open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2\\', 'counry.csv'), 'w')

rp = open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2','worldcities.csv'), 'r')
cnt = 0
for line in rp:
    if cnt <= 10:
        wp.write(line)
        wp.write('\n')
    else:
        break
    cnt += 1
rp.close()
wp.close()






#d1 = {'fname': 'Steve', 'lname': 'Jobs'}
#d2 = {'fname': 'Steve', 'lname': 'Jobs', 'age': 21}

import json
wp = open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2', 'test_new.json'), 'w+')
for x in range(3):
    if x == 0:
        wp.write(json.dumps(d1))
    elif x == 1:
        wp.write(json.dumps(d2))
    else:
        wp.write(json.dumps({'age':24, 'salary':10000}))
    wp.write('\n')
wp.close()



#import json
wp = open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2', 'test_new.json'), 'w+')
for x in range(5):
    if x == 0:
        wp.write(json.dumps(d1))
    elif x == 1:
        wp.write(json.dumps(d2))
    else:
        wp.write(json.dumps({'age':24, 'salary':10000}))
    wp.write('\n')
wp.close()



#import json
rp = open(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2', 'test_new.json'), 'r')
# content = json.loads(rp.read())
for line in rp:
    #print(line)
    rec = json.loads(line)
    #print(rec, type(rec))
    print(rec.get('salary', 'Not found'))
    
rp.close()




# d1['key'] and d1[key]
path = os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2', 'test_new.json')
print(path)


os.path.exists(os.path.join('Misc/old', 'test.json'))


os.path.exists(os.path.join('C:\\Users\\NAEEN REDDY\\Desktop\\py\\D2', 'test.json'))














