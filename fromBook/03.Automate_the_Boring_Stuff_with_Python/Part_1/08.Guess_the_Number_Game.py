#!/usr/bin/env python
# coding: utf-8

# In[27]:


# This is a "Guess the Number Game"

import random

secretNumber = random.randint(1,100)
print("I'm thinking of a number between 1 and 100!")

# Ask the player to guess 6 times

for guessTaken in range(1,6):
    print("Take a Guess: ")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your Guess is Low!")
    elif guess > secretNumber:
        print("Your Guess is High!")
    else:
        break # This condition is the corrent guess!
    remainAttemps = 5 - guessTaken
    if remainAttemps == 0:
        print(str(remainAttemps) + " attemps remain! Try again!!")
    else:
        print(str(remainAttemps) + " attemps remain! Try harder!!" + "\n")
        
if guess == secretNumber:
    print ("Good Job! You guessed my number in " + str(guessTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber) + "!")


# In[ ]:




