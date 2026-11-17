"""
Move all zeros to the end
- Create a list containing positive numbers, negative numbers, and zeros.
- Move all zeros to the end.
- Maintain the original order of all non-zero elements.
- Do not use sort() or sorted().
Example:
numbers = [0, 1, 0, 3, 12, 0, 5]
Expected output:[1, 3, 12, 5, 0, 0, 0]
"""
num_list = []
num_of_numbers = int(input("Enter the amount of numbers: "))

for i in range(num_of_numbers):
    num = int(input("Enter the number: "))
    num_list.append(num)

print("The numbers are:", num_list)

zeroes_no = 0
new_list = []

for i in num_list:
    if i == 0:
        zeroes_no += 1
    else:
        new_list.append(i)

print("The number of zeroes are:", zeroes_no)

for i in range(zeroes_no):
    new_list.append(0)

print("The list is:", new_list)