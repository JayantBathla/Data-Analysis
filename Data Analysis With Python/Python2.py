#!/usr/bin/env python
# coding: utf-8

# In[1]:


#LOOPS 


# In[1]:


i =1
while i <=5:
    print('hello', i)
    i +=1


# In[2]:


i = 1
while i <=5:
    print(i)
    i += 1
    
print("Loop Ended")


# In[1]:


i = 5
while 0 < i :
    print(i)
    i -= 1
    
print("Loop Ended")


# In[2]:


i = 1
while i <=100:
    print(i)
    i += 1
    
print("Loop Ended")


# In[3]:


i = 100
while i >= 0:
    print(i)
    i -= 1
    


# In[5]:


n = int(input("Table of number:  "))
i =1
while i <= 10:
    print(n , 'x',i, '=', i*n)
    i += 1
        


# In[6]:


i = 1
while i <=10:
    print(i**2)
    i += 1


# In[2]:


tpl = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i <= len(tpl):
    if (tpl[i] == x):
         print("match found at", i)
            
    else: 
        print("finding")
    i+=1


# In[3]:


#break : loop will terminate/stop where we write break
i = 1
while i <=5:
    print(i)
    if (i == 3):
        break
    i += 1
    
print("Loop Ended")


# In[9]:


tpl = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(tpl):
    if (tpl[i] == x):
         print("match found at", i)
         break
            
    else: 
        print("finding")
    i+=1


# In[11]:


#Continue : it will terminate the current iteration and continue from next one.. Basically continue acts as skip

i = 0
while i <=5:
    
    if (i == 3):
        i+=1
        continue
    print(i)
    i += 1
    
print("Loop Ended")



# In[16]:


# printing odd numbers
i = 1
while i <=100:
    
    if (i%2 == 0):
        i+=1
        continue
    print(i)
    i += 1
    
print("Loop Ended")


# In[19]:


#even numbers

i = 1
while i <=100:
    
    if (i%2 != 0):
        i+=1
        continue
    print(i)
    i += 1
    
print("Loop Ended")


# In[20]:


#FOR LOOPS 


# In[22]:


i =1
for i in range(11):
    print(i**2)


# In[39]:


tpl = (1,4,9,16,25,36,49,64,81,100, 49)

#search for number x

 
x= 49
idx = 0
for i in tpl:
    if (i == x):
        print('found at', idx)
        idx += 1
    else:
        print("finding")
    


# In[42]:


# write a program to find the sum of first n natural numbers

n = int(input("sum of n numbers: "))
 
    
sum = 0    
for i in range(1, n+1):
    sum += i
    
print("total sum is", sum)




# In[51]:


n = int(input("sum of n numbers: "))
 
    
sum = 0 
i = 0
while  i < n:
    i +=1
    sum += i
    
print("total sum is", sum)


# In[1]:


## FUNCTIONS


# In[6]:


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    print(fact)
    
    
factorial(6)
    
    


# In[3]:


# write a for loop to execute the following pattern
# *
# **
# ***
# ****
# *****


# In[10]:


n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()


# In[9]:


#write a program to find factorial of a number


# In[19]:


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    print(fact)
    
    
factorial(10)

     
    


# In[20]:


# Count number of vowels in a string


# In[23]:


string = "My name is Jayant Bathla"
vowels = "aeiou"
count =0 
for char in string:
    if char.lower() in vowels:
        count += 1
print("no. of vowles are:", count)


# In[1]:


#find longest word in a sentence using forloop


# In[3]:


sentence = 'My name is Jayant Bathla'
words = sentence.split()  #it will split words on basis of space


# In[4]:


longest_word = ""
for word in words:
    if len(word)> len(longest_word):
        longest_word= word
print("Longest word is:", longest_word)


# In[5]:


#do-while loop 


# In[1]:


#fibonacci sequence


# In[ ]:





# In[3]:


n = int(input())
i = 0
for i in range(0, n+1):
    print(i**2)
    i +=1
    


# In[17]:


