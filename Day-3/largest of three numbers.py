# Find the largest number from the three numbers taken from user

def find_max(x,y,z):
    if x>y:
        if y>z:
            return x
        else:
            return z
    else:
        if y>z:
            return y
        else:
            return z

num1=(int(input("Enter the first number: ")))
num2=(int(input("Enter the second number: ")))
num3=(int(input("Enter the thrird number: ")))

num=find_max(num1, num2, num3)
print("The maximum number is: ", num)