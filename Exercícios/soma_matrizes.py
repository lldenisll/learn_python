
def calcula_dimensoes(matriz):
    height = len(matriz)
    width = 1
    for item in matriz:
        width = len(item)
        break
    return height, width
def criamatriz (linhas, colunas,valor):
    matriz = []
    for i in range (linhas):
        linha = []
        for j in range (colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz

def soma_matrizes(m1, m2):
    h, w = calcula_dimensoes(m1)
    if calcula_dimensoes(m1) != calcula_dimensoes(m2):
        return False
    else:
        n_linhas=len(m1)
        n_col=len(m1[0])
        r=criamatriz(n_linhas,n_col,0)

        for lin in range(n_linhas): #percorre as linhas da matriz
            for col in range(n_col): #percorre as colunas da matriz
                r[lin][col]=m1[lin][col]+m2[lin][col]
        return r
if __name__ == '__main__': #rodar o script
    A=[[1, 2, 3], [2, 3, 4]]
    B=[[10, 20, 30], [20, 30, 40]]
    print(soma_matrizes(A,B))