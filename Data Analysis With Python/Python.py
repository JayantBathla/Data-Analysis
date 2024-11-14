#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Python_1

print(12)
print(False)
# Python is case sensitive language.




print(type("Jayant"), type(21),type(True))

# Arithmatc Operations

print(5 + 7)
print(5 - 7 )
print(5 * 7)
print(5 / 7)
print(5 // 7)
print(5 % 7)
print(5 ** 7)

# comparision Operaters <,>,=<,=>,==,!= || They will give result in boolean values (true, false)
# Logical Operaters - not, or, and ||  They will give result in boolean values (true, false)

# variables 


# In[5]:


print('jayant')


# In[1]:


print("Hello World!")


# In[8]:


count = 0  
for num in range(1,1001):
    track = 0 
    for i in range (1,num+1):
        if (num%i == 0):
            track += 1
    if track == 2:
        count += 1
     


# In[9]:


print(count)


# In[10]:


# Python_1

print(12)
print(False)
# Python is case sensitive language.


print("Jayant")
print(type("Jayant"), type(21),type(True))

# Arithmatc Operations
print('Arithmatc Operations')
print(5 + 7)
print(5 - 7 )
print(5 * 7)
print(5 / 7)
print(5 // 7)
print(5 % 7)
print(5 ** 7)


# Value of true is always 1 if is used in arithmatic operations 
print(True * 'Jayant')
print(True + True)

# comparision Operaters <,>,=<,=>,==,!= || They will give result in boolean values (true, false)
print('Comparision Operaters')
print(5 > 7)
print(5 >= 7 )
print(5 < 7)
print(5 >= 7)
print(5 != 7)
print(5 == 7)

# Logical Operaters - not, or, and ||  They will give result in boolean values (true, false)
print('Logical Operaters')
print(5>7) and (7!=7)



# Variables 

a = 5
print(a)
a = a +1
print(a)


a += 1

a = a * 5
a //=5
print(a)


pr = 10000
intr  = 7 
yrs = 5

Total_amt = (pr*intr*yrs)/100 + pr
print(Total_amt)


# type casting(changing the type of data)
print(int(3.14))
# print(int('Jayant')) Cant convert string to integer
print(int(True))





print(str(3.14))
print(str(32342))
print(str(True))


print(bool(3.14))
print(bool(32342))
print(bool('Jayant'))
print(bool(' '))
print(bool(0))
# Anything youll convert to boolean, it will give you true always. you will get false as output only when there is 0 or when youre writhing nothing inside a string


# CONDITIONS
 
age = 180

print(age >= 18)


if age >= 18:
    print('eligible')


if (age >= 18) and (age <= 100):
    print('eligible')
    
elif (age >= 0) and (age < 18):
    print('Not Eligible')
    
else:
    print('Invalid')

num = 31
    
if(num % 5 == 0):
    if(num % 7 == 0):
        print ('div 5 & 7')
    else:
        print('5 not 7')
elif(num % 7 == 0):
    print('7 not 5')

else:
    print('not 5 not 7')


n =13


for i in range(1,11):
    print(n,'x',i,'=',n*i)
    


for i in range (5,51,5):
    print(i)
    
num = 35
for i in range (num,num*10+1,num):
    print(i) 

# for reverse order 
for i in range(10,0,-1):
      print(i)

num = 22

for i in range(num*10,num-1,-num):
      print(i)

# Q1 print all the number from the table of 23 which are divisible by 5 
num = 23

for i in range(1,11):
      res = i*num
      if res%5 == 0:
          print(res)
          
# Q2 print the number between 1-100 that are divisible by 5 and 3

for i in range (1,101,1):
    if (i%5 == 0) and (i%3 == 0):
        print(i)
        
        
# Q3 How many prime numbers do we have between 0-1000
primes = 0
for num in range (1,1001):
    
    count =0
    
    for i in range (1,num+1):
        if(num%i == 0):
            count += 1
    

    if count == 2:
        primes += 1
        
        
print(primes)



# In[14]:


print('Jayant', end= ' ')
print('Bathla', end=' ')


# In[20]:


# string replication
print('jayant'* 4)


# In[21]:


#string length


# In[22]:


print(len('jayant  bathla'))


# In[35]:


#string slicing
print('jayant' [3])
print('jayant bathla'[-4])
print('jayant bathla'[0:6])
print('jayant bathla'[7:14])


# In[38]:


#string case conversion

print('jayant bathla'.upper())
print('jayant bathla'.lower())


# In[41]:


# string stripping

print('      jayant bathla     '.strip())
# it only takes care of extra spaces in begining and end of string not the between


# In[43]:


#string replacing
print('jayant bathla'.replace('a', 'x'))


# In[45]:


# string count
print('jayant bathla'.count('a'))


# In[46]:


#string find
print('jayant bathla'.find('bat'))


# In[49]:


#string check

print('jayantbathla'.isalpha())
print('1234'.isdigit())
print('JAYANT'.isupper())
print('jayant'.islower())


# In[51]:


#string capitalization
print('jayant bathla'.capitalize())
print('jayant bathla'.title())


# In[54]:


#check for start and end
print('jayant bathla'.startswith('jay'))
print('jayant bathla'.endswith('hla'))


# In[60]:


print('jayant bathla'.center(20, '*'))
print('jayant bathla'.ljust(20, '*'))
print('jayant bathla'.rjust(20, '*'))


# In[62]:


print(float("3.14"))


# In[63]:


print('hello'.capitalize())
print('hello'.upper())


# In[1]:


n =30 
i = 1
s = 1

while (n>s):
    
    print(s)
    i = i+1
    s= s+i
    


# In[ ]:


#Write a Python program to count the total number of digits in a given number using a while loop.

#Example: For the number 75869, the output should be 5.


# In[ ]:





# In[5]:


print('heelo')


# In[ ]:





# In[1]:


num = 75869
count = 0
while num != 0:
    num = num // 10  # floor division to reduce the last digit
    count = count + 1
print("Total digits are:", count)


# In[8]:


# LIST
lst = ['Jayant', 'bathla' , 'jbathla@gmail.com', 'ghaziabad']
print(lst)


# In[10]:


print(lst[0])


# In[11]:


print(lst[3])


# In[12]:


print(lst[-1])


# In[14]:


lst[1] = 'Bathla'


# In[15]:


print(lst)


# In[16]:


lst.append('varun')


# In[17]:


lst.remove('Jayant')


# In[18]:


print(lst)


# In[19]:


lst = [1,2,3,4,6,35,23,13,1,43253,5242,4,3,31]
print(lst)


# In[20]:


print(sorted(lst))
# similarly can find minimum and maximum just by putting min or max in place of sorted


# In[22]:


print(lst[::-1])


# In[24]:


lst.reverse


# In[25]:


print(lst)


# In[27]:


lst.index(43253)


# In[28]:


print(lst.count(1))


# In[29]:


lst.extend([23,32,45,632,1111111,])
print(lst)


# In[30]:


#iterating through list


# In[54]:


print(lst)
for i in (lst):
    print(lst)


# In[32]:


print(lst)
for i in range(len(lst)):
    print(i, lst[i])


# In[57]:


print(lst)
for i in range(-1,-11,-1):
    print(lst[i], i)


# In[59]:


for i in range(-1, -(len(lst)+1), -1):
    print(i,lst[i])


# In[ ]:


# MULTI-DIMENSIONAL LIST


# In[34]:


lst = [[1,2,3],[4,5,6],[7,8,9]]


# In[35]:


print(lst[0])


# In[36]:


print(lst[1])


# In[37]:


print(lst[0][0])


# In[38]:


print(lst[2][0])


# In[39]:


#modify values
lst[1][1] = 22
print(lst)


# In[40]:


lst[1] = ['Jayant', 21]


# In[41]:


print(lst)


# In[44]:


lst.append([1,11,111])
del lst[0]
print(lst)


# In[46]:


print(lst)
for i in lst:
    print(lst)


# In[48]:


print(lst)
for i in lst:
    for j in lst:
        print(lst)


# In[49]:


# LIST COMPREHENSIONS
lst = [1,2,3,4,5,6]
print(lst)


# In[38]:


print([[j for j in range(1,4)] for i in range(4)])


# In[51]:


lst = [i**2 for i in lst]
print(lst)


# In[1]:


dct  = {1 : 'Jayant', 2: 'Ridhma', 3 : 'Sunil', 4 : 'Meenu'}
print(dct)


# In[2]:


print(dct[1])


# In[3]:


print(dct[4])


# In[9]:


#adding and updating key value pairs
dct[5] = 'varun'
print(dct)
del(dct[3])
print(dct)


# In[6]:


#cleaning the dictionary
dct.clear()


# In[7]:


print(dct)


# In[10]:


#Iterating through the dictionary
dct  = {1 : 'Jayant', 2: 'Ridhma', 3 : 'Sunil', 4 : 'Meenu'}
dct[5] = 'varun'
print(dct)


# In[11]:


print(dct.keys())


# In[12]:


print(dct.values())


# In[13]:


for k in dct.keys():
    print(dct[k],k)


# In[14]:


print(dct.items())


# In[15]:


#check if key is prsent in dictionary
print(1 in dct)
print(10 in dct)


# In[18]:


#dct updating values
dct1 = {1: 'A', 2 : 'B',3 : 'C'}
dct2 = {1 : 'a',2 : 'b',3 : 'c'}
print(dct1)
print(dct2)
dct1.update(dct2)
print(dct1)
print(dct2)


# In[19]:


# MULTI-DIMENSIONAL DICTIONARY


# In[20]:


dct = {1 : {'name' : 'Jayant', 'marks' : [38,48,87,47,45]},
       2 : {'name' : 'Manish', 'marks' : [38,49,87,47,45]},
       3 : {'name' : 'Hitesh', 'marks' : [38,23,87,47,45]}}
print(dct)


# In[22]:


print(dct[1])


# In[23]:


print(dct[2]['name'])


# In[24]:


dct[3]['name'] = 'Ridhma'
print(dct)


# In[28]:


for i in dct.keys():
    print(i , dct[i])


# In[29]:


for i in dct.keys():
    print(i , dct[i]['name'])


# In[30]:


dct = { 1 : {'name' : 'Ashish', 'phone' : 123456789, 'marks' : {'hin':45,'mth':42,'sci':41}},
         2 : {'name' : 'Ankur' , 'phone' : 127398127, 'marks' : {'hin':32,'mth':38,'sci':13}},
         3 : {'name' : 'Riya'  , 'phone' : 127398127, 'marks' : {'hin':12,'mth':38,'sci':43}}}
print(dct)


# In[33]:


#you have to access marks of maths of everyone
for i in dct.keys():
    print(i, dct[i]['name'] , dct[i]['marks']['mth'])


# In[34]:


dct = {i:i**3 for i in range(1,6)}
print(dct)


# In[35]:


dct = {i:i**2 for i in range(1,11) if i%2 == 0}
print(dct)


# In[43]:


#COnvert list to dictionary
lst = ['Apple','Banana','Grapess']
dct = {item : len(item) for item in lst}
print(dct)

dct={len(item): item for item in lst}
print(dct)


# In[41]:


dct = {'num_' + str(i) : i for i in range(1,11)}
print(dct)


# In[51]:


dct = {'num_' + str(i) : i for i in range(1,11)}
dct = {k:v for k,v in dct.items() if v%3 == 0}
print(dct)


# In[50]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
final_dct = {(i,j) : matrix[i][j] for i in range(3) for j in range(3)}
print(final_dct)
print('-'*30)

final_dct = {matrix[i][j] : (i,j) for i in range(3) for j in range(3)}
print(final_dct)


# In[1]:


#creating a set
my_set = {1,2,3,4,5}
print(my_set)


# In[2]:


my_set.add(6)


# In[3]:


print(my_set)


# In[4]:


print(type(my_set))


# In[5]:


popped_element = my_set.pop()
print(popped_element)


# In[6]:


my_set.discard(4)
print(my_set)


# In[7]:


for i in my_set:
    print(i)


# In[8]:


#set operations
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}


# In[9]:


print('union: ', set_1 | set_2 )


# In[10]:


print('intersection: ', set_1 & set_2)


# In[11]:


print('difference: ', set_1 - set_2)


# In[12]:


print('difference: ', set_2 - set_1)


# In[13]:


print('Symmetric difference: ', set_1 ^ set_2)


# In[14]:


my_set.clear()
print(my_set)


# In[15]:


#TUPLE
tpl = (1,2,3,4,5)
print(tpl)


# In[16]:


# Accessing
tpl = (1,2,3,4,5)
print(tpl[0])
print('-'*20)

# Slicing
tpl = (1,2,3,4,5)
print(tpl[1:3])
print('-'*20)

# Concatenate
tpl1 = (1,2,3,4)
tpl2 = (4,5,6,7)
tpl = tpl1 + tpl2
print(tpl)
print('-'*20)

# Iterating
print(tpl)
for i in tpl:
    print(i)
print('-'*20)

# Checking the Element
print(tpl)
print(2 in tpl)
print(3 in tpl)
print(4 in tpl)
print('-'*20)

# Checking the Count
print(tpl)
print(tpl.count(4))
print('-'*20)

# Finding the Index
print(tpl)
print(tpl.index(3))
print('-'*20)

# Multiplying the Touple
print(tpl)
print(tpl*3)
print('-'*20)


# In[1]:


def greet():
    print("Hello")

greet()


# In[2]:


greet()


# In[3]:


for i in range(5):
    greet()


# In[4]:


#understanding the scope of functions 

g_var = 10

def scope():
    l_var = 5
    print(g_var,l_var)
scope()


# In[5]:


print(g_var,l_var)


# In[6]:


# as l_var was defined inside a function, calling it to br printed outside a function will show an error


# In[25]:


def hi(n):
    print("Hello", n)
    
hi("Jayant")


# In[36]:


def greet(name = "------"):
    print("Hello", name)
    
greet()


# In[37]:


def subm(a = 0, b = 0):
    print(a,b,a+b)
    
subm(5,10)


# In[38]:


subm()


# In[39]:


#function return

def subm(a = 0, b = 0):
    return(a+b)
    
s = subm(10,12)
print(s)


# In[40]:


# multiple return
def multi(a = 0, b = 0):
    return(a+b, a-b, a*b)
    
s = multi(10,12)
print(s)


# In[47]:


#multi-function(a function inside function)
lst = [1,2,3,4,5]

def sq(lst):
    return[i**2 for i in lst]
   
def cu(lst):
    return[i**3 for i in lst]


def final(lst):
    lst_1 = sq(lst)
    lst_2 = cu(lst)
    return[lst_1[i] + lst_2[i] for i in range(len(lst_1))]
print(final(lst))


# In[48]:


print(final(lst))


# In[60]:


# practice list 


# In[67]:


#print all the numbers in lst between 0-100 that are divisible by 100
lst = []

for i in range(101):
    if (i%5 == 0) and (i%7 == 0):
        lst.append(i)
    
print(lst)
        


# In[69]:


lst = [[1,2,4,5,6], [4,5,6,4,5]]
s =0 
for i in range(len(lst)):
    for j in range(len(lst[0])):
        s += lst[i][j]
        
print(s)


# In[70]:


lst = [[1,2,4,5,6], [4,5,6,4,5]]
s =0 
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j])
        


