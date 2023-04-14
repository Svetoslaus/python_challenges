def get_count(input_str):
  vowels = ['a','e','i','o','u']
  count = 0
  for char in input_str:
    if char in vowels:
      count += 1
  return count

test.assert_equals(get_count("abracadabra"), 5)
