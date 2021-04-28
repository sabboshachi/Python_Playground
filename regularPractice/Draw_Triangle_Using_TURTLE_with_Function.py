#!/usr/bin/env python
# coding: utf-8

# In[10]:


import turtle

def arms(arm_length):
    for i in range(3):
        turtle.forward(arm_length)
        turtle.left(120)
counter = 0
while counter < 1:
    arms(200)
    turtle.left(5)
    counter += 1
turtle.exitonclick()


# In[ ]:




