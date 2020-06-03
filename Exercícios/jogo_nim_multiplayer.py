import random
def usuario2_escolhe_jogada(n,m):
    print()
    while True:
        print(usuario2, "Quantas peças você vai tirar?")
        num = int(input("Digite aqui: "))
        if num > m or (n - num) < 0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            if num < 2:
                print(usuario2," tirou uma peça.")
            else:
                print(usuario2," tirou", num, "peças.")
                print()
            return num

            
def partida():
    
    global usuario1
    global usuario2
    
    usuario1=input("Qual o nome do player1: ")
    usuario2=input("Qual o nome do player2: ")
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    print("Vamos jogar os dados para ver quem começa")
    print()
    
    dadousuario1=(random.randrange(1, 6))
    print()
    dadousuario2=(random.randrange(1, 6))
    
    print(usuario1," tirou", dadousuario1)
    print()
    print(usuario2," tirou",dadousuario2)
    if dadousuario1>dadousuario2:
        print(usuario1," começa")
        jogador=1
    else:
        print(usuario2," começa")
        jogador=0
        
    while n>0:
        if jogador==0:
            n = n - usuario2_escolhe_jogada(n,m)
            jogador=1
        else: 
            n = n - usuario_escolhe_jogada(n,m)
            jogador = 0
        if n==0 and jogador==0:
            print("Fim do jogo!",usuario1, "ganhou!")
            break
        if n==0 and jogador==1:
            print("Fim do jogo! O ",usuario2, "ganhou!")
            break
        if n<2:
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam",n,"peças no tabuleiro")
            
        
def usuario_escolhe_jogada(n,m):
    
    print()
    while True:
        print(usuario1, "Quantas peças você vai tirar?")
        num = int(input("Digite aqui: "))
        if num > m or (n - num) < 0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            if num < 2:
                print(usuario1," tirou uma peça.")
            else:
                print(usuario1," tirou", num, "peças.")
                print()
            return num

def campeonato():
    print("Você escolheu um campeonato!")
    rodada = 1
    while rodada <= 3:
        print("**** Rodada",rodada,"****")
        print()
        partida()
        print()
        rodada = rodada + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X",(rodada-1),"Computador")

    
#inicio do programa
print("Vamos começar")
print("1- para jogar uma partida isolada")
print("2- para jogar um campeonato")
escolha=int(input("Escolha: "))

while escolha !=1 and escolha !=2:
    print("por favor escolha entre 1 ou 2")
    escolha=int(input("Escolha: "))

else:
    if escolha == 1:
        print("Você escolheu uma partida isolada")
        partida()
        
    if escolha ==2:
        print("Você escolheu um campeonato")
        campeonato()



       
