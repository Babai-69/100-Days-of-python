import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    return password


length = int(input("Enter the password length: "))

if length < 4:
    print("Password length must be at least 4!")
else:
    result = generate_password(length)
    print("Generated Password:", result)
