import random
import string

def generate_password(length):
    """Generate a random password of a given length."""

    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = upper_alphabet.lower()
    symb = "!#$%^&*()\|:.,?/@"
    number = "1234567890"
    characters = upper_alphabet+lower_alphabet+symb+number


    password = ''.join(random.choice(characters) for i in range(length))

    return password

if __name__ == '__main__':
    print(generate_password(10))
