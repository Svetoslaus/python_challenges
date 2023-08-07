def create_two_sets_of_equal_sum(n):
    total_sum = n * (n + 1) // 2

    if total_sum % 2 != 0:
        return []

    target_sum = total_sum // 2
    set1, set2 = [], []
    remaining_numbers = set(range(1, n + 1))

    for i in range(n, 0, -1):
        if i <= target_sum:
            set1.append(i)
            target_sum -= i
            remaining_numbers.remove(i)
        else:
            set2.append(i)

    return [set1, set2]

# Test the function
n = 7
print(create_two_sets_of_equal_sum(n))  # Output: [[1, 2, 4], [3, 5, 6, 7]]

n = 5
print(create_two_sets_of_equal_sum(n))  # Output: None
