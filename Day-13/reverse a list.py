"""
Reverse a list
- Create a list containing multiple elements.
- Create a new empty list named reversed_list.
- Access the original list starting from its last element.
- Add each element to the new list.
- Print the reversed list.
- Restriction: Don't use reverse() or slicing ([::-1]).
"""

num_list=[]
reversed_list=[]

num=int(input("Enter the number of members in the list: "))

for i in range(1,num+1):
    user_input=int(input("Enter your number: "))
    num_list.append(user_input)
print("The numbers are: ",num_list)

while len(num_list) > 0:
    popped_num=num_list.pop()
    reversed_list.append(popped_num)
    
print ("The reverse list is: ", reversed_list)