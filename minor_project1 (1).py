#!/usr/bin/env python
# coding: utf-8

# In[1]:


Password ="1234"
attempts = 3
while attempts > 0:
   guess=int(input("Enter the Password: "))
   if guess == Password:
      print("Correct password")
      break
   else:
      attempts -= 1  
      print("Incorrect Password.Try again later")
if attempts == 0:
   print("No attempts left. Access denied.")  


# In[ ]:





# In[ ]:





# In[ ]:




