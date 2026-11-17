"""
- Create a list containing repeated elements.
- Count how many times each element appears.
- Display each unique element with its frequency.
- Do not use count() or dictionaries initially.
Example:
numbers = [10, 20, 10, 30, 20, 10]
Expected output:10 = 320 = 230 = 1
"""
numbers = [10, 20, 10, 30, 20, 10]

checked = []

for i in numbers:
    if i not in checked:
        frequency = 0

        for j in numbers:
            if i == j:
                frequency += 1

        print(i, "=", frequency)
        checked.append(i)