#Count and Print all prime numbers in a list

import math #importing math function since we used sqrt 
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
primelist = []
count = 0

for ele in list1:
    if ele < 2:  #If the element is less than 2, it would not be prime
        continue
    if ele == 2:  #2 is a prime number
        primelist.append(ele)
        count += 1
        continue
    if ele % 2 == 0:  #If element is an even number, it is not prime
        continue

    # For numbers greater than 2
    prime_no = True
    for i in range(3, int(math.sqrt(ele)+ 1), 2):  #Checks from 3 to the number's divisor itself with an increment of 2
        if ele % i == 0: #Checks if the element is divisible upto its divisor
            prime_no = False
            break

    if prime_no == True:  # If the number is still prime
        primelist.append(ele)
        count += 1

print(f"The New list {primelist} has {count} prime numbers")

