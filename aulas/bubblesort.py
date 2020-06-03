def bubble_sort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
                print(lista)
    return lista