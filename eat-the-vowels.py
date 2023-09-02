user_word = input().upper()
word_without_vowels = ""

for letter in user_word:
    
    if letter in "AEIOU":
        continue
    
    word_without_vowels += letter



for letter in word_without_vowels:
   print(letter)