# In[84]:


lsst = [[1,2,4],
        [4,5,6],
        [7,8,9]]
# print diagonal elements of this list
s = 0
for i in range(3):
    for j in range(3):
        if i == j:
            s += lsst[i][j]
            print(lsst[i][j])


# In[86]:


print(s)
# this is the sum of the diagonal elements


# In[91]:


p = 0
for i in range(3):
    for j in range(3):
        if i + j == 2:
            p += lsst[i][j]
            print(lsst[i][j])
# these are the elements of the second diagonal of the matirx and bottom is ther sum


# In[92]:


print(p)


# In[1]:


#inbuilt libraries


# In[5]:


import math


# In[16]:


# Basic Arithmetic Functions:
x = 10.8
print(math.ceil(x))  # upper bound
print(math.floor(x)) # lower bound
print(math.trunc(x)) # remove decimal
print('-'*30)

# Exponential and Logarithmic Functions:
x = 3
print(math.exp(x))   # Returns e raised to the power of x.
print(math.log10(x)) # Returns the base-10 logarithm of x.
print('-'*30)

# Trigonometric Functions:
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print('-'*30)

# Constants:
print(math.pi)   # Mathematical constant pi (π).
print(math.e)    # Mathematical constant e (base of natural logarithm)
print('-'*30)


