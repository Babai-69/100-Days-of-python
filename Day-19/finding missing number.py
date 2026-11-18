"""
Find the missing number
- Create a list containing numbers from 1 to N.
- One number is missing from the sequence.
- Find the missing number.
Example:
numbers = [1, 2, 3, 5, 6, 7, 8]
Expected output:4
"""

numbers = [1, 2, 3, 5, 6, 7, 8]

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)
