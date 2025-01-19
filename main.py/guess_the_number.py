# 1. Guess the number:

import random

list_range= [*range(1,101)] #range of numbers from 1 to 100 in a list
random_number= random.choice(list_range)
print("Hello! Let's Play a game!\nYou can guess a number between 1 and 100 and I'll check if you got it right")

# print(random_number), if you want it printed

while True:  #to keep the user guessing until they get the right number 
    try:
        user_guess=int(input("Enter your guess\n")) #getting a number guessed by the user
    
        if (user_guess<random_number):

            print("Your guess is too low ")
    
        elif (user_guess>random_number ):
        
            print("Your guess is too high ")

        else:
            print("YAY, You have guessed the number right")
            break #exit loop once the user has guessed the number right

        
    except ValueError:
        print("Please enter a valid integer")