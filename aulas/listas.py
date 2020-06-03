#listas de objetos
#Coleção de objetos, em outras linguagens de programação isso é chamado de array
#Em python utilizamos [] para listas
#as listas começam na contagem zero, ou seja hospedagem é o zero e turismo o 4, se utilizar números negativos ele começa do final da lista, por exemplo -1 seria turismo 
# podemos usar o comando len junto com uma lista para saber a qtde de itens da lista
#podemos adicionar itens a lista depois de feita com a função append basta colocar categorias.append("Produtos")
#é possível também trocar uma informação, por ex se quero trocar hospedagem, categorias[0]="Outra coisa"


#categorias=["Hospedagem","Cozinha","Bar","Turismo"]

print()
print("Bem vindo ao realizador de listas de receitas 2000")
print()
print("Para começar, basta adicionar os ingredientes abaixo, quando terminar digite Fim")

igredient=[]

ing=(input("Digite um ingrediente: "))
igredient.append(ing)

        
while ing != str("Fim"):
    
    
    ing=input("Digite um ingrediente: ")
    igredient.append(ing)
#nome da lista.pop() faz com que remova o ultimo item da lista, fiz isso para remover o item Fim, e imprimir somente os ingredientes da receita
igredient.pop()
print(igredient)
