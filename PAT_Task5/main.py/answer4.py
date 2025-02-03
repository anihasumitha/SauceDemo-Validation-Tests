#Check if a given string is number or not

input_string = input("Enter a string: ")  # Gets an input that is a string

#Using lambda function to replace the first '.' , to remove any '+' or '-' that is in front of the number and to check if the rest are digits
# We check to see if the decimal point occurs only once
is_number = lambda input: input.replace('.','',1) .lstrip('+-') .isdigit() if (input.count('.') <=1 ) else False

#If the decimal point occurs more than once, it returns False, else true
# When true, the if block executes
if is_number(input_string):  
    print("It is a number")
# When False, the else block executes
else:
    print("It is not a number")