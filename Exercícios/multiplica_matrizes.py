def multiplica_matrizes(m1, m2):
        n_linhas_m1, n_col_m1 = len(m1),len(m1[0]) #DEFINE O NÚMERO DE LINHAS E COLUNAS DE M1
        n_linhas_m2, n_col_m2 = len(m2), len(m2[0]) #DEFINE O NÚMERO DE LINHAS E COLUNAS DE M2
        assert n_col_m1 == n_linhas_m2 #ASSERT ERRO SE NUMERO DE COLUNAS DA MATRIZ 1 FOR DIFERENTE DO NUMERO DE LINHAS DA MATRIZ2
        r=[]
        for lin in range(n_linhas_m1): #percorre as linhas da matriz 1
            r.append([])
            for col in range(n_col_m2): #percorre as colunas da matriz 2
                r[lin].append(0)
                for k in range(n_col_m1):
                    r[lin][col] += m1[lin][k] * m2[k][col]
        return r
if __name__ == '__main__': #rodar o script
    A=[[1, 2, 3], [4, 5, 6]]
    B=[[1,2],[3,4],[5,6]]
    print(multiplica_matrizes(A,B))