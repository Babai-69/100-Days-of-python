#Asks the user how many numbers they want to enter.
#Accepts those numbers using a for loop.
#Calculates their average.
#Returns the average.

def avg_num(x):
        new_num=x/amount_num
        return(new_num)

# def avg_num(x,y):
#   avg=x/y
#   return(avg)

amount_num=int(input("Enter the amount of number you want to calculate: "))
sum=0

if amount_num>0:

    for i in range (1,amount_num+1):
        num=(int(input("Enter the number: ")))
        print("You have entered: ",num)
        sum=sum+num
    average_num=avg_num(sum)

    #avgerage_num=avg_num(sum,amount_name)

    print("The average num of all number is: ",average_num)

else:
    print("You have entered 0, plaease enter a number!")
