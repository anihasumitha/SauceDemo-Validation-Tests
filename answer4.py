#Sum of First and last digit of a number

num=int(input("Enter a number\n")) #Getting integer input from user

last_digit=num%10 #extracting last digit from the input

first_digit=num
while(first_digit>9):
    first_digit=first_digit/10 #repeating this until we get the first digit 

sum=first_digit+last_digit #adding the first and last digits
print(f"Sum of first and last digits of the number {num} are ",int(sum)) #printing the sum output
