def calcula_dimensoes(matriz):
    height = len(matriz)
    width = 1
    for item in matriz:
        width = len(item)
        break
    return "{}".format(height) + "X" + "{}".format(width)

def dimensoes(matriz):
    print(calcula_dimensoes(matriz))


