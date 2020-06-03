import random
from bubblesort import ordenador
import time

class contatempos:
    def lista_aleatorio(self, n):
        lista=[0 for x in range(n)]
        for i in range(n):
            lista[i]=random.randrange(1000)
        return lista

    def estaordenada(self, lista):
        for i in range(len(lista)):
            if lista[i] > lista[i + 1]:
                return False
        else:
            return True
    def compara(self, n):
        lista1=self.lista_aleatorio(n)
        lista2=lista1[:]
        o=ordenador()
        antes=time.time()
        novalista1=[]
        novalista1=o.bolha(lista1)
        depois=time.time()
        print("Bolha demorou",depois-antes)
        antes=time.time()
        novalista2=o.ordenada(lista2)
        depois=time.time()
        print("Ordenada demorou", depois-antes)
        if self.estaordenada(novalista1) == True:
            print("ok")


