
def computador_escolhe_jogada(n,m):
    print()
    qtd = 0
    if n <= m:
        qtd =  n
    else:
        if (n % (m+1)) == 0:
            qtd = m
        else:
            pc = 0
            while pc % (m + 1) != n % (m + 1):
                pc = pc + 1
                if pc % (m + 1) == n % (m + 1):
                    qtd = pc
                    break
    if qtd < 2:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",qtd,"peças.")
    return qtd
            
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if(n % (m+1)) == 0:
        print("Você começa")
        jogador=1
    else:
        print("Computador começa")
        jogador=0
        
    while n>0:
        if jogador==0:
            n = n - computador_escolhe_jogada(n,m)
            jogador=1
        else: 
            n = n - usuario_escolhe_jogada(n,m)
            jogador = 0
        if n==0 and jogador==0:
            print("Fim do jogo! Você ganhou!")
            break
        if n==0 and jogador==1:
            print("Fim do jogo! O computador ganhou!")
            break
        if n<2:
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam",n,"peças no tabuleiro")
        
def usuario_escolhe_jogada(n,m):
    print()
    while True:
        num = int(input("Quantas peças você vai tirar? "))
        if num > m or (n - num) < 0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            if num < 2:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou", num, "peças.")
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



       
