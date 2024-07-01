import random
#define 3 list Contain number and letters and symbols
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
number = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','+']
# 3 input function to ask user how many letters ,numbers and symbols it consists of the password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
#variable password as a string to Concatenate each character from letters ,numbers and symbols
password = ""
#list to save each character To make the order of the password scatter
pass_list =[]
#3 for loops to select random numbers,letters and symbols
for i in range(0,nr_letters):
  pass_list.append(random.choice(letters))
for i in range(0,nr_symbols):
  pass_list.append(random.choice(symbols))
for i in range(0,nr_numbers):
  pass_list.append(random.choice(number))
#function shuffle To make the order of the password scatter
random.shuffle(pass_list)
#Concatenate characters in string and print it
for i in pass_list:
  password += i
print(password)