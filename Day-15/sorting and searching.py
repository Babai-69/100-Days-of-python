"""
Sort a list without built-in functions
- Take 10 numbers from the user.
- Store them in a list.
- Sort the numbers in ascending order.
- Create another list for descending order.
- Do not use sort() or sorted().
- Use loops and conditions to perform sorting.
"""

num_list=[]
num_of_numbers=int(input("Enter the amount of number: "))


for i in range (1,num_of_numbers+1):
    num=(int(input("Enter the number: ")))
    num_list.append(num)

print("The numbers are: ",num_list)

#decending_list=[]

for i in range (len(num_list)):
    for j in range(i+1,len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print ("The ascending list is: ",num_list)

"""
while len(num_list) > 0:
    popped_num=num_list.pop()
    decending_list.append(popped_num)
"""

for i in range (len(num_list)):
    for j in range(i+1,len(num_list)):
        if num_list[i] < num_list[j]:
            num_list[j], num_list[i] = num_list[i], num_list[j]

print ("The decending list is: ",num_list)