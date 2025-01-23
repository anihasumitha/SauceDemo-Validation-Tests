#To find duplicates in three lists

list1=[2,3,4,5,6]
list2=[4,2,10,7]
list3=[23,45,3,8,10,2]

result=[]
for element in list1: #Iterating through the list1 and checking with the elemnts in list1 and list2
    if element in list2 or element in list3:
        if element not in result:
            result.append(element)

# Print the duplicates
print("Duplicates in all three lists:", result)
