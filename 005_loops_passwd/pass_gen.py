#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


# Easy level

# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)
#     print(password)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# for char in range(0, nr_numbers):
#     password += random.choice(symbols)


# Hard

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_numbers):
    password_list.append(random.choice(symbols))

# random.shuffle(password_list) # embaralha a lista original
pass_shuffle = random.sample(password_list, len(password_list))

password = ""
for char in pass_shuffle:
    password += char

print("".join(pass_shuffle))
print(password)