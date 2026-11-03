# Write a function named multiply_digits(num).
#1. Ask the user to enter an integer.
#2. Use a while loop inside the function.
#3. Extract each digit from the number.
#4. Multiply all the digits together.
#5. Return the final multiplication result.

def multiply_digits(num):
    num=abs(num)

    if num==0: # handling 0
        return 0
    
    prod=1

    while num > 0:
        digit = num % 10
        prod = prod * digit
        num = num // 10

    return prod

num=int(input("Enter the number you want to multiply: "))
print("You have entered: ",num)

multi_num=multiply_digits(num)

print("The multiplied number is: ",multi_num)
