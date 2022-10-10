#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas!\n")
nr_letters= int(input("Quantas letras voce gostaria?\n")) 
nr_symbols = int(input(f"Quantos simbolos voce gostaria?\n"))
nr_numbers = int(input(f"Quantos numeros voce gostaria?\n"))


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



random.shuffle(lista_senha)

senha = ""

for char in lista_senha:
    senha += char

print(f"Sua senha eh {senha}")