# Special Functions:
x = 5
print(math.factorial(x))  # Returns the factorial of x.
print(math.gamma(x))      # Returns the gamma function at x.
print('-'*30)


# In[15]:


import random

print(random.random())                      # [0.0 - 1.0]
print(random.randint(1,10))                 # Pick a random number in that range
print(random.choice([1, 2, 3, 4, 5]))       # Take a random value
print(random.sample([1, 2, 3, 4, 5], 3))    # Random Sample of n values
print(random.uniform(1.0, 2.0))             # Random Float in tht range

random.seed(42)   #seed value is same

print(random.random())
print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))


# In[19]:


import datetime

print(datetime.datetime(2024, 10, 28, 10, 30, 0)) # Specific Datatime
print(datetime.datetime.now())                    # Current Datetime

print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))     # to chnage the format

date_1 = datetime.datetime(2023, 11, 28, 10, 30, 0)
date_2    = datetime.datetime.now()

print(date_2 - date_1)


# In[21]:


from collections import Counter, defaultdict, OrderedDict, ChainMap

# 1. Counter
my_list = [1, 2, 3, 1, 2, 1, 2, 3, 4]
counter = Counter(my_list)
print(counter)

# 2. Defaul Dictionary | No need to check if 'a' is in the dictionary
d = defaultdict(int)
d['a'] += 2
print(d)

# 3. Ordered Dictionary
d = OrderedDict()
d['one'] = 1
d['two'] = 2
print(d)


# In[22]:


import string

# Constants
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print('-'*30)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print('-'*30)

print(string.punctuation)


# In[26]:


class person:
    name = 'Jayant'
    age = 21


# In[28]:


p1 = person()
print(p1.name)
print(p1.age)


# In[32]:


p1.name = 'Varun'
p1.age = 23


# In[33]:


print(p1.name)
print(p1.age)


# In[34]:


p2 = person()
print(p2.name)
print(p2.age)


# In[37]:


# Methods 
print('METHODS')


# In[39]:


class Student:
    name = 'Jayant'
    
s1 = Student()
print(s1.name)


# In[41]:


class Student:
    name = 'Jayant'
    def __init__(self):
        print("adding new student to the database")
    
s1 = Student()


# In[42]:


# as we have added the constuctor it will show the adding statement whenever we run init function even without print name


# In[43]:


class Student:
    name = 'Jayant'
    def __init__(self):
        print(self)
        print("adding new student to the database")
    
s1 = Student()
print(s1.name)


# In[44]:


class Student:
    def __init__(self, fullname):
        self.name= fullname
        print("adding new student to the database")
    
s1 = Student("Varun")
print(s1.name)


# In[46]:


# self will always be first parameter, self is refrence of instance of class and is used to access variables i  class\


# In[47]:


class Student:
    def __init__(self, fullname):
        self.name= fullname
        print("adding new student to the database")
    
s1 = Student("Varun")
print(s1.name)
s2 = Student("Ridhi")
print(s2.name)


# In[49]:


class Student:
    def __init__(self, fullname):
        self.name= fullname
        print("adding new student to the database")
        
    def welcome(self):
        print("Welcome Student")
        
    
s1 = Student("Varun")
print(s1.name)
s1.welcome()
s2 = Student("Ridhi")
print(s2.name)
s2.welcome()


# In[57]:


class Student:
    def __init__(self, name , marks):
        self.name= name
        self.marks = marks
        print("marks added")
    
    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name, "your avg score is :" , sum/3)
    
s1 = Student("Varun", [92,67,81])
print(s1.name, s1.marks)
s1.avg_marks()


# In[59]:


s2 = Student("Jayant", [45,67,99])
print(s2.name,s2.marks)
s2.avg_marks()


# In[9]:


class Account:
    def __init__ (self,balance, acc):
        self.account_no = acc
        self.balance = balance
        
    def debit(self, amount):
        self.balance -= amount
        print(amount, "is debited from your account" )
        
    def credit(self, amount):
        self.balance += amount
        print(amount, "is credit to your account" )
        
    def get_balance(self):
        return(self.balance)
        

        
acc1 = Account(13000, 1021002201)
print(acc1.balance,acc1.account_no)
acc1.debit(2000)
acc1.credit(5000)
acc1.get_balance()



# # Starting with Numpy

