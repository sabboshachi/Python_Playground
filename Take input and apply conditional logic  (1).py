#!/usr/bin/env python
# coding: utf-8

# In[3]:


saarc = ["Bangladesh", "India", "Nepal", "Srilanka", "Bthutan", "Afganistan", "Pakistan"]
country = input ("Enter the name of your country:")
if country in saarc:
    print ("Your country is a member of SAARC")
    
else:
    print("Your country is not a member of SAARC")
    
        


# In[9]:


marks = input ("Enter your marks:")
marks = int(marks)

if marks >= 80:
    print("You got A+")
elif marks >= 70:
    print ('You got A')
elif marks >= 60:
    print ('You got A-')
elif marks >= 50:
    print ("You got B")
elif marks >= 40:
    print ("You got C")
else:
    print("Fuck,,, You are failed")


# In[14]:


num = input("Enter a nnmber")
num = int(num)
if num > 0:
    print ('The Number is Positive')
elif num < 0:
    print ("The number is Negative")
else:
    print ("THe number is zero")


# In[26]:


num = input("Enter a Mumber:")
num = int(num)

num_1 = 2

if num % 2 == 0:
    print ('THe number is even')
else:
    print("The number is odd")


# In[36]:


year = input("Enter a Year:")
year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ( year, " year is a Leap Year")
        else:
            print ( year, " year isn't a Leap Year")
    else:
        print ( year, " year is a Leap Year")
else:
    print( year, " year isn't a Leap Year")


# In[ ]:




