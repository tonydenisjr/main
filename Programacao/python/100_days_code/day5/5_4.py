#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#senha1 = ""
#for n in range(0, nr_letters):
#    numero1 = random.randint(0, nr_letters)
#    senha1 = senha1 + letters[numero1]
#
#senha2 = ""
#for n in range(0, nr_symbols):
#    numero2 = random.randint(0, nr_symbols)
#    senha2 = senha2 + symbols[numero2]
#
#senha3 = ""
#for n in range(0, nr_numbers):
#    numero3 = random.randint(0, nr_numbers)
#    senha3 = senha3 + numbers[numero3]
#
#senha = senha1 + senha2 + senha3
#
#print(senha)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

lista_senha = []


for n in range(0, nr_letters):
    numero = random.randint(0, nr_letters)
    lista_senha.append(letters[numero])

for n in range(0, nr_symbols):
    numero = random.randint(0, nr_symbols)    
    lista_senha.append(symbols[numero]) 

for n in range(0, nr_numbers):
    numero = random.randint(0, nr_numbers)    
    lista_senha.append(numbers[numero])

#print(lista_senha)

random.shuffle(lista_senha)

senha = ""

for char in lista_senha:
    senha += char

print(senha)