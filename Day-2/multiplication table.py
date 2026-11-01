# Ask the user for a number and print its multiplication table up to 10.

num=int(input("Enter the number: "))
print("You have entered: ", num)


print("The multiplication table is: ")

for i in range (1,11):
        print(i*num, end=" \n")