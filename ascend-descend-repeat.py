def ascend_descend(length, minimum, maximum):
    # Your code here
    return ""

def ascend_descend(length, minimum, maximum):
    result = ""
    current_num = minimum
    step = 1

    for _ in range(length):
        result += str(current_num)

        # Switch direction if at the boundaries
        if current_num == maximum:
            step = -1
        elif current_num == minimum:
            step = 1

        # Move to the next number
        current_num += step

    return result


