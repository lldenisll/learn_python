def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i #fazer retornar a posição sem usar a função index

    return False