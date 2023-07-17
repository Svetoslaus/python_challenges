def variance(words):
    # Calculate the total number of words
    total_words = len(words)

    # Calculate the expected value E[X]
    expected_value = sum(len(word) for word in words) / total_words

    # Calculate the variance E[(X - E[X])^2]
    variance = sum((len(word) - expected_value) ** 2 for word in words) / total_words

    # Round the variance to 4 decimal places
    variance = round(variance, 4)

    return variance


# Test examples
words_example1 = ["Hello", "World"]
words_example2 = ["Hi", "World"]

print("Variance for Example 1:", variance(words_example1))  # Output: 0.0
print("Variance for Example 2:", variance(words_example2))  # Output: 2.25
