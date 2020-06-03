import random

print("Olá! Bem vindo ao jogo da adivinhação")
print("O jogo é simples: O computador irá pensar em um número, e você deverá acertar!")
print()
print("Vamos lá?")

MIN=random.randint(51,99)
MAX=random.randint(99,150)
númeropc=random.randint(MIN, MAX)

print("Adivinhe o número que o computador escolheu entre,",MIN, "e",MAX)
usuario=0
chances=1
while númeropc!=usuario and chances<=3:
    usuario = int(input("Digite aqui um palpite: "))
    if usuario==númeropc:
        break
    if usuario not in range (MIN, MAX):
        print("O valor não está no limite escolhido pelo computador")
        chances-=1
    chances=chances+1

    if chances==2:
        if númeropc%2 == 0:
            print("O número é divisível por 2")
        else:
            print("O número não é divisível por 2")
    if chances==3:
        print("Essa é a sua última chance")
        print("O número está entre",númeropc-3, "e",númeropc+3)

if númeropc==usuario:
    print("Parabéns, você acertou o número era: ",númeropc)
else:
    print("Não foi dessa vez, o número correto era",númeropc)