def is_leap(year):     
    if (year % 400 == 0) and (year % 4 == 0 ):
        
        return True
    elif (year%100 != 0):
        return True
    
    else:
        return False
    
is_leap(1999)


# In[18]:


#PANDAS DATA PREPROCESSING HOW TO HANDLE NULLS IN DIFFERENT CASES


# In[19]:


#IF Column holds numeric values


# In[20]:


import pandas as pd


# In[21]:


data = pd.read_csv("https://raw.githubusercontent.com/AshishJangra27/Data-Analysis-with-Python-GFG/refs/heads/main/3.%20Data%20Preprocessing%20-%20Removing%20Null%20Value%20Rows/googleplaystore.csv")


# In[22]:


data


# In[23]:


#finding avg value


# In[37]:


data['Rating' ]


# In[41]:


df = data.dropna()


# In[42]:


df


# In[43]:


df['Rating']


# In[47]:


sum(df['Rating'])/9360


# In[49]:


round(sum(df['Rating'])/9360,2)


# In[50]:


print("Average rating of these apps is:" ,round(sum(df['Rating'])/9360,2) )


# In[51]:


## How many apps are there with rating 5


# In[52]:


df['Rating']


# In[55]:


count = 0
for i in df['Rating']:
    if (i == 5.0):
        count += 1
print(count)


# In[56]:


## How many apps with rating in range 4 to 4.5

count = 0
for i in df['Rating']:
    if (i >= 4.0 and i <=4.5):
        count += 1
print(count)


# In[69]:


## Find sum of reviews
df['Reviews']


# In[68]:


s = 0
for i in df['Reviews']:
    s += int(i)
print(s)


# In[70]:


## Categorical data


# In[71]:


df.head()


# In[72]:


df['Category'].unique()


# In[73]:


# how to print above in better manner
for i in df['Category'].unique():
    print(i)


# In[75]:


len(df['Category'].unique()) ## total number of categories


# In[80]:


#find number of applications in art and design
count = 1
for i in df['Category']:
    if (i == "ART_AND_DESIGN"):
        count+=1
print(count)


# In[83]:


#type
df['Type'].unique()


# In[87]:


## Find How many Applications are free or paid

f = 1
for i in df['Type']:
    if (i == "Free"):
        f+=1
print(f)


# In[85]:


count = 1
for i in df['Type']:
    if (i == "Paid"):
        count+=1
print(count)


# In[91]:


print(f/(f+count) *100) #Percentage of free applications


# In[92]:


df['Content Rating'].unique() #all the content rating


# In[93]:


for i in df['Content Rating'].unique():
    print(i)


# In[94]:


#Automate Categorical


# In[95]:


#earlier we wrote for loop to find number of application in art and design but we cant keep repeating the process to find 
# count of each category so we will write nested for loop


# In[107]:


for name in df['Category'].unique():
    c = 1
    
    for i in df['Category']:
        if (i == name):
            c+=1
    print(name , c)
    


# In[116]:


#Total number of apps in each conten rating
content_ratings = {}
for name in df['Content Rating'].unique():
    c = 1
    
    for i in df['Content Rating']:
        if (i == name):
            c+=1
    content_ratings[name] = c
print(content_ratings)
    


# In[118]:


## Null Values Handling


# In[ ]:





# In[119]:


df = pd.read_csv("https://raw.githubusercontent.com/AshishJangra27/Data-Analysis-with-Python-GFG/refs/heads/main/7.%20Null%20Values%20Handling%20-%20Numeric/Data.csv")


# In[120]:


df


# In[127]:


## How to analyze if you dont want to drop nulls
get_ipython().system('pip install sklearn')


# In[131]:


from sklearn.impute import SimpleImputer
import numpy as np


# In[132]:


# How to fill null values using imputer


# In[135]:


imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')


# In[138]:


df.iloc[:,1:3].values


# In[140]:


imputer.fit(df.iloc[:,1:3].values)
x = imputer.transform(df.iloc[:,1:3].values)


# In[141]:


x


# In[142]:


df.iloc[:,1:3] = x


# In[144]:


df # as you can see null values in age and salary are filled with avg values of those columns


