# To find the triplet in the list whose sum is equal to 59


list1= [10, 20, 30, 9]
sum = 59
triplets = []

# Length of the list
n = len(list1)

# Finding triplets; considers individual element against the next, to check the sum 
# and appends the elements to  new list called triplets
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if list1[i] + list1[j] + list1[k] == sum: 
                triplets.append((list1[i], list1[j], list1[k]))

# Print the results
print("Triplets with sum equal to", sum, "are:", triplets)

