def merge_sort(lista):
    if len(lista) <=1:
        return lista #base da recursão
    else: meio=len(lista)//2

    lado_esquerdo=merge_sort(lista[:meio]) #passa o parametro apenas com o lado esquerdo da lista, e devolve o lado esquerdo ordenado
    lado_direito=merge_sort(lista[meio:]) #idem para o lado direito
    return merge(lado_esquerdo, lado_direito) #intercala os lados direito e esquerdo

def merge(lado_esquerdo, lado_direito): #chamda recursiva
    if not lado_esquerdo: #base da recursão
        return lado_direito
    if not lado_direito:
        return lado_esquerdo
    if lado_esquerdo[0]<lado_direito[0]: #comparaçao pra ver qual numero vai para o primeiro elemento da lista
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:],lado_direito) #ver sorting algorithism animations
    return [lado_direito[0]]+ merge(lado_esquerdo, lado_direito[1:])
