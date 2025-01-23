#To find the min element

# Unsorted list
list1 = [5, 2, 9, 1,34,2,7,4,9,0,45]
# Sort the list
list1.sort()  # Sorts the list in place
# Find the minimum element
if list1:  # Check if the list is not empty
    min_element = list1[0]
    print("The minimum element in the list is:", min_element)
else:
    print("The list is empty")
