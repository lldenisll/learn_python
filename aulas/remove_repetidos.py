

def remove_repetidos(lista):
    nova_lista = []
    for i in lista :
        if i not in nova_lista :
            nova_lista.append(i)
    return sorted(nova_lista)

