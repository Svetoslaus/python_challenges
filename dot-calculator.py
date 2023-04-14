def calculator(equation):
  nums = equation.split()
  if len(nums) != 3:
    return "Invalid equation!"

  dots1 = len(nums[0])
  dots2 = len(nums[2])
  operator = nums[1]

  if operator == "+":
    return "." * (dots1 + dots2)
  elif operator == "-":
    return "." * max(0, dots1 - dots2)
  elif operator == "*":
    return "." * (dots1 * dots2)
  elif operator == "//":
    return "." * max(0, dots1 // dots2)
  else:
    return "Invalid operator!"

print(calculator("..... + ..............."))  # "...................."
print(calculator("..... - ..."))  # ".."
print(calculator("..... - ."))  # "...."
print(calculator("..... * ..."))  # "..............."
print(calculator("..... * .."))
