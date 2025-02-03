#Extracting Year, Month and Day from a datetime object

from datetime import datetime

user_input_date =input("Enter todays date in YYYY-MM-DD format") #getting user input
formatted_date = datetime.strptime(user_input_date, "%Y-%m-%d") #formats the user input to YYYY-MM-DD format

#Using lambda function to extract year, month and day
result_year= lambda y : y.year
result_month= lambda y : y.month
result_day= lambda y : y.day

print(f"Year : {result_year(formatted_date)}\nMonth :{result_month(formatted_date)}\nDate : {result_day(formatted_date)}")
