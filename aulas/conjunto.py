conjunto={3,6,7,8} #uma das caracteristicas do conjunto é que ele não considera valores repetidos
print(conjunto)
conjunto.add(5) #pode adicionar elementos
print(conjunto)
conjunto.remove(3) #ou remover, note que ele remove os 2 números 3
conjunto.discard(3)
print(conjunto)

conjunto2={1,2,3,4,5}

conjunto3=conjunto.union(conjunto2) #posso unir 2 conjuntos e fomrmar um novo
print(conjunto3)
conjuntointer=conjunto2.intersection(conjunto) #retorna os valores que estao nos 2 conjuntos
print(conjuntointer)
conjuntodifer=conjunto2.difference(conjunto) #diferença entre um e outro
print(conjuntodifer)
conjuntodifersimetric=conjunto2.symmetric_difference(conjunto) #diferença simétrica contempla todos os elementos dos conjuntos
print(conjuntodifersimetric)

###

conjuntoa= {1,2,3}
conjuntob={1,2,3,4,5}
conjunto_subste=conjuntoa.issubset(conjuntob) #verificar se um conjunto é subconjunto de outro
print(conjunto_subste)
conjunto_superset=conjuntoa.issuperset(conjuntob) #verifica se é superconjunto
#se um for sub conjunto o outro será super conjunto sempre, nesse caso por ex o a é subconjunto de b e b é superconjunto de a
print(conjunto_superset)

lista=["cachorro","gato","gato","elefante"] #isso é uma lista normal
conjunto_animais=set(lista) #posso converter para conjunto, removendo as duplicidades
print(conjunto_animais)
lista_animais=list(conjunto_animais)#posso converter novamente para lista(removendo duplicidade com baixo custo computacional)


conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado

mariana = 2
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3
dedos = {mariana, renato, larissa, rafael, augusto, rafaela}
print(dedos)