class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message = message

while True:
    try:
        x=int(input("Entre uma nota de 0 a 10: "))
        print(x)
        if x > 10:
            raise InputError("Nota não pode ser maior que 10") #força uma exceção
        elif x<0:
            raise InputError("Nota não pode ser menor que zero")
        break
    except ValueError:
        print("Valor inválido, digite apenas números")
    except InputError as ex:
        print(ex)