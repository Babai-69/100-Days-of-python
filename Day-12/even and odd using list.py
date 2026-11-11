"""
Count even and odd numbers
- Create a list containing 10 numbers.
- Create two counter variables:
  - even_count = 0
  - odd_count = 0
- Use a for loop to access every number.
- Print both counters.
"""

num = [54, 38, 18, 51, 60, 3, 91, 8, 92, 50]

even_count=0
odd_count=0

for i in num:
    
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print ("The odd numbers are: ",odd_count)
print ("The even numbers are: ",even_count)