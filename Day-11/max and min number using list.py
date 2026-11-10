"""
Find maximum and minimum
- Create a list containing multiple numbers.
- Create two variables:
  - largest – initially store the first element.
  - smallest – initially store the first element.
- Use a for loop to check every element.
- If an element is greater than largest, update largest.
- If an element is smaller than smallest, update smallest.
- Print both results.
- Restriction: Don't use max() or min().
"""

num = [54, 38, 18, 51, 60, 3, 91, 8, 92, 50, 65, 87, 96, 39, 78,
       94, 45, 17, 23, 35, 76, 32, 15, 77, 44, 88, 47, 11, 59,
       74, 100, 14, 22, 85, 49, 37, 5, 1, 53, 9, 75, 93, 20,
       29, 52, 28, 86, 30, 61, 46]

largest_num=num[0]
smallest_num=num[0]

for i in num:
    if i > largest_num:
        largest_num = i
    elif i < smallest_num:
        smallest_num = i

print("Largest number is: ",largest_num)
print("Smallest number is: ",smallest_num)