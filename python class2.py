#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.Type Conversion


# In[4]:


x= 10
y= float(x)
print(type(y))


# In[2]:


x=10
y=10.5
print(type(x+y))


# In[ ]:


#Bill Calculator


# In[32]:


a= input("product")
b=int(input("quantity in L"))
price=100
total=price*b
print("total",total)


# 2.control statement

# In[25]:


a=10
if a>15:

    print("hello")


# In[28]:


a=10
if a<15:
    print("hello")


# In[ ]:


if-else


# In[33]:


a=10
if a>15:
    print("hello")
else:
    print("bye")


# In[44]:


a=int(input("enter the number")) 

if x>0:
    print("negative")
else:
    print("positive")
    


# In[90]:


a=int(input("enter age"))
if a<=13:
     print('Child')
elif a<18:
    print("Teen")
else:
    print('Adult')


# In[51]:


a=int(input("enter marks"))
if a>= 40:
    print("pass")
else:
    print("fail")


# In[ ]:


#nestead if question


# In[74]:


month=input("Month: ")
if month in ['jan', 'feb' , 'november', 'december']:
     print("winter")
elif month in ['may' , 'june' , 'july' , 'august'] :
     print("summer")
elif month in ['march' , 'april']:
     print("spring")
elif month=='september':
     print("autum")
else:
     print("autum")


# In[77]:


Vehicle=input("Type of vehicle: ")
year=int(input("buying year: ")) 
if Vehicle in ['car', 'scooty', 'bike']:
               print("always check expiry date ")
if year>15:
       print("already expire")
elif year<15:
       print("5 years still left")
else:
    print("please calculate")


# In[86]:


x = 3
if x == 5:
    print('Five')
elif x == 3:
    print('Three')
else:
    print('Other')


# In[88]:


a=int(input("enter the number")) 

if x<0:
    print("negative")
elif x==0:
    print("zero")
else:
    print("positive")


# In[91]:


a=int(input("enter the number")) 

if a/2:
    print("Even")
if a>10:
    print('It is greater than 10')


# In[94]:


a=int(input("enter marks"))
if a>90:
    print("A")
elif a>75:
    print("B")
elif a>60:
    print("C")
else:
    print("fail")


# In[1]:


a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b & a>c:
    print("first number is greatest")
elif b>a & b>c:
    print("second number is greatest")
    
else:
    print("third number is greatest")


# In[ ]:




