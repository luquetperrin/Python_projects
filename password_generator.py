"""
Create a Password Generator
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

password_list = []

for i in range(n_letters):
    generated_letters = random.choice(letters)
    password_list += generated_letters

for i in range (n_symbols):
    generated_symbols =random.choice(symbols)
    password_list += generated_symbols

for i in range (n_numbers):
    generated_numbers = random.choice(numbers)
    password_list += generated_numbers

random.shuffle(password_list)

password =""
for char in password_list:
    password += char
print(password)