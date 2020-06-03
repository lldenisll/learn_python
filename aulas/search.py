import pytest

class comida:
    def __init__(self,nome,sabor):
        self.nome=nome
        self.sabor=sabor
minhas_comidas_favoritas= [comida("pizza", "brócolis"),
                                comida("lasanha", "queijo"),
                                comida("Bolo", "Chocolate")]

def busca_sequencial(seq,x):
    for i in range(len(seq)):
        if seq[i].nome == x:
            print("Realmente, é uma das minhas comidas favoritas, e o sabor que mais gosto é ",seq[i].sabor)

    return False

x=input("Digite o valor buscado: ")
busca_sequencial(minhas_comidas_favoritas,x)