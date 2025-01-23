#Even and Odd List

list1=[10,501,22,37,100,999,87,351]
even_list=[]
odd_list=[]
length=len(list1)
print("Default List :",list1)

# For loop to check through the elements of the list
for i in range(length): 
    ele=list1[i] 
    #Checks if the element is divisible by 2, hence even
    if ele%2 == 0: 
    #If it is, it inserts the element to a new list
        even_list.append(ele) 
    else: #or else it is odd
        odd_list.append(ele) # it inserts this to another list which is specific for odd numbers

#prints out both lists
print("List with even numbers : ",even_list) 
print("List with odd numbers : ",odd_list)










