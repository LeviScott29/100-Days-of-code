import random 
print("welcome to the Python Password Generator")
nr_letters = int(input("how many letters do you want? \n"))
nr_numbers =int(input("how many numbers do you want? \n"))
nr_symbols = int(input ("how symbols do you want? \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#chooses random letters, numbers, and symbols to add to password list
password_list=[]
for i in range(0, nr_letters):
    random_letters=random.choice(letters)
    password_list +=random_letters
    
for i in range(0, nr_numbers):
    random_numbers=random.choice(numbers)
    password_list +=random_numbers

for i in range(0, nr_symbols):
    random_symbols=random.choice(symbols)
    password_list +=random_symbols

random.shuffle(password_list)
#takes elements of password list and concatenates them into a string of characters
password=""
for i in password_list:
    password+=i

print(password)