# In[148]:


#How to deal with categorical null values


# In[149]:


imputer = SimpleImputer(missing_values = np.nan , strategy = 'most_frequent')
imputer.fit(df.iloc[:,:1].values)
x = imputer.transform(df.iloc[:,:1].values)


# In[153]:


df.iloc[:,:1] = x


# In[154]:


df #NUll value is filled with france as it was most occuring country same can be done for Purchased column


# In[155]:


#applying this to whole data instead on particular columns


# In[156]:


imputer = SimpleImputer(missing_values = np.nan , strategy = 'most_frequent')
imputer.fit(df.iloc[:,:].values)
data = imputer.transform(df.iloc[:,:].values)


# In[160]:


df.iloc[:,:] = imputer.transform(df.iloc[:,:].values)


# In[161]:


df


# In[162]:


## NOW WORKING ON GOOGLE PLAY STORE DATASET NULL VALUES USING IMPUTER


# In[163]:


df = pd.read_csv("https://raw.githubusercontent.com/AshishJangra27/Data-Analysis-with-Python-GFG/refs/heads/main/3.%20Data%20Preprocessing%20-%20Removing%20Null%20Value%20Rows/googleplaystore.csv")


# In[164]:


df.head()


# In[168]:


df.isnull().sum()


# In[169]:


imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')


# In[171]:


df.iloc[:,2:3].values


# In[172]:


imputer.fit(df.iloc[:,2:3].values)
x = imputer.transform(df.iloc[:,2:3].values)


# In[174]:


df.iloc[:,2:3]= x


# In[175]:


df


# In[176]:


imputer = SimpleImputer(missing_values = np.nan , strategy = 'most_frequent')
imputer.fit(df.iloc[:,11:13].values)
data = imputer.transform(df.iloc[:,11:13].values)


# In[177]:


df.iloc[:,11:13] = data


# In[178]:


df


# In[179]:


df.isnull().sum()


# In[188]:


df1 = df.dropna()


# In[189]:


df1.isnull().sum()


# In[1]:


#Multiple Columns, dealing with multiple columns can be done by using indexing


# In[2]:


#for example i want to find number of apps in art and design that are also free


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


data = pd.read_csv("https://raw.githubusercontent.com/AshishJangra27/Data-Analysis-with-Python-GFG/refs/heads/main/3.%20Data%20Preprocessing%20-%20Removing%20Null%20Value%20Rows/googleplaystore.csv")


# In[7]:


df = data.dropna()


# In[8]:


df


# In[24]:


df = df.values


# In[25]:


c = 0
for i in df:
    if(i[1] == 'ART_AND_DESIGN' and i[2] >= 4.5):
        c += 1
print(c)   


# In[27]:


c = 0
for i in df:
    if(i[1] == 'ART_AND_DESIGN' and i[6] == 'Free'):
        c += 1
print(c)


# In[28]:


# Using Conditions


# In[ ]:





# In[34]:


data[data['Category'] == 'ART_AND_DESIGN'] #It is only returning rows that have category art and design


# In[35]:


df1 = data[data['Category'] == 'ART_AND_DESIGN']


# In[36]:


df1[df1['Type'] == 'Free']  #art and design apps that are free


# In[37]:


#how many apps are there in family with rating> 4.5 and free


# In[39]:


df2 = data[data['Category'] == 'FAMILY']


# In[40]:


df3 = df2[df2['Type'] == 'Free']


# In[41]:


df3[df3['Rating']> 4.5]


# In[42]:


#only print names
df3[df3['Rating']> 4.5]['App']


# In[44]:


#SORTING


# In[45]:


df3.sort_values(by = 'Rating', ascending = True)


# In[46]:


#only print top 10 of above result


# In[48]:


df3.sort_values(by = 'Rating', ascending = True).head(10)


# In[49]:


#groupby


# In[50]:


data.groupby('Category').mean()['Rating']


# In[53]:


## find how many apps are there in each category using groupby
df= data.dropna()


# In[59]:


df.groupby('Category').count()['Type'].sort_values(ascending = True)


# In[ ]:




