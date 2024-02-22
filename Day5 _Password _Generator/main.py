import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password ?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
# nr_letters = 4
for check_letter in range(1, nr_letters + 1):  # 1 - 4
    password += random.choice(letters)
for check_sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for check_number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

change_pass = ''.join(random.sample(password, nr_letters + nr_symbols + nr_numbers))  # Random character in string

print(f"Here is you password: {change_pass}")

#Solution2
# password_list = [] # Create list
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)    #Print for check total list after append
# random.shuffle(password_list)   #Random item in list with shuffle function
# print(password_list)    #Print for check total list after random
#
# password = ""      #For to change list to string
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}") #Print final password