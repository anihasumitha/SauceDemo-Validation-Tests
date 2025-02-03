# Product of all numbers in a list

from functools import reduce

list1=[5,2,10,4] #a list 

product = lambda num1, num2: num1*num2 #finding the product of the numbers in list1 using lambda function

result = reduce(product, list1) #using reduce function to reduce the list to a single output
print("The product of all numbers in the list is",result) #printing the single value output which would be 400 as a result of the multiplication
