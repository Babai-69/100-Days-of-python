"""
Calculate the average
- Create an empty list.
- Take 5 numbers from the user.
- Store all 5 numbers in the list.
- Calculate the total of all elements using a loop.
- Divide the total by the number of elements.
- Store the result in an average variable.
- Print the average.
- Restriction: Don't use sum().
"""
total=0
num_list=[]
num=int(input("Enter the number of members in the list: "))

for i in range(1,num+1):
    user_input=int(input("Enter your number: "))
    num_list.append(user_input)
print("The numbers are: ",num_list)

for i in num_list:
    #total=sum(num_list)
    total=total+i
    average=total/len(num_list)

print ("The total is: ", total)
print ("The average is: ",average)
