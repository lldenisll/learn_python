#Objeto = dados + código
    #encapsulamento (cada capsula é um objeto)
    #cod de um objeto nao deve interferir em outro objeto
#Classes
    #classes definem os tipos de objetos
    #classes definem quais os dados e o código dos objetos
#Dados são atributos do objeto
#Código são métodos do objeto
#Os objetos são instancias das classes

#ex
#classe:carro
#instancia: meu_carro, carro_do_surftopia
#atributos: ano, modelo, cor e velocidade
#métodos: acelera (velocidade), pare()
import random

class Carro: #criamos a classe carro
    pass

meu_carro = Carro() #criamos o objeto meu carro na classe carro
carro_do_surftopia = Carro() #criamos o objeto carro do surftopia na classe carro
meu_carro.ano= 2013 #criamos atributos para o objeto dentro da classe ano modelo e cor para os 2 carros
meu_carro.modelo = "Gonew"
meu_carro.cor="Branco"
carro_do_surftopia.ano= 2006
carro_do_surftopia.modelo="Kombi"
carro_do_surftopia.cor="Branco"

print(meu_carro.modelo) #podemos imprimir algo específico
print(meu_carro.ano)
meu_carro.modelo="Bicicleta" #podemos alterar algum atributo
print(meu_carro.modelo)

#método especial __init__
#construtor da classe
#chamado automaticamento pelo interpretador quando os obj sao criados

class Caranga:
        def __init__(self,modelo,ano,cor):  # sempre primeira variavel é self, depois os atributos que queremos
            self.modelo = modelo
            self.ano = ano
            self.cor = cor

carro = Caranga("Fox","1999","Preto")

print(carro.modelo)
nomes=["Dênis","Laís","Rogério","Lucia","Daniel","Romualdo"]
class personagem:
    def __init__(self,nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
dia=random.randint(1,28)
mes=random.randint(1,12)
ano=random.randint(1910,2010)
pessoa1=personagem(random.choice(nomes),(dia,"/",mes,"/",ano))
print(pessoa1.nascimento)