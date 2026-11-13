"""
Find duplicate elements
Use this example:
numbers = [10, 20, 30, 20, 40, 10, 50]
Your tasks:
- Create an empty list named duplicates.
- Use a loop to access every element.
- Check whether an element appears more than once.
- If it appears more than once, add it to duplicates.
- Make sure the same duplicate isn't added repeatedly.
- Print the duplicate elements.
Expected output:
[20, 10]
"""
numbers = [10, 20, 30, 20, 40, 10, 50, 40]

duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])

print("Duplicate numbers are:", duplicates)
