# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
soma_alturas = 0
numero_alunos = 0

for altura in student_heights:
    soma_alturas += altura
    numero_alunos += 1

peso_medio = soma_alturas / numero_alunos
peso_medio = int(peso_medio)

print(peso_medio)