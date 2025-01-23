#To find first non-repeating element

list1 = [2,3,4,6,3,5,5,6,9,2]
count = {} #list to store the counted numbers

# Count the occurrences of each integer
for num in list1:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
        
# Find the first non-repeating integer
first_non_repeating = None
for num in list1:
    if count[num] == 1:
        first_non_repeating = num
        break

# Print the result
if first_non_repeating is not None:
    print("The first non-repeating integer is:", first_non_repeating)
else:
    print("There are no non-repeating integers in the list.")
