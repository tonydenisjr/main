# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Iniciando variaveis e strings
name1 = name1.lower()
name2 = name2.lower()

valor_p1 = 0
valor_p2 = 0

#Verificando o TRUE
valor_p1 += name1.count("t")
valor_p1 += name1.count("r")
valor_p1 += name1.count("u")
valor_p1 += name1.count("e")

valor_p1 += name2.count("t")
valor_p1 += name2.count("r")
valor_p1 += name2.count("u")
valor_p1 += name2.count("e")

# Verificando o LOVE
valor_p2 += name1.count("l")
valor_p2 += name1.count("o")
valor_p2 += name1.count("v")
valor_p2 += name1.count("e")

valor_p2 += name2.count("l")
valor_p2 += name2.count("o")
valor_p2 += name2.count("v")
valor_p2 += name2.count("e")

valor_p1 = str(valor_p1)
valor_p2 = str(valor_p2)

percentual_final = valor_p1 + valor_p2
percentual_final = int(percentual_final)

if percentual_final < 10 or percentual_final > 90:
    print(f"Your score is {percentual_final}, you go together like coke and mentos.")
elif percentual_final > 40 and percentual_final < 50:
    print(f"Your score is {percentual_final}, you are alright together.")
else:
    print(f"Your score is {percentual_final}")