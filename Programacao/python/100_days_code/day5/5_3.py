#Write your code below this row 👇
soma_pares = 0

for n in range(1, 101):
    numero = n % 2
    if numero == 0:
        soma_pares +=n

print(soma_pares)


#for number in ranger(2, 101, 2)