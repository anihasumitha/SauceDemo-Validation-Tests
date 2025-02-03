#Fibonacci Series

from functools import reduce #importing reduce function

n=int(input("Enter the limit for fibonacci series\n"))

def fib_series(num):
    first =[0,1]
    for i in range(0,num-2):
        first.append(reduce(lambda x,y : x+y,first[-2:])) #adding the last two digits of the list and adding them to the end of the list
    print("Fibanocci Series:\n",first) #printing the series till the limit 

fib_series(n) #calling the fib_series function

