#A new list with squares of the even numbers in a list

list1=[1,5,10,3,4,80,26,7] #the given list
print("The original list:",list1) 

check_even = lambda num : num%2==0 #checks if the number is even or odd
even_list=list(filter(check_even,list1)) # creates a list called even_list with all even numbers from list1

even_square = lambda data : data ** 2 #Squares the even numbers
print("List of squares of all even numbers in the original list: ",list(map(even_square,even_list))) #calculates and prints the square of all the numbers in even_list 


