from random import choice
import random
import string

a = "han" + \
    "Le" + \
    "Dinh"

#print (a)

b = 7
if b < 2:
    print("b < 2")
elif b > 2 and b < 5:
    print("b is from 2-->5")
else :
    print("b > 5")

#input("\n\nPress the enter key to exit.")
"""this is
multiple lines comments"""

x = y = z = 2
a,b,c=1,2,3
#print(a,b,c)
x //= 3
#print(x)

x = 3
while (x < 10):
    x += 1
    print(x)
    # y = input("\n\n enter a nuber ")
    # print("y = ", y)
    # if int(y) == 8: break

#input("\n\nPress the enter key to exit.")

for letter in 'Python':
   if letter == 'h':
      pass
      print ("Day la khoi pass")
   print ("Chu cai hien tai :", letter)

print ("Good bye!")

a = complex(1,2)
print(a)


x = [1,5, -2, 0, 3]
y = choice(x)
print(y)


Str_var1 = "hello python"
Str_var2 = 'HELLO PYTHON'
# print(Str_var1)
# print(Str_var2)

# for i in range(0, len(Str_var1)):
#     print(Str_var1[i])

# index = 0
# print(Str_var1[index:index + 2])



# print(Str_var1*2)
#
# print("My name is %s and I am %d years old" % ("Han", 27))
#
# x = "le;dinh; han ;90    "
# print(x)
# # print(str.strip(x))
#
# y = x.strip().split(";")
# z = x.count(';')
# print(z),
# #
# x = [1,2,3,4,5,6]
# x[0] = 0
# print(x)
# y = tuple(x)
# print(y)
# y[0] = 1
# print(y)

x = {'name':'Han', 'Age':27, 'Sex':'Male'}
print(x['Age'])

import time
localTime = time.localtime()
localTime = time.asctime(time.localtime())

print(localTime)

from datetime import datetime
print(datetime.today())

def Sum(x,y = 1):
    z = x + y
    return z

from Module_add import *
print(Addition(2,3))

# print("hoc Python", " that don gian", ' ban co thay vay ko?')

import os
# os.rename("TxtFileRenamed.txt", "TxtFile.txt")

x = open("TxtFile.txt",'r')
print(x.read())
x.close()

# print(x.closed)
y = open('TxtFile.txt', 'a+')
# y.write("I am trying to write to the file")
print(y.read())
y.close()



#===========2/28/2017====================

from SinhVien import *
sv1 = SinhVien("Han Le", 10000)
# sv1.tuoi = 21
print(sv1)
print(sv1.__doc__)


import xml.sax
import xml.dom
