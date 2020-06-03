def busca(lista,x):
    primeiro=0
    ultimo=len(lista)-1

    while primeiro <= ultimo:
        meio=(primeiro+ultimo)//2
        print(meio)
        if lista[meio]==x:
            return meio
        elif x < lista[meio]:
             ultimo=meio-1
        elif x>lista[meio]:
             primeiro=meio+1
        else:
            return False
    return False
