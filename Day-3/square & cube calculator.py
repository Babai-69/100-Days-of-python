# calculating square and cube values of a number
def sqr(num):
    return num * num
def cube(num):
    return num ** 3

while True:
    num=int(input("Enter the number:"))

    if num==0:
        print("You have entered 0, please enter a valid number")  
    else:
        sqr_num=sqr(num)
        cube_num=cube(num)
        print("The square of your number is: ",sqr_num)
        print("The cube of your number is: ", cube_num)
        break