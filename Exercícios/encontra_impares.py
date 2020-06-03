def encontra_impares(lista):
    if len(lista) == 0:
        return []
    r = lista.pop(0)
    if r % 2 != 0:
        return [r] + encontra_impares(lista)
    return encontra_impares(lista)

