def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

# Test cases
print(is_leap_year(2000))  # True
print(is_leap_year(2020))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2023))  # False
