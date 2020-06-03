# def sum_letters(string):
    #letters=0
    #for i in string:
     #   if i.isalpha():
      #      letters += 1
       # else:
        #    pass
    #return letters NAO PRECISEI USAR

def menor_nome(nomes):

    x=min(listafinal(nomes), key=len)
    y = ''.join((x))
    return(y.capitalize())

def ignora(list):
    newlist=([])
    for i in list:
        newlist.append(i.split())

    return newlist
def listafinal(list):
    listafinal=[]
    lista=ignora(list)
    i=0
    while i < len(lista):
        x= ''.join(lista[i])
        listafinal.append(x)
        i=i+1
    return listafinal

menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José
menor_nome(['LU   ', ' josé ', 'PAULO', 'Catarina'])
menor_nome(['zé', ' lu', 'fê'])