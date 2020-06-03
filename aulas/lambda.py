contador_letras= lambda lista: [len(x) for x in lista] #lambda é eficiente para funções que podemos resolver com uma linha

lista=["cachorro","gato","elefante"]
print(contador_letras(lista))

soma=lambda a,b: a+b #lambda chama a função, depois vem os parametros, e a execução

print(soma(4,2))

calculadora={  #dicionário
    'soma': lambda a,b: a+b,
    'subtração': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
}

soma=calculadora['soma']
print(soma(10,4))

valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)
print(resultado)