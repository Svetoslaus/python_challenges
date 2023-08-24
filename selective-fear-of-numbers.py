def am_I_afraid(day, num):
    if day == "Monday":
        return num == 12
    elif day == "Tuesday":
        return num > 95
    elif day == "Wednesday":
        return num == 34
    elif day == "Thursday":
        return num == 0
    elif day == "Friday":
        return num % 2 == 0
    elif day == "Saturday":
        return num == 56
    elif day == "Sunday":
        return num == 666 or num == -666
    else:
        raise ValueError("Invalid day of the week")


day = "Monday"
num = 12
result = am_I_afraid(day, num)
print(f"Fear triggered: {result}")
