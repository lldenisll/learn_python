n = int(input("Digite um número inteiro: "))
#é preciso definir um valor para a variavel soma, ela vai aparecer lá em baixo, mas se rodarmos sem valor, irá aprecer um erro, então definimos o valor neutro da soma (0)
soma = 0

#Faremos esse comando enquanto o n for maior que zero, vai quando acabarem os algarismos a divisão n//10 vai dar zero e vai acabar o programa
while (n > 0):
#resto faz a sobra da divisão do numero inteiro por 10, esse valor é o ultimo algarismo, o resto
    resto = n % 10
#n vai cuidar de remover o ultimo algarismo porque faz a divisão exata do número por 10, tirando a sobra
    n = n // 10
#soma é a variavel final, o que vamos imprimir, ele usa a variavel soma que no começo vale zero e soma ao resto, todas as vezes que o while executar o programa irá retornar um valor de resto
    soma = soma + resto


print(soma)