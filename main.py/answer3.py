#Count the happy numbers in list

list1 = [10, 501, 22, 37, 100, 999, 87, 351]
happylist = []
count=0

for ele in list1:  # Take individual elements in the list using for loop
    num = ele
    ite = 0  # Initialize a counter for the  number of iterations

    while num != 1 and ite < 100:  # Limit iterations to 100, to avoid infinite loops
        sum = 0  # Reset sum for each number
        while num > 0:
            digit = num % 10
            sum += digit ** 2  # Add the square of the digit
            num //= 10  # Using division to remove the last digit
        num = sum  # Update num to the new sum
        ite += 1  # Increment the iteration counter

    if num == 1:  # If it reaches 1, it's a happy number
        happylist.append(ele)
        count+=1

# Print the happy numbers and their count
print(f"There are {count} Happy numbers in the list:", happylist)


