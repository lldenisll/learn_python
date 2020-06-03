numero=int(input("Preencha o número que quer verificar:" ))
'pedimos a informação ao usuário, note que já estamos transformando o o input que por padrão vem como string em valor inteiro (int)'

ver = numero%3
'para saber se o número é múltiplo de 3, fazemos a divisão que nos retorna o valor que sobra da divisão, se o resultado for 0 o número é multiplo de 3'
ver2 = numero%5
'para saber se o número é múltiplo de 5, fazemos a divisão que nos retorna o valor que sobra da divisão, se o resultado for 0 o número é multiplo de 5'

if ver==0 and ver2==0:
    print("FizzBuzz")
else:
    print(numero)
    
'por fim, imprimimos (print) FizzBuzz caso o número seja multiplo de 3 e (and) multiplo de 5, valores calculados em ver e ver2, caso não seja verdadeiro ira imprimir o próprio número preenchido pelo usuário' 