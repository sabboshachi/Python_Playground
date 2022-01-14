#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle 

turtle.shape("turtle")
turtle.color("blue")
turtle.speed(2)

counter = 0
while counter < 54:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(7.5)
    counter += 1
turtle.exitonclick()


# In[ ]:




