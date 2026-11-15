"""
Rotate a list
- Take a list of numbers from the user.
- Ask the user how many positions they want to rotate.
- Rotate the list to the right by that number of positions.
- Example:
            numbers = [1, 2, 3, 4, 5]
            rotation = 2# 
            Expected output:[4, 5, 1, 2, 3]
"""

num_list=[]
num_of_numbers=int(input("Enter the amount of number: "))

for i in range (1,num_of_numbers+1):
    num=(int(input("Enter the number: ")))
    num_list.append(num)

print("The numbers are: ",num_list)

# Ask for rotation positions
rotate_num = int(input("Enter the number of positions to rotate: "))

# Handle an empty list
if len(num_list) == 0:
    print("The list is empty!")

else:
    # Handle rotation greater than list length
    rotate_num = rotate_num % len(num_list)

    # Rotate the list to the right
    if rotate_num != 0:
        a = num_list[-rotate_num:]
        b = num_list[:-rotate_num]
        total_list = a + b
    else:
        total_list = num_list

    print("The rotated list is:", total_list)
