# Day 8 – ATM Simulation & Temperature Converter

## Overview

Welcome to Day 8 of my **100 Days of Python** journey!

Today, I focused on building two practical Python programs using functions, loops, conditional statements, and user input.

The objective was to understand how Python functions can be used to perform real-world tasks, handle user choices, and perform mathematical conversions.

## Topics Covered

- Python Functions
- Function Parameters and Return Values
- `while` Loops
- Conditional Statements (`if`, `elif`, `else`)
- User Input (`input()`)
- Mathematical Operations
- Temperature Conversion
- Basic ATM Operations
- Input Validation

## Challenges Completed

### 1. ATM Simulation

**File:** `atm_simulation.py`

**Objective:**

- Create a basic ATM simulation program.
- Allow users to check their account balance.
- Allow users to deposit money.
- Allow users to withdraw money.
- Check whether sufficient balance is available before withdrawal.
- Prevent invalid transactions.
- Provide an option to exit the ATM system.

**Example Menu:**

```text
===== WELCOME TO ATM =====

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice:
```

**Example Operations:**

| Operation | Initial Balance | Amount | Expected Balance |
|---|---:|---:|---:|
| Deposit | ₹1,000 | ₹500 | ₹1,500 |
| Withdraw | ₹1,000 | ₹300 | ₹700 |
| Withdraw | ₹1,000 | ₹1,500 | Insufficient Balance |
| Check Balance | ₹1,000 | - | ₹1,000 |

**Concepts:** Functions, loops, conditional statements, arithmetic operations, user input, and input validation.

---

### 2. Temperature Converter

**File:** `temperature_converter.py`

**Objective:**

- Create a temperature conversion program using functions.
- Convert Celsius to Fahrenheit.
- Convert Fahrenheit to Celsius.
- Allow users to select the conversion direction.
- Accept temperature values from the user.
- Display the converted temperature.

**Conversion Formulas:**

**Celsius to Fahrenheit:**

°F = (°C × 9/5) + 32

**Fahrenheit to Celsius:**

°C = (°F − 32) × 5/9

**Example Conversions:**

| Conversion | Input | Expected Output |
|---|---:|---:|
| Celsius to Fahrenheit | 0°C | 32°F |
| Celsius to Fahrenheit | 100°C | 212°F |
| Fahrenheit to Celsius | 32°F | 0°C |
| Fahrenheit to Celsius | 212°F | 100°C |

**Example Menu:**

```text
===== TEMPERATURE CONVERTER =====

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius

Enter your choice:
```

**Concepts:** Functions, parameters, return statements, conditional statements, mathematical formulas, and user input.

---

## Learning Outcomes

By completing these challenges, I practised:

1. Creating practical programs using Python functions.
2. Understanding how to manage user choices through menus.
3. Using loops to keep programs running until the user exits.
4. Performing deposit and withdrawal operations.
5. Applying conditions to validate financial transactions.
6. Understanding and implementing temperature conversion formulas.
7. Returning calculated values from functions.
8. Improving logical thinking through real-world programming examples.

## Final Note

Day 8 helped me connect Python programming concepts with practical, real-world applications.

I am gradually learning how to build interactive programs by combining functions, loops, conditions, and mathematical operations.

**Keep learning, keep practising, and keep coding!**

Happy Coding! 🐍
