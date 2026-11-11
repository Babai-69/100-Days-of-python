"""
Separate positive and negative numbers
- Take 10 numbers as input from the user.
- Store all numbers in one list.
- Create two empty lists:
  - positive_numbers
  - negative_numbers
- Use a for loop to check every number.
- If a number is greater than 0, add it to the positive list.
- If a number is less than 0, add it to the negative list.
- Print both lists.
- Extra: What will happen if the user enters 0? Handle it separately if you want.
"""
num=[]
for i in range(1,11):
    user_input=int(input("Enter number: "))
    num.append(user_input)
print("The numbers are: ",num)

positive_num=0
negative_num=0
zero=0

positive=[]
negative=[]
zeros=[]

for i in num:

    if i>0:
        positive_num+=1
        positive.append(i)

    elif i<0:
        negative_num+=1
        negative.append(i)

    else:
        zero+=1
        zeros.append(i)

print ("The positive numbers are: ", positive)
print ("The negative numbers are: ", negative)
print ("The zeros are: ", zeros)