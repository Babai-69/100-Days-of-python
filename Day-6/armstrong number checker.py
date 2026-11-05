# Your task: Write a function named is_armstrong().

# Requirements
# 1. Accept an integer from the user.
# 2. Count the total number of digits.
# 3. Raise each digit to the power of the total number of digits.
# 4. Add all the results.
# 5. Return True if the sum equals the original number.
# 6. Otherwise, return False.
# 7. Negative numbers should return False.

def is_armstrong(x):
    
    if x<0:
        return "Invalid number!"

    old_x=x
    s=0
    digits = len(str(x))
    
    while x>0:
          rev=x%10
          s=s+rev**digits
          x=x//10

    if s==old_x:
            return "armstrong number"
    else:
            return "not an armstrong number"

num=int(input("Enter the number: "))
print("You have entered: ",num)
armstrong=is_armstrong(num)
print("The number is: ",armstrong)