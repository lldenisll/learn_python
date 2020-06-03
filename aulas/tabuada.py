#Repetições encaixadas, utilizadas quando precisamos trabalhar com planos não lineares, com mais de uma dimensão, por ex dados em uma tabela, que tem linhas e colunas, obedecendo a estrutura:
#while cond:
#       while cond1:
#           COMANDO
# De modo que o comando fará para cada repetição do while mais externo fará todas as repetições do while interno, depois volta ao externo e testa novamente(ou seja se o while externo executar 10 vezes e o interno 5 terá 50 repetições do comando)

#Definmos a linha começar no 1 e a coluna também, as posições iniciais da tabuada
linha = 1
coluna = 1
#O primeiro while vai rodar a linha até o 10 (valor maximo da nossa tabuada)
while linha <=10:
#o segundo while fará o mesmo com a coluna, ou seja iremos até 10 na linha e 10 na coluna, resultando em 100
    while coluna <=10:
#Ao fim desse while iremos imprimir linha * coluna para obter a tabuada desejada, note que inserimos ,end ao final para separar cada comando do while por um espaço como o tab do teclado, usando o comando /t
        print(linha*coluna, end="\t")
#depois de imprimir a primeira linha da tabuada, acrescentamos 1 na coluna para passarmos a proxima, até chegar no 10
        coluna=coluna+1
#agora que encerramos o while interno, vamos ao mais externo e acrescentamos mais 1 na linha, ele irá rodar todas as linhas e todas as colunas e fará a tabuada do outros números
    linha = linha + 1
#imprime um vazio
    print()
#volta para a coluna 1
    coluna=1