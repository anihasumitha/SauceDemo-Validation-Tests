
#2.Word Scramble

import random

words=["python","javascript","java","automation","pytest","guvi","selenium"]

random_word= random.choice(words) #chooses a random word from the list "words"
length=len(random_word)
jumbled_word=''.join(random.sample(random_word,length)) #scrambling the word using random.sample and joining them together with the join function

print("Hello! Let\'s try unscrambling a jumbled word! ")

while True:
    

    user_guess=input(f"Unscramble the word \"{jumbled_word}\" and Enter your answer\n") #get user input

    if(user_guess==random_word): #checking if the user entered input and the unscrambled word matches and this block executes if it is true
        print("You have guessed it right")
        break
        
    else:  #this block executes if the condition is not true
        print("Incorrect answer. Try again!") 




    