# In[2]:


pip install numpy


# In[4]:


import numpy as np


# In[6]:


#How to create an array
arr = np.array([1,2,3,4,5])
print(arr)


# In[7]:


print(type(arr))


# # dimensions in array

# In[9]:


#0D Array, array with only one element in it 


# In[10]:


arr = np.array(20)
print(arr)
print(type(arr))
print(arr.ndim) #ndim is used to check dimensions


# In[11]:


#1D Array


# In[39]:


arr = np.array([1,2,3,4,5,6])
print(arr)
print(arr.ndim)
arr.shape


# In[13]:


#2D Array


# In[43]:


arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim)
arr.shape #it tells the shape of the array in format(row, columns)
arr.dtype #it tellsthe type of data stored inside an array
#floats can also be put inside an array


# In[15]:


#3D Array


# In[41]:


arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [1,4,7]]])
print(arr)
print(arr.ndim)
arr.shape
#similarly we can create n dimension array, if we notice difference in 2d and 3d array can be seen in the no. of --
# -- square brackets used while creating array


# In[24]:


#another way to create n number array, using ndmin
arr = np.array([1,2,3,4,5], ndmin=5)
print(arr)
print("Dimensions of the array arr are:", arr.ndim)


# In[45]:


#easy way to create zeros and ones
zeros = np.zeros((5,4))
zeros


# In[46]:


ones = np.ones((7,2))
ones


# In[27]:


# Numpy array Indexing
## Indexing is basically accessing any element inside an array, similarly how we did earlier in lists


# In[28]:


arr = np.array([1,2,3,4,5,6])
print(arr)
print(arr[0])


# In[35]:


m = np.array([23,45,24,23,424,23,31,42,21,3,242,353,5,5234,23])
print("Element number 5 in array m is:",m[6])
print("Element number 10 in array m is:",m[11])
print("Last Element in array m is:",m[-1])

print("Sum of above 3 is :", m[6]+m[11]+m[-1])


# In[31]:


#Accessing 2D Arrays


# In[36]:


m = np.array([[10,20,30,40,50],[5,10,15,20,25]])
print(m[0][3])
print(m[1][3])


# In[37]:


#add any 2 elements from the 2 array both belonging to different rows
print("SUM IS", m[0,2]+m[1,-1])


# In[115]:


arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])


# In[116]:


arr


# In[120]:


arr[:,:]


# In[121]:


arr[:,:1] #all rows of column 1


# In[124]:


arr[:,1:2]


# In[123]:


arr[:1,:] #all columns of 1st row


# In[125]:


arr[1:2,1:2]


# In[126]:


#all elements except 1st row and 1st column
arr[1:,1:]


# In[47]:


#create random, reshape
arr = np.random.random((3,3))


# In[48]:


arr


# In[55]:


#create array within specified range (it is like an for loop)
np.arange(1,10,2)
#Parameters: start, stop, and step.

#Syntax: np.arange(start, stop, step)


# In[61]:


np.linspace(1,5, 15) 

#Parameters: start, stop, and num (Total number of values i want).
# all the values will be equidistant to each other
#Syntax: np.linspace(start, stop, num)


# In[64]:


#reshape

m = np.random.random((5,3))


# In[65]:


m


# In[66]:


arr = np.reshape(m , (3,5))


# In[168]:


arr


# In[169]:


#Note while reshaping the array the size of the array should be same fro example above 5,3 =5x3 = 15 is size
# final size after reshape should be 15 


# In[170]:


#Flatten


# In[171]:


arr.flatten()
# as you can see by flattening the array we have converted it from 2d to 1d


# In[172]:


arr.ravel() # same as flatten


# In[79]:


#Arithmatic Operations on array
arr1 = np.array([1,2,3,4,5,6])


# In[84]:


arr1


# In[83]:


print(arr1+1)
print(arr1-1)
print(arr1*4)
print(arr1/31)


# In[87]:


arr1**2 #power2


# In[89]:


arr1 +=1


# In[90]:


arr1


# In[92]:


arr1 *=3
arr1


# In[93]:


arr1.min()


# In[94]:


arr1.max()


# In[95]:


arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr


# In[103]:


arr.max(axis=0) # this will print maximum values based on each column(COLUMN -WISE)


# In[104]:


arr.max(axis=1) # this will print maximum values based on each row (ROW-WISE)


# In[106]:


#Arithmatic operations on multiple arrays


# In[108]:


arr1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr2 = np.array([[9,8,7],
                [6,5,4],
                [3,2,1]])

arr3 = np.array([[9,8,7,5],
                [6,5,4,2],
                [3,2,1,5]])


# In[109]:


arr1+arr2


# In[111]:


arr1+arr3 #for arithmatic operations on multiple arrays, arrays must have same shape


# In[112]:


arr1*arr2


# In[114]:


arr1.dot(arr2) 



#C[0][0]: Dot product of the first row of 𝐴 A and the first column of 𝐵 B:
#𝐶 [ 0 ] [ 0 ] = ( 1 × 9 ) + ( 2 × 6 ) + ( 3 × 3 ) = 9 + 12 + 9 = 30 C[0][0]=(1×9)+(2×6)+(3×3)=9+12+9=30
#𝐶 [ 0 ] [ 1 ] 𝐶 [ 0 ] [ 1 ] = ( 1 × 8 ) + ( 2 × 5 ) + ( 3 × 2 ) = 8 + 10 + 6 = 24 
#𝐶 [ 0 ] [ 2 ] C[0][2]: = ( 1 × 7 ) + ( 2 × 4 ) + ( 3 × 1 ) = 7 + 8 + 3 = 18 C[0][2]=(1×7)+(2×4)+(3×1)=7+8+3=18


# In[127]:


#Array sorting


# In[129]:


arr = np.array([[7,4,8,9,5], [1,5,8,9,10],[2,4,6,8,11]])
arr


# In[131]:


np.sort(arr, axis =1, kind = 'mergesort') #sort based on row as axis =1 


# In[132]:


np.sort(arr, axis =0, kind = 'mergesort') #sorting based on column as axis =0


# In[133]:


#Array  Merging -- Concatinate


# In[134]:


arr1 = np.array([[1,2,3,4],
                [5,6,7,8]])
arr2 = np.array([[8,7,6,5],
                [4,3,2,1]])


# In[135]:


arr1


# In[136]:


arr2


# In[138]:


np.vstack((arr1,arr2)) #Stcking Vertically


# In[140]:


np.hstack((arr1,arr2)) #Stcking Horizontally


# In[141]:


##note = for  0  axis we perform vertical stack and for axis 1 we perform horizintal stack


# In[144]:


np.concatenate((arr1,arr2), axis=1)


# In[146]:


arr = np.concatenate((arr1,arr2), axis=0)


# In[147]:


arr


# In[150]:


# simolar to stack, we can also split array in to 2
np.hsplit(arr , 2) 


# In[149]:


np.vsplit(arr, 2)


# In[154]:


## Array slicing is basically performing indexing based on the elemens you want to access


