# import random
# 
# random_int = random.randint(1, 100)
# 
# print(random_int)


#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
valor = random.randint(0,1)

if valor == 1:
    print("Heads")
elif valor == 0:
    print("Tails")