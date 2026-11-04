# Write a function to check whether a number is prime or not.
# Requirements:
# - Accept an integer from the user.
# - Check whether the number is prime.
# - Return True if prime, otherwise False.
# - Handle zero, one, and negative numbers.

def is_prime(n):
    if n<=1:
        return False

    pri=0

    for i in range (1,n+1):
        if n%i==0:
            pri=pri+1

    if pri==2:
        return True
    else:
        return False

num=int(input("Enter the number: "))
print("Print your number: ", num)

prime_no=is_prime(num)
print("The number is Prime: ", prime_no)