# In[152]:


arr1 = np.array([[1,2,3,4],
                [5,6,7,8],
                 [8,7,6,5],
                 [4,3,2,1]])


# In[153]:


arr1


# In[155]:


#for example i want to see all element except 1row amd 1 column
arr[1:,1:]


# In[157]:


#1st row
arr[:1,:] # first colon is used for rows and second colon is used for columns


# In[159]:


#i want 6,7
      #7,6  as result
arr[1: 3, 1:3]


# In[160]:


## Automating using Numpy


# In[161]:


arr = np.array([1,2,3,4,5,6,7,8,9,10])


# In[162]:


arr


# In[163]:


arr >5
# to find which how many values are greater then 5 in the array


# In[164]:


#to print elements along with it
arr[arr>5]


# In[165]:


len(arr[arr>5])


# In[166]:


#If we had to do the same for list we would have to write a for loop to find out a values that are greater than


# In[167]:


# find the values in array that are divisble by 3
arr[arr%3 == 0]


# In[173]:


m = np.array([23,45,24,23,424,23,31,42,21,3,242,353,5,5234,23])


# In[174]:


np.unique(m)


# In[177]:


np.unique(m, return_index = True) # give unique values and there index values 


# In[179]:


np.delete(m ,[2]) # 24 is deleted form m


# In[180]:


arr1 = np.array([[1,2,3,4],
                [5,6,7,8],
                 [8,7,6,5],
                 [4,3,2,1]])


# In[181]:


np.delete(arr1, [2],axis = 1) # 3rd column is deleted


# # Getting started with Pandas
# 

# In[4]:


import numpy as np
import pandas as pd


# In[5]:


lst = (1,2,3,4,5)


# In[6]:


np.array(lst)


# In[9]:


df = pd.Series(lst)


# In[10]:


df


# In[16]:


df = pd.DataFrame([lst,lst,lst])


# In[17]:


df


# In[18]:


del df #deleting datframe


# In[19]:


df


# In[23]:


df = pd.read_csv("https://gist.githubusercontent.com/DariaAlekseeva/299611a0daa6008685f7/raw/b431eb200bcafd2eba68a11ccbc80d051d3eeba9/titanic.csv")


# In[24]:


df


# In[22]:


#to see top 5 data


# In[25]:


df.head()


# In[26]:


#to see last 5


# In[27]:


df.tail()


# In[28]:


#how to find datatype of each column in the dataframe


# In[30]:


df.dtypes


# In[32]:


#Nan in Cabin denotes to the missing data
#pandas fill  null values with Nan


# In[34]:


df.describe() #it shows max, min , count , mean and standard deviation of the data


# In[36]:


