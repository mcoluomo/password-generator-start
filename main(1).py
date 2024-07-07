#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
try:
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
except ValueError:
    print("Please enter valid integers for the number of letters, symbols, and numbers.")
    exit()

if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:
    print("Please enter positive values for the number of letters, symbols, and numbers.")
    exit()

import secrets
random_letters = [secrets.choice(letters) for _ in range(nr_letters)]
random_symbols = [secrets.choice(symbols) for _ in range(nr_symbols)]
random_numbers = [secrets.choice(numbers) for _ in range(nr_numbers)]

random_password = random_letters + random_symbols + random_numbers

random.shuffle(random_password)

print(f"Your password is: {''.join(random_password)}")

