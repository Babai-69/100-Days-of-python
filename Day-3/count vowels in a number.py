# Write a function named count_vowels(text), that counts how many vowels are present in the given text.
# Accepts a sentence.
# Counts how many vowels (a, e, i, o, u) are present.
# Returns the total number of vowels.
def count_vowels(text):

    vowel=0
    for letter in text:
        if letter in "aeiou":
            vowel=vowel+1
    return vowel

text=input("Enter the text: ").lower() # lower() is use so that if user paste captal letter it converts into small or lowercaps
print("You have written: ",text)
# word= text.split() # For beginners don't use it right now

# for word in text.split(): # Using split function to breakdown the full text into words
#    for letter in word:
#        print("The letter is: ",letter)
        
vowel=count_vowels(text)

print("The total number of vowels are: ", vowel)