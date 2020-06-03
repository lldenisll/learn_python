from bhaskara import Bhaskara
import pytest #imported so we can use the pytest.fixture (line 5)

class TestBhaskara:
    @pytest.fixture
    def b(self):
        return Bhaskara() #created in order to use in the asserts of each case

    def testa_uma_raiz(self,b):
        assert b.imprime_raizes(1,0,0) == (1,0)

    def testa_duas_raiz(self,b):
        assert b.imprime_raizes(1,-5,6) == (2,3,2)

    def testa_zero_raiz(self,b):
        assert b.imprime_raizes(10,10,10) == 0

    def testa_raiz_negativa(self,b):
        assert b.imprime_raizes(10,20,10) == (1,-1) #tested by pytest, result 4 passed in 0.02 seconds...

#fixtures é um valor fixo para um conjunto de testes, usado para guardar objetos que dão trabalho para ser criados
#criamos a fixture com @pytest.fixture