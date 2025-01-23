#To find sub-list with sum equal to zero

list1 = [4, 2, -3, 1, 6]
#Initializing sublist_found as false so that if a sublist with sum 0 is found, it can be used to break out of loop
sublist_found = False

# Finding sublists with sum equal to zero
for i in range(len(list1)):
    for j in range(i + 1, len(list1) + 1):
        sublist = list1[i:j]  # Get the sublist from index i to j-1
        if sum(sublist) == 0:
            print("Sublist with sum equal to zero is:", sublist)
            sublist_found = True
            break  # Stop searching after finding the first sublist
    if sublist_found:
        break  # Exit the outer loop if a sublist is found

if not sublist_found:
    print("No sublist with sum equal to zero found.")
