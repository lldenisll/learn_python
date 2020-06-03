class ordenador:

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, 1):
            for j in range(i):
                if lista[j]>lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    return lista
        print(lista)
    def ordenada(self,lista):
        fim = len(lista)
        for i in range(fim - 1):
            posicao_do_minimo = i
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
