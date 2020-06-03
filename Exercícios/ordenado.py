
def ordenada (lista):
    if len(lista)==1:
        return True
    else:
        fim = len(lista)
        for i in range(fim - 1):
            posicao_do_minimo = i
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            novalista = lista[:]
            lista[i], lista[posicao_do_minimo] = novalista[posicao_do_minimo], novalista[i]

            if lista == novalista:
                return True
            else:
                return False




