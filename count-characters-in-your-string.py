def count(input_string):
    # Initialize an empty dictionary to store the character counts
    char_counts = {}

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_counts[char] = 1

    return char_counts

