# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
valor_maximo = student_scores[0]

for n in range(0, (len(student_scores)-1)):    
    valor_atual = student_scores[n+1]

    if valor_atual > valor_maximo:
        valor_maximo = valor_atual

print(f"The highest score in the class is: {valor_maximo}")
