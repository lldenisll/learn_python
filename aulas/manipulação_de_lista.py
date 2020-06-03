#Manipulação de listas 
#Fatias de lista
#nome_da_lista[x:y] esse comando extrai trecho da lista iniciado em x e terminado em y


lista1=[1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

print("O primeiro comando imprime os itens da posição 1 até a posição 5 da lista 01")
print(lista1[1:5])

print()

print("esse comando [:x] imprime os x primeiros números começando da posição zero, no ex abaixo x=10")
print(lista1[:10])

print("Esse comando [x:] imprime os x últimos itens da lista, no ex abaixo 10")
print(lista1[10:])

#podemos armazenar em uma nova lista também, uma fatia de lista, por ex abaixo, salvamos em uma nova lista os 10 últimos itens da lista1

listanova=lista1[10:]

#clonando listas, no caso abaixo, lista3 e lista2 recebem a lista de cores, qualquer alteraçao feita na lista irá alterar as duas variáveis, pois se referem a mesma lista, não é o ideal, como podemos clonar a lista então?

lista2=["vermelho","verde","Azul"]
lista3=lista2
#a função clone, abaixo, pode ser substituita simplesmente por [:]
def clone (lista2):
    clone=[]
    for objeto in lista2:
        clone.append(objeto)
    return clone
#lista4=clone(lista2) esse código funciona mas pode ser substituito pelo cód abaixo
lista4=lista2[:]
lista4[1]="Violeta"
print("Veja o código para entender, estamos clonando a lista 2,e alterando a posição 01 para violeta")
print(lista4)

print()

#pertinencia a uma lista, serve para checar se um item pertence a uma lista

print("podemos verificar se um item esta na lista perguntando item in lista, no caso abaixo rodamos 'violeta' in lista4, retornou true") 
print("Violeta" in lista4)

#concatenação de lista
print("A contatenação de lista nos permite somar listas, no caso abaixo fizemos a lista4+lista2")
print(lista4+lista2)
#podemos também criar uma nova lista que seja a soma de varias listas
      
lista5=lista4+lista2+lista1+lista3
      
#podemos também multiplicar uma lista
print("No caso abaixo triplicamos a lista 4, utilizando o comando lista4*3")
lista4_triplicada=lista4*3
print(lista4_triplicada)

#Remoção de elementos em listas
print("Deletamos o item no índice 1 da lista 4 com o comando del")
del lista4[1]
print(lista4)
print("Podemos também deletar um trecho da lista, abaixo deletamos do indice 1 ao 3 da lista 4 lista4[1:3]")
del lista4[1:3]
print (lista4)