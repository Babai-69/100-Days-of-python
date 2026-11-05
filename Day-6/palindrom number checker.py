# Write a function named is_palindrome().

# Requirements:
# 1. Accept an integer from the user.
# 2. Check whether the number reads the same forward and backward.
# 3. Return True if it is a palindrome.
# 4. Return False otherwise.
# 5. Handle negative numbers (negative numbers should return False).

def is_palindrome(x):

    if x<0:
        return "Invalid number! please retry a new number"
    
    n=0
    x1=x # Storing the num into a variable
    while x>0:

        digit=x%10
        n=(n*10)+digit
        x=x//10

    if n==x1: # Checking if the variable is equals to the number or not after the program executes
        return "Palindrome"
    else:
        return "Not Palindrome"

num=int(input("Enter your number: "))
print("You have entered: ", num)

palindrom=is_palindrome(num)
print("Your number is: ",palindrom)