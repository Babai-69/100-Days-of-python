# Day 6 – Number Logic Challenges

## Overview

Welcome to Day 6 of my **100 Days of Python** journey!

Today, I focused on improving my logical thinking and problem-solving skills by working with numbers and their properties.

I practised using functions, loops, conditional statements, and mathematical operations to solve different programming problems.

## Topics Covered

- Python Functions
- Function Parameters and Return Values
- `while` Loops
- Conditional Statements (`if`, `elif`, `else`)
- Modulus Operator (`%`)
- Floor Division (`//`)
- Exponentiation (`**`)
- Digit Extraction
- Number Manipulation
- Boolean Values (`True` and `False`)

## Challenges Completed

### 1. Palindrome Number Checker

**File:** `palindrome_number.py`

**Objective:**

- Accept an integer from the user.
- Check whether the number reads the same forward and backward.
- Return `True` if it is a palindrome.
- Return `False` otherwise.
- Handle negative numbers.

**Example:**

For input `121`:

Reversed number = `121`

Since the original number and reversed number are equal, it is a palindrome.

**Test Cases:**

| Input | Expected Output |
|---|---|
| 121 | True |
| 12321 | True |
| 123 | False |
| 10 | False |
| -121 | False |
| 0 | True |

**Concepts:** Functions, loops, digit extraction, modulus (`%`), floor division (`//`), conditional statements.

---

### 2. Armstrong Number Checker

**File:** `armstrong_number.py`

**Objective:**

- Accept an integer from the user.
- Count the total number of digits.
- Raise each digit to the power of the total number of digits.
- Add all the calculated values.
- Return `True` if the sum equals the original number.
- Return `False` otherwise.
- Handle negative numbers.

**Example:**

For input `153`:

1³ + 5³ + 3³ = 153

Since the sum equals the original number, it is an Armstrong number.

**Test Cases:**

| Input | Expected Output |
|---|---|
| 0 | True |
| 153 | True |
| 370 | True |
| 371 | True |
| 407 | True |
| 9474 | True |
| 123 | False |
| -153 | False |

**Concepts:** Functions, loops, digit counting, exponentiation (`**`), modulus (`%`), floor division (`//`).

---

## Folder Structure

```text
Day-06/
│
├── palindrome_number.py
├── armstrong_number.py
└── guide.md
```

## Learning Outcomes

By completing these challenges, I practised:

1. Understanding how to manipulate individual digits of a number.
2. Reversing numbers using loops.
3. Checking numerical properties using mathematical operations.
4. Using functions to make code reusable.
5. Working with Boolean values (`True` and `False`).
6. Combining loops and conditional statements.
7. Improving logical thinking and problem-solving skills.

## Final Note

Day 6 helped me improve my understanding of number manipulation and mathematical logic in Python.

I am learning to approach problems step by step and write solutions independently instead of simply memorizing code.

**One day at a time, one problem at a time!**

Happy Coding! 🐍