df[['Passengers', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']]


# In[39]:


df.dtypes == object


# In[41]:


df.dtypes == 'float64'


# In[43]:


df[df.dtypes[df.dtypes == 'float64'].index] #it will only show the columns that have float type data


# In[44]:


df[df.dtypes[df.dtypes == 'int64'].index] #it will only show the columns that have integer type data


# In[45]:


df.head(15) #default gives first 5 data when i put particularly how much data i want to see it will show 


# In[46]:


#similarly for last data
df.tail(1)


# In[47]:


#what are the columns
df.columns


# In[48]:


#how to access one partiular column
df[['Ticket']]


# In[61]:


#INDEXING OR SLICING


# In[50]:


#for example now i want to see data between ticket 4 to 15
df[['Ticket']][4:16]


# In[55]:


# for example i want to see tickets with a gap of 2 like 4,6,8
df[['Ticket']][4:18:2]


# In[60]:


df[['Ticket','Cabin']][4:17:2] # doing same for multiple columns


# In[62]:


#How to create new column
df['new_col'] = 0


# In[63]:


df


# In[65]:


# if i want my column to be added to a particular location
df.insert(loc = 4, column = 'Last_name', value = 23)


# In[66]:


df


# In[70]:


df1 = df['Name'][:10]


# In[71]:


df1


# In[69]:


#as you see in the above result python gives an automated index starting from 0 to 9  


# In[72]:


#what if i want to edit this index based on me
t = ('n1', 'n2' ,'n3' , 'n4' ,'n5' ,'n6' ,'n7', 'n8' ,'n9', 'n10' )  #t represents the index i want 
pd.Series(df1 , index = t)


# In[74]:


pd.Series(list(df1), index = t)


# In[75]:


# Concatinating to datas
m1 = pd.Series([100,200,300,400,500], index = (1,2,3,4,5))


# In[76]:


m1


# In[77]:


m2 = pd.Series([600,700,800,900,1000], index = (1,2,3,4,5))


# In[79]:


m3 = pd.concat([m1,m2])


# In[80]:


m3


# In[81]:


#both the series are concated bu the problem arising is that 2 values hold same index
m3[2]


# In[ ]:


#Arithmatic Operations 


# In[82]:


m1*m2


# In[83]:


m1 + m2


# In[85]:


df.head()


# In[87]:


#how to delete any particular column


# In[89]:


df.drop('new_col')


# In[90]:


## while deleting a column you also have to mention along which axis do you want to delete, 
## so column(going from index to last column name) is axis 1 and rows is axis 0 (going vertically from row 1 to last row)


# In[91]:


df.drop('new_col', axis = 1)


# In[93]:


df


# In[94]:


#as you can see new_col is not permanently deleted, to delete it permanently you have to write inplace = true
df.drop('new_col', axis = 1, inplace = True)


# In[96]:


df # now new_col is permanently deleted


# In[97]:


# How to delete any particular row


# In[98]:


df.head()


# In[99]:


# i want to delete index 3
df.drop(3)


# In[100]:


# still it is not permanently deleted


# In[101]:


df.head()


# In[102]:


df.drop(3 , inplace = True)


# In[104]:


df  # Now it is permanently deleted


# In[105]:


df.drop('Last_name', axis = 1, inplace = True)


# In[106]:


df


# In[107]:


## How can i convert any particular column to index, for example i want name column to be set as index


# In[109]:


df.set_index('Name', inplace = True)  #inplace = true is necessary to make peranent changes


# In[110]:


df


# In[113]:


#Now how to reset the index
df.reset_index(inplace =True)


# In[114]:


df


# In[115]:


#how to create dataframe form dictionary


# In[118]:


d = {"key1": [1,2,3,4,5],
      "key2": [6,7,4,2,4],
      "key3":[ 2,9,6,4,2]}


# In[119]:


print(d)


# In[120]:


pd.DataFrame(d)


# In[121]:


dd = pd.read_csv("https://raw.githubusercontent.com/sonwaneshivani/Data-Science-Learning/refs/heads/main/taxonomy.csv")


# In[122]:


dd


# In[123]:


# DATA LINKS -- TITANIC - - https://gist.githubusercontent.com/DariaAlekseeva/299611a0daa6008685f7/raw/b431eb200bcafd2eba68a11ccbc80d051d3eeba9/titanic.csv


# In[124]:


# TAXONOMY - --https://raw.githubusercontent.com/sonwaneshivani/Data-Science-Learning/refs/heads/main/taxonomy.csv


# In[126]:


dd


# In[127]:


#How to remove Nan or null Values for rows


# In[130]:


dd.dropna(inplace = True)


# In[131]:


dd


# In[133]:


df1 = pd.read_csv("https://raw.githubusercontent.com/sonwaneshivani/Data-Science-Learning/refs/heads/main/taxonomy.csv")


# In[134]:


df1


# In[136]:


df1.dropna(axis=1) # this is how u drop columns that have nan/null values


# In[137]:


#how to fill values inplaces of Nan instead of deleting


# In[139]:


df1


# In[140]:


df1.fillna("Jayant")


# # Pandas Continued

# In[2]:


import pandas as pd
#to convert particular data to different data type
sr = pd.Series([1,2,3,4])


# In[3]:


sr


# In[4]:


sr.astype("float")


# In[5]:


sr.astype("str")


# In[6]:


sr = pd.Series([1,2,3,4,5,6,7,8,9,10])


# In[7]:


sr.between(10,50)


# In[8]:


sr.between(1,5)


# In[9]:


# Functions on strings
ds = pd.Series(['JAYANT', 'Varun', 'Python', 'RidhMa'])


# In[10]:


ds.str.upper()


# In[11]:


ds.str.lower()


# In[13]:


len(ds)


# In[14]:


for i in ds:
    print(len(i))


# In[15]:


ds = pd.Series(['    JAYANT  ', '  Varun  ', '  Python  ', '   RidhMa'])


# In[22]:


ds.str.strip() #it will remove extra spaces


# In[18]:


ds.str.contains('R')


# In[19]:


ds.str.replace('R', 'r')


# In[25]:


ds.str.count( 'A')


# In[27]:


ds.str.endswith('a')


# In[29]:


ds.str.startswith('')


# In[31]:


ds.to_list() #how to convert into a list


# In[32]:


m1 = pd.Series([100,200,300,400,500], index = (1,2,3,4,5))
m2 = pd.Series([600,700,800,900,1000], index = (1,2,3,4,5))


# In[39]:


m1.append(m2).reset_index() #another way to concat 


# In[2]:


import pandas as pd
#understanding drop once agaain
data = { 'one'   : pd.Series([1, 2, 3, 4]),
         'two'   : pd.Series([10, 20, 30, 40]),
         'three' : pd.Series([100, 200, 300, 400]),
         'four'  : pd.Series([1000, 2000, 3000, 4000])}


df = pd.DataFrame(data)
df


# In[3]:


df.drop([1,3], axis = 0)   # row wise drop


# In[7]:


df.drop(['one', 'four'], axis = 1) # column wise drop


# In[9]:


df.T #transpose 


# In[13]:


df.empty #it will tell if dataframe is empty or not


# In[15]:


df.sum()


# In[16]:


df.mean()


# In[17]:


df.median()


# In[18]:


df.mode()


# In[19]:


data = { 'one'   : pd.Series([1, 2, 3, 4]),
         'two'   : pd.Series([10, 20, 30, 40]),
         'three' : pd.Series([100, 200, 300, 400]),
         'four'  : pd.Series([1000, 2000, 3000, 4000])}


df = pd.DataFrame(data)
df


# In[20]:


df.describe()


# In[23]:


def add_(i,j):
    return i + j

df.pipe(add_, 10) #first we explained the function add_, now i want to aplly that function to whole dataset so il;l use pipe\
#df.pipe("functon we described", "by values we want the function to be performed")


# In[24]:


def sub_(i,j):
    return i-j

df.pipe(sub_, 11)


# In[25]:


def mean_(col):
    return col.mean()


df.pipe(mean_)


# In[26]:


def square(i):
    return i ** 2

df.pipe(square)


# In[27]:


df.pipe(mean_).pipe(square) #it returns mean square


# In[28]:


#Apply funtion


# In[29]:


#apply function will allow us to perform any function on a dataframe or any particular element of dataframe


# In[32]:


import numpy as np
df.apply(np.mean) #this returns mean


# In[35]:


df.apply(lambda x: x.max() - x.min()) # it is subtractin minimum values form maximum valus


# In[38]:


#we can also change index using re index
df.reindex([1,0,1,2])  # but unlike earlier along with index the values inside dataframe also get changed


# In[39]:


df.reindex([3,2,1,0])


# In[41]:


#sorting


# In[42]:


data = { 'one'   : pd.Series([2, 21, 1, 4]),
         'two'   : pd.Series([10, 202, 310, 40]),
         'three' : pd.Series([100, 20, 3100, 400]),
         'four'  : pd.Series([100, 20001, 3, 4000])}


df = pd.DataFrame(data)
df


# In[43]:


df.sort_values(by = 'one', ascending = False)


# In[46]:


df.sort_values(by = ['one', 'three'])


# In[ ]:


#GROUP BY FUNCTIONS IN PYTHON


# In[49]:


cricket = {'Team'   : ['India', 'India', 'Australia', 'Australia', 'SA', 'SA', 'SA', 'SA', 'NZ', 'NZ', 'NZ', 'India'],
           'Rank'   : [2, 3, 1,2, 3,4 ,1 ,1,2 , 4,1,2],
           'Year'   : [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
           'Points' : [876,801,891,815,776,784,834,824,758,691,883,782]}

df = pd.DataFrame(cricket)
df


# In[50]:


df.groupby('Team').groups


# In[51]:


df.groupby(['Team','Year']).get_group(('Australia',2014))


# In[52]:


df.groupby('Team')['Points'].sum()


# In[53]:


df = pd.read_csv("https://raw.githubusercontent.com/AshishJangra27/In-One-Go/refs/heads/main/Pandas/Football.csv")


# In[54]:


df


# In[55]:


# Data cleaning & Learning about your data


# In[56]:


df.info()


# In[57]:


df.isnull()


# In[60]:


df.isnull().sum() #it will count null values in each column


# In[62]:


df.describe(percentiles = [.80])


# In[64]:


de = df.copy() #how to copy a dataframe


# In[65]:


#so now any changes made in de will not be applicable to original data - df and de is a copy of df


# In[71]:


#unique values
df['Player Names'].unique() #this returns list of all unique names


# In[72]:


df['Player Names'].nunique() #this will give count of unique values


# In[73]:


#how to replace null values


# In[78]:


mis = round(df['Matches_Played'].mean(),0)
mis


# In[76]:


df.fillna(mis) # so 22 will be filled in nulls of matches played as avg value that is 22


# In[80]:


df.sample # it will always give  a random sample of  n values


# In[81]:


#how to save dat to csv


# In[82]:


data = { 'one'   : pd.Series([1, 2, 3, 4]),
         'two'   : pd.Series([10, 20, 30, 40]),
         'three' : pd.Series([100, 200, 300, 400]),
         'four'  : pd.Series([1000, 2000, 3000, 4000])}


df = pd.DataFrame(data)
df


# In[85]:


df.to_csv('Numbers', index = False) 
#this data frame will be saved as a csv file index = flase will remove index from csv i you want index then dont wrtie anything


# # A detailed Pandas Profile Report

# In[88]:


import matplotlib
import pandas_profiling as pp


# In[ ]:





# In[ ]:





# In[ ]:





# # Starting With Matplotlib

# In[90]:


import matplotlib.pyplot as plt


# In[91]:


#Linear Graph 
x = [1,2,3,4]
y = [5,6,7,8]


# In[94]:


plt.plot(x,y, color = "r") #color can be set according to you
plt.show()


# In[97]:


x = [5,2,9,9,7]
y = [10,5,8,4,2]
plt.plot(x,y, marker = "o")
plt.show()


# In[98]:


x = [5,2,9,9,7]
y = [10,5,8,4,2]
plt.plot(x,y, marker = "*")
plt.show()


# In[99]:


#how to plot x and y seperately


# In[4]:


import matplotlib.pyplot as plt
x = [5,2,9,9,7]
y = [10,5,8,4,2]
plt.plot(x,y, marker = "*", color = "g")
plt.plot(y, marker = "o")
plt.plot(x, marker = "^")
plt.show()


# In[5]:


#Bar Graph


# In[13]:


x = [1,2,3,4,5]
y= [6,7,8,9,10]
c = ('r', 'g', 'b', 'y', 'c')
plt.bar(x,y , color = c)
plt.show()


# In[23]:


import numpy as np
x = np.array(['a', 'b', 'c', 'd'])
y = np.array([5,4,6,2])
plt.barh(x,y, color = 'hotpink', height = 0.2) #width in normal bar graph is height in hbar graph so both work on width of bars pllotted

plt.show()


# In[21]:


x = [1,2,3,4,5]
y= [6,7,8,9,10]
c = ('r', 'g', 'b', 'y', 'c')
plt.bar(x,y , color = c, width = 0.5) #width can be set according to you for bars
plt.show()


# In[24]:


#Scatter plot


# In[28]:


x = np.linspace(1,90,10)
y = np.linspace(1,50,10)

plt.scatter(x,y)
plt.show()


# In[45]:


x = ([5,9,3,1,12])
y = ([10,22,11,29,10])

plt.scatter(x,y, color = 'hotpink' , s =200) # s = 200 increases the size of dots 
plt.xlabel("Month") #putting labels to x and y axis
plt.ylabel("Orders")
plt.title("Scatter Plot") #this will put a title above the graph 
plt.show()


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# In[10]:


#Converting an image into greyscale using matplotlib
fname = r'Imgggg.jpg'

#opening image using pil
image = Image.open(fname).convert('L')

#mapping image to greyscale
plt.imshow(image, cmap = 'gray')
plt.title('Flowers')
plt.show()


# In[11]:


#PIE chart


# In[12]:


x = ([10,20,30,40])
y = (['English', ' Maths', 'SST', 'Science'])


# In[14]:


plt.pie(x , labels = y)
plt.legend()
plt.show()


# # BLACK FRIDAY SALES PRACTICE

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("https://raw.githubusercontent.com/AshishJangra27/Data-Analysis-with-Python-GFG/refs/heads/main/20.%20Black%20Friday%20-%20Walkthrough/BlackFriday.csv")


# In[3]:


data


# In[4]:


data.info()


# In[5]:


#we can see that product category 2 and 3 have null values
data.isnull().sum()


# In[8]:


#Because 60% of data will be removed if we drop all null values, Therefore we will remove column product2 and 3 instead
# of deleteing 373299 rows


# In[9]:


del data['Product_Category_2']
del data['Product_Category_3']


# In[12]:


data.head()


# ## Analysis starts now

# In[13]:


data['User_ID'] #In the result we can see one user_id has bought multiple items


# In[ ]:





# In[23]:


data.nunique() #this tells us about data we will work for example it tells there are 5891 unique user and 3623 products


# In[24]:


data['Age'].unique()


# In[25]:


data['Occupation'].unique()


# In[27]:


data['Stay_In_Current_City_Years'].unique()


# In[28]:


data['Product_Category_1'].unique()


# In[31]:


data['Purchase'].sum()/len(data['Purchase']) #average spending per product


# In[32]:


#Analysing based on gender 


# In[37]:


len(data[data['Gender'] == 'M']) #Purchases made by men


# In[38]:


len(data[data['Gender'] == 'F']) 


# In[49]:


{'Ratio' : [len(data[data['Gender'] == 'M']), len(data[data['Gender'] == 'F'])]}


# In[61]:


df = pd.DataFrame({'Ratio' : [len(data[data['Gender'] == 'M']), len(data[data['Gender'] == 'F'])]}, index = ['Male', 'Female'])


# In[63]:


df.plot.pie(y = 'Ratio', figsize = (6,6), autopct = '%.1f')
plt.xlabel('Male')


# In[64]:


## Easy way to do the same 


# In[65]:


data.groupby('Gender').size()


# In[72]:


data.groupby('Gender').size().plot(kind = 'pie',title = 'Gender Ratio', figsize = (6,6), autopct = '%.1f')


# In[74]:


data.groupby('Gender').size().plot(kind = 'bar',title = 'Gender Ratio', figsize = (6,6))


# In[76]:


data.groupby('Gender').sum()['Purchase'] #Total amount spent by each gender


# In[77]:


data.groupby('Gender').sum()['Purchase'].plot(kind = 'pie' , autopct = '%.2f', figsize = (6,6))


# In[78]:


data.groupby('Gender').mean()['Purchase']  #Average money spent by each gender


# In[80]:


data.groupby('Gender').mean()['Purchase'].plot(kind = 'pie' , autopct = '%.1f',figsize = (6,6))


# In[1]:


#Analysisng AGE and Marital Status


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


data = pd.read_csv("BlackFriday.csv")


# In[4]:


data


# In[6]:


data.groupby('Age').size()  #no. of products purchased by different age group


# In[8]:


data.groupby('Age').size().plot(kind = 'bar', title = "Age Distribution", figsize = (12,6))


# In[9]:


for i in data['Age'].unique():   #all ages
    print(i)


# In[15]:


for i in data['Age'].unique():   #all gives count of all the rows of different age groups basically what groupby gave us
    
    print(i , ':', len(data[data['Age'] == i]))


# In[20]:


lst = []
for i in data['Age'].unique():   #this gives us all the products belonging to each age group 
       lst.append([i , data[data['Age'] == i]['Product_ID'].nunique()])


# In[21]:


lst


# In[22]:


df = pd.DataFrame(lst, columns = ['Age', 'Products']) #converting the above into a data frame


# In[23]:


df


# In[25]:


df.plot.bar(x = 'Age', figsize = (10,6))


# In[28]:


#create a graph to find amount spent by each age category
data.groupby('Age').sum()['Purchase'].plot(kind = 'bar', figsize = (12,6), title = "Amount Spending by Different Age groups")


# In[29]:


#create a chart for marital status


# In[34]:


data.groupby('Marital_Status').size().plot(kind = 'pie' , figsize = (6,6) , autopct = '%.1f', label = 'Marital_Status')


# In[35]:


# Multi Column Analysis


# In[43]:


import pandas as pd
import numpy as np


# In[44]:


data.head()


# In[48]:


sns.set(rc = {'figure.figsize': (12,6)})
sns.countplot(x = 'Age', hue = 'Gender', data = data )


# In[49]:


sns.countplot(x = data['City_Category'])


# In[50]:


data.groupby('City_Category').size().plot(kind = 'pie', autopct = '%.2f', figsize = (5,5))


# In[53]:


#city category and gender
sns.set(rc = {'figure.figsize':(12,6)})
sns.countplot(x = 'City_Category', hue = 'Gender', data = data)


# In[1]:


#Analysing the main part that is products along with occupation to get what people are buying wat


# In[2]:


import pandas as pd
import numpy as np


# In[4]:


data = pd.read_csv("BlackFriday.csv")
del data['Product_Category_2']
del data['Product_Category_3']


# In[5]:


data


# In[8]:


import seaborn as sns
sns.countplot(x = data['Stay_In_Current_City_Years']) #maximum no. of people in cities have been staying for  year


# In[9]:


import seaborn as sns
sns.countplot(x = data['Stay_In_Current_City_Years'], hue = data['Gender'])


# In[10]:


import seaborn as sns
sns.countplot(x = data['Stay_In_Current_City_Years'], hue = data['Marital_Status'])


# In[11]:


import seaborn as sns
sns.countplot(x = data['Stay_In_Current_City_Years'], hue = data['City_Category'])


# In[15]:


data.groupby('Stay_In_Current_City_Years').sum()['Purchase'].plot(kind = 'bar', figsize = (12,6))


# In[12]:


#Above plots show that we can target male unmarried from city B that have been staying in city for 1 year and
#many other ways based on above graphs


# In[16]:


sns.countplot(x = data['Occupation'])


# In[19]:


data.groupby('Occupation').sum()['Purchase'].sort_values().plot(kind = 'bar', figsize = (12,6))


# In[22]:


data.groupby('Occupation').sum()['Purchase'].sort_values()


# In[20]:


data.groupby('Occupation').mean()['Purchase'].sort_values().plot(kind = 'bar', figsize = (12,6))


# In[21]:


data.groupby('Occupation').mean()['Purchase'].sort_values()


# In[23]:


#Above analysis shows us that occupation 4 and 0 have done most purchases but when we see average(mean), 
#we can say that 12 & 17 are buying expensive products where as 4 & 0 are buynig less price but more quantity of products


# In[24]:


sns.countplot(x = data['Occupation'], hue = data['Gender']) ## This shows gender ratio of diff. occupations


# In[28]:


data.groupby('Occupation').nunique()['Product_ID'].sort_values().plot(kind = 'bar', figsize = (12,6))
#count of products for each occupation


# In[29]:


#mostly sold products


# In[30]:


data.groupby('Product_Category_1').size().sort_values().plot(kind = 'bar', figsize = (12,6))


# In[32]:


data.groupby('Product_Category_1').sum()['Purchase'].sort_values().plot(kind = 'bar', figsize = (12,6))
## Amount spent on each product categoty


# In[33]:


# Above graphs show highest values to be same that is product category 8,5 and 1 but if we look at rest of the graph
# we can say that product 13 has been sold more than 7 products but total sales of product 13 are least that means 
# product 13 has a low price compared to other products
#similarly 7 has been sold less no of times but revenue generated by it is more that means it price is above other products


# In[36]:


data.groupby('Product_ID').size().nlargest(10).plot(kind = 'bar', figsize = (12,6))
#Top selling PROducts


# In[37]:


#Gender and Marital Status


# In[46]:


for i in range(len(data)):
    print(data['Gender'][i]+ '_'+ str(data['Marital_Status'][i]))
## creating a list that gives gender and marital status of a person and adding it to the data


# In[47]:


l= []
for i in range(len(data)):
    l.append(data['Gender'][i]+ '_'+ str(data['Marital_Status'][i]))
l


# In[48]:


data['Gender_marital'] = l


# In[49]:


data


# In[50]:


sns.countplot(x = data['Gender_marital'])


# In[51]:


sns.countplot(x = data['Gender_marital'], hue = data['Age'])


# # Heart Disease Data Set

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv('heart.csv')


# In[5]:


df


# In[9]:


sns.displot(x = df['Age'] , kde = True, rug = True) 


# In[10]:


df.groupby('Sex').size().plot(kind = 'pie', figsize = (5,5), autopct = '%.2f')


# In[15]:


sns.displot(x = df['RestingBP'] ,bins = 15, kde = True, color = 'blue') 


# In[18]:


sns.displot(x = df['Cholesterol'] , kde = True, color = 'hotpink') 


# In[19]:


sns.displot(x = df['Oldpeak'] , kde = True, color = 'green') 


# In[20]:


df.groupby('ChestPainType').size().plot(kind = 'pie', figsize = (5,5), autopct = '%.2f')


# In[21]:


df.groupby('RestingECG').size().plot(kind = 'pie', figsize = (5,5), autopct = '%.2f')


# In[22]:


df.groupby('ST_Slope').size().plot(kind = 'pie', figsize = (5,5), autopct = '%.2f')


# In[23]:


df.groupby('HeartDisease').size().plot(kind = 'pie', figsize = (5,5), autopct = '%.2f')


# In[26]:


df.groupby('Sex').mean()['HeartDisease'].plot(kind = 'bar', figsize = (10,5))


# In[27]:


## VIOLIN PLOT


# In[29]:


sns.violinplot(y = df['Sex'], x = df['HeartDisease'])


# In[30]:


# 0  means person is not having heart disease, 1 means having the disease
## from the plot we can say males have more chances of having the disease whereas many females are in -ve that means 
#less chances of having the disease


# In[31]:


sns.violinplot(y = df['Age'], x = df['HeartDisease'])


# In[32]:


# above graph shows that avg age of not having disease is less than 55 years whereas avg age of having a disease is 
# above than 55 or around 60 years we can see that in the plot


# In[ ]:


# Correlation 


# In[33]:


df.corr(numeric_only = True) #closer to zero means lesser correaltion
#closer to one means more corrrelation


# In[34]:


sns.heatmap(df.corr(numeric_only = True))


# In[35]:


#Correaltion - JOINT PLOT


# In[36]:


sns.jointplot(x = 'Age', y= 'MaxHR' , data = df)


# In[37]:


sns.jointplot(x = 'Age', y= 'MaxHR' , data = df , kind = 'hex')


# In[38]:


sns.jointplot(x = 'Age', y= 'MaxHR' , data = df , kind = 'reg')
#regression lines shows that as age increases max hr decreases


# In[39]:


## PAIR PLOT - It will plot all the possible combinations for correlation


# In[40]:


sns.pairplot(df) #you should use pair plot when columns are limited not when column number is like 20, 30 or 100 only less than that


# In[ ]:




