import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
numero_pessoas = len(names)

n_pessoa_escolhida = random.randint(0, numero_pessoas-1)

pessoa_escolhida = names[n_pessoa_escolhida]


print(f"{pessoa_escolhida} is going to buy the meal today!")