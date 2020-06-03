numero=input("Digite um número inteiro: ")
tiraunidade=int(numero)%10
semunidade=int(numero)-tiraunidade
resultadoum=semunidade/10
dezena=int(resultadoum%10)

print ("O dígito das dezenas é" ,dezena,)