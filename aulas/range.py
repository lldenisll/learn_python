#range é um intervalo, limite de valores entre 2 dados
#pode ser usado junto com o comando for


#for i in range(fim):
    #COMANDO
    
#for i in range (inicio,fim):
    #COMANDO
    
#for i in range (inicio, fim, passo):
    #COMANDO

print("O exemplo abaixo utiliza apenas uma variavel, imprime apenas na ordem os 20 primerios numeros começando do zero")
for i in range (20):
    print (i)

    
print("O exemplo abaixo utiliza 2 variaveis no comando range e imprime  na ordem os 10 primerios numeros começando do 10")    

for x in range (10,20):
    print (x)
    
print("O exemplo abaixo utiliza 3 variaveis entre parenteses para o comando range, e imprime começando do número 3 até antes do 30 de 3 em 3")     
for y in range (3,30,3):
    print (y)

print("O exemplo abaixo imprime todos os pares entre 0 e 40")
pares = range (0,40,2)
for p in pares: 
    print (p)
print("O exemplo abaixo, aletara a lista teste para todos os numeros da lista teste ao quadrado")
teste=[1,2,3,4,5,6,7,8,9]
for e in range(len(teste)):
    teste[e]=teste[e]**2
print (teste)
