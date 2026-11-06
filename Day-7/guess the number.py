# Generate a random number within a predefined range.
# Ask the user to guess the randomly generated number.
# Compare the user's guess with the actual number.
# Display a hint if the guess is too high or too low.
# Continue the game until the user guesses correctly.
# Count and display the total number of attempts.
# Display a congratulatory message when the user wins.

number=99
print("I have selected a number between 1 and 100.")
print("Can You Guess It?")

while True:
        num=int(input("Enter your number: "))

        if num==number:
            print("Congratulations! You guessed the correct number!")
            break
        elif num<number:
            print("Too low! Try again.")
        elif num>number:
            print("Too high! Try again.")
