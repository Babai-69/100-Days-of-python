"""
Create two different lists.
- Find all elements that exist in both lists.
- Do not include duplicate common elements in the result.
- Do not use set().
Example:
list1 = [10, 20, 30, 40, 50]list2 = [30, 40, 60, 70]
Expected output:[30, 40]
"""
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

common = []

for i in list1:
    if i in list2:
        if i not in common:
            common.append(i)

print("Common elements:", common)