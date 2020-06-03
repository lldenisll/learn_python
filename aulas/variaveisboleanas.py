'Utilização de expressões e variáveis booleanas utilizando indicadores de passagem para testar condições e imprimir resultados de acordo com cada condição, se satifesteita ou não. Vamos utilizar os comandos if/else e while. De modo que iremos executar um comando até que a condição if deixe de ser satifeita.'

decrescente = True
'determiamos a variável descrescente como verdadeira'

anterior=int(input("Digite o primeiro número da sequência: "))
'a variável anterior é definida para verificar se o valor inserido na váriavel valor que está dentro da chave while é menor que o defindo na variavel anterior, esse comando é feito para testar se o primeiro número é menor que o próximo número'

valor = 1
'definmos o valor = 1 pois precisamos definir a variável antes de coloca-la na chave do while o valor é igual a um pois tem que ser diferente de zero, de acordo com a primeira regra que criamos na chave while'

while valor!=0 and decrescente:
    valor=int(input("Digite o próximo número da sequência: "))
    if valor>anterior:
        decrescente=False
    anterior=valor
'aqui definimos o que iremos executar o comando que pede o próximo número da sequencia enquanto esse número for diferente de zero e menor que o anterior, isso esta discriminado após o comando while. O que faz com que esse comando funcione, além do comando (valor!=0) o comando if que dita que quando o valor for menor que o anterior o decrescente passa a ser falso. Quando o decrescente passa a ser falso o while para de executar o comando pois a variavel nao é mais decrescente. Note que para funcionar temos que atribiur a variaavel anterior o valor imputado pelo usuário na variável valor.'

if decrescente:
    print("A sequência está em ordem decrescente! ")
else:
    print("A sequëncia não está em ordem decrescente! ")
    
'por fim simplesmente imprimimos utilizando o comando print o resultado se (if) for decrescente e se não (else) for decrescente' 