largura=int(input("digite a largura: "))
altura=int(input("digite a altura: "))
a=altura

while altura > 0:
    x = 0
    while x < largura:
        if altura == (a) or x == (largura - 1) or altura == 1 or x == 0:
            print("#" , end = '')
        else: 
            print(" " , end = '')
        x+=1
    altura = altura - 1
    print()
    
    #quero imprimir na largura o valor da largura apenas na primeira e na ultima linha, e quero imprimor na altura, o valor da altura apenas na priemira e na ultima coluna