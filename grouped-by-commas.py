def group_by_commas(n):
    # Convert the integer to a string
    num_str = str(n)
    
    # Initialize an empty list to store the grouped digits
    grouped_digits = []
    
    # Loop through the string in reverse
    for i, digit in enumerate(reversed(num_str)):
        # Add a comma after every 3 digits (except for the last group)
        if i > 0 and i % 3 == 0:
            grouped_digits.append(',')
        grouped_digits.append(digit)
    
    # Join the list and reverse it to get the correct order
    grouped_digits.reverse()
    
    # Convert the list of characters back to a string and return it
    return ''.join(grouped_digits)

# Test cases
print(group_by_commas(1))        # Output: "1"
print(group_by_commas(10))       # Output: "10"
print(group_by_commas(100))      # Output: "100"
print(group_by_commas(1000))     # Output: "1,000"
print(group_by_commas(10000))    # Output: "10,000"
print(group_by_commas(100000))   # Output: "100,000"
print(group_by_commas(1000000))  # Output: "1,000,000"
print(group_by_commas(35235235)) # Output: "35,235,235"
