a="batata"

print(a[0]) # esse comando irá imprimir a posição de caracter 1 do srtring na variável a, ou seja a letra b

print(a.upper()) #esse comando irá imprimir a string da variável a em letra maíuscula

print(a.lower()) #esse comando irá imprimir a string da variável a em letra minúscula

b="BATATA"
print(a.capitalize()) #esse comando irá imprimir a string da variável a com a primeira letra maíuscula
print(b.capitalize()) #idem, note que a variável b tem todas as letras em maíscula, e o código corrige

c="  denis.ga.each@gmail.com    "
print(c.strip()) #a função strip remove os espaços de uma string, útil para dev web em campos de login

d="o rato roeu a roupa do rei de roma"
print(d.count("r")) #a função count retorna a quantidade de uma determinada sub string de uma variável com string

print(d.replace("rato","batata")) #a função replace troca uma palavra dentro de uma variável com string

print(d.capitalize().center(80)) #a função center centraliza o texto, é preciso definir a largura no ()
print(d.find("rato")) #a função retorna a posição de uma determinada sub-string

print(d[:13]) #imprime até a posição 13
print(d[13:]) #imprime da posição 13 em diante
print(d[2:8]) # imprme da posição 2 até a 8

lista_de_nomes=["                  Ana","Rodrigo","Clayton"]
x=(min(lista_de_nomes))
print(x.split())
