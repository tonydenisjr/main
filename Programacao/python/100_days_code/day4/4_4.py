import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

condicao_valida = True
forma_mao = [rock, paper, scissors]
selecao_computador = random.randint(0,2)

selecao_humano = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))

if selecao_humano > 2 or selecao_humano < 0:
    print("Invalid Number!")
    condicao_valida = False
    
if condicao_valida:
    print(forma_mao[selecao_humano])

    print("Computer chose:")
    print(forma_mao[selecao_computador])


    if selecao_humano == 0: #pedra
        if selecao_computador == 2: #tesoura
            print("You Win!")
        if selecao_computador == 1: #papel
            print("You Lose!")
    elif selecao_humano == 1: #papel
        if selecao_computador == 0: #pedra
            print("You Win!")
        if selecao_computador == 2: #tesoura
            print("You Lose!")
    elif selecao_humano == 2: #tesoura
        if selecao_computador == 1: #papel
            print("You Win!")
        if selecao_computador == 0: #pedra
            print("You Lose!")
    elif selecao_humano == selecao_computador:
        print("Tie")


"""
Se humano escolher pedra:

    se computador escolher tesoura: humano venceu
    se o computador escolher papeu: humano perdeu

se humano escolher papel:

    se o computador escolher pedra: humano venceu
    se o computador escolheu tesoura: humano perdeu

se o humano escolher tesoura:

    se o computador escolher papel: humano venceu
    se o computador escolher pedra: humano perdeu

senao 

    empate
"""
