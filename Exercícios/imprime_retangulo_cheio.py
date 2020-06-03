largura=int(input("digite a largura: "))
altura=int(input("digite a altura: "))
#enquanto a altura for maior que zero
while altura > 0:
#definimos um valor inical para X, enquanto o X não chegar na largura, iremos imprimir um #, após imprimr, somamos 1 ao x e verificmaos novamente, tiramos um da altura também, pois iremos rodar no while externo a condição da altura chegar zero, quando altura chegar em zero a largura também deve ter chegado ao x
    x = 0
    while x < largura:
        print("#" , end = '') 
        x+=1
    altura = altura - 1
    print()