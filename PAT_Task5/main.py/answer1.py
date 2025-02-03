#To Filter people under 18 

details=[{"name":"Aniha","age":24},{"name":"Jerusha","age":12},{"name":"Casey","age":16},{"name":"Joy","age":32}] #list of dictionary with names and ages of people

# Filtering people under 18
check_under_18 = lambda person: person["age"] < 18
under_18 = list(filter(check_under_18, details)) #using filter function to store only details of people under 18

# Mapping the rest to a new list
check_over_18=lambda p: p["age"] >= 18
over_18 = list(filter(check_over_18, details))

#Printing the Results
print("Under 18:", under_18)
print("Over_18:", over_18)




