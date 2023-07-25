def add_check_digit(number):
    factors = [2, 3, 4, 5, 6, 7]
    product_sum = sum(int(digit) * factors[i % 6] for i, digit in enumerate(number[::-1]))
    remainder = product_sum % 11
    check_digit = 11 - remainder if remainder > 1 else 0 if remainder == 0 else 'X'
    return number + str(check_digit)
