"""
Sum of all elements
- Create a list containing multiple numbers.
- Create a variable named total and initialize it with 0.
- Use a for loop to access each element.
- Add each element to total.
- Print the final sum.
- Restriction: Don't use the built-in sum() function.

"""

num = [54, 38, 18, 51, 60, 3, 91, 8, 92, 50, 65, 87, 96, 39, 78,
       94, 45, 17, 23, 35, 76, 32, 15, 77, 44, 88, 47, 11, 59,
       74, 100, 14, 22, 85, 49, 37, 5, 1, 53, 9, 75, 93, 20,
       29, 52, 28, 86, 30, 61, 46]

total=0

for i in num:
    total=total+i

print(total)
