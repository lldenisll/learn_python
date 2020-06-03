lista=[1,10]
arquivo=open("teste.txt", 'r')
try:
    texto=arquivo.read()
    divisao=10/1
    numero = lista[1]
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero")
except ArithmeticError: #esse é pai do zerodivision, por isso vem a baixo
    print("Houve um erro aritimético")
except IndexError:
    print("Erro ao acessar indece inválido da lista")
except Exception as ex: #pai de todas as execeções por isso é o último
    print("Erro desconhecido. ERRO: {} " .format(ex))
else:
    print("Executa quando nao ocorre exceção")
finally:
    print("Sempre executa")
    arquivo.close() #bom fechar o arquivo ou qualquer coisa que precisa ser executada indendepnde do erro no finally

