'primeiro temos que lembrar o que é o fatorial, representado pelo sina de exclamação, vamos a um exemplo prático 4! = 4*3*2*1 = 24, logo 4! é igual a 24'
def fatorial(n):
    produto = 1
    i = 1
    while i <= n:
        produto = produto * i
        i = i + 1
    return produto

import pytest

@pytest.mark.parametrize("entrada,valor_esperado",[
    (0,1),
    (1,1),
    (4,24),
    (5,120)
    ])

def test_fatorial(entrada,valor_esperado):
    assert fatorial(entrada) == valor_esperado


