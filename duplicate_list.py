my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

duplicate = []


for number in my_list:
   if number not in duplicate:
       duplicate.append(number)

print("The list with unique elements only:")
print(duplicate)
