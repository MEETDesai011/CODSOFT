import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

try:
    user_input = int(input("Enter desired password length: "))
    generated_password = generate_password(user_input)
    print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")
