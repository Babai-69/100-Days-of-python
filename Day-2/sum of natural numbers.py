# Ask the user for a number and calculate the sum of all natural numbers from 1 to that number.
#Using if-else loop

num=int(input("Enter a number: "))
print("The number you entered: ",num)

if num > 0:
    print("The sum of all number from 1 is: ")
    print(num*(num+1)//2)

else:
    print("Please Enter a positive number! ")

# Using For loop

num=int(input("Enter a number: "))
print("The number you entered: ",num)

total=0

for i in range (1,num+1):
    total=total+i

print("\nThe total after calculating the number is: ",total)