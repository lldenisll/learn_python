contador_letras= lambda lista: [len(x) for x in lista] #lambda é eficiente para funções que podemos resolver com uma linha

lista=["cachorro","gato","elefante"]
print(contador_letras(lista))

soma=lambda a,b: a+b #lambda chama a função, depois vem os parametros, e a execução

print(soma(4,2))