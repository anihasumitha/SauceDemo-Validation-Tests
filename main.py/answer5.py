#All the ways to make Rs.10

coins=[1,2,5,10] # The coins we use to try to get Rs.10
output_10=[] #E mpty list to store all possible combinations

# Nested loops to explore all possible uses of each coin
for a in range(2):  # Rs. 1 can be used 0 or 1 times
    for b in range(2):  # Rs. 2 can be used 0 or 1 times
        for c in range(2):  # Rs. 5 can be used 0 or 1 times
            for d in range(2):  # Rs. 10 can be used 0 or 1 times
                # Check if the combination sums to Rs. 10
                if a * 1 + b * 2 + c * 5 + d * 10 == 10:
                    output_10.append((a, b, c, d))

# Print the total number of combinations
print(f"Total number of ways to make Rs.10 out of Rs.1, Rs.2, Rs.5 and Rs.10 : {len(output_10)}")
