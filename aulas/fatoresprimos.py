#Dado um número inteiro n, n>1, imprimir sua decomposição em fatores primos, indicando também a multiplicidade de cada fator
import sys



n=int(input("Digite um número inteiro: "))

fator=2
multiplicidade = 0 
#primeiro while vai percorrer os fatores até fator ser igual a 1, pq o n / 1 é igual a n
while n>1:
#while interno irá verificar se o fator divide o número N
    while n%fator==0:
#se dividir por fator, então iremos avançar 1 na multiplicidade e dividir n por favor, após isso na linha 17 fora do while iremos testar o fator + 1, e zeramos a multiplicidade
        multiplicidade = multiplicidade + 1
        n=n/fator
    if multiplicidade>0:
        print("fator ",fator,"multiplicidade ",multiplicidade)
        
    fator=fator+1
    multiplicidade=0

