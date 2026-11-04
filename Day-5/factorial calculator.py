# Write a function named calculate_factorial(n).
# Requirements:
# 1. Accept an integer from the user.
# 2. Calculate the factorial using a loop.
# 3. Return the final result.
# 4. Handle negative numbers.
# 5. Remember that the factorial of 0 is 1.

def calculate_factorial(n):
    if n==0:
        return 1
    elif n<0:
        return "Invalid Input! please try another number"
    f=1
    for i in range (1, n+1):
        f=i*f
    return f

num=int(input("Enter the number: "))
print("You have entered: ",num)
fact=calculate_factorial(num)
print("The factorial of the number is: ",fact)