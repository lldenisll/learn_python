#usuário digita varios numeros e pra cada numero o programa diz se é primo ou não 

n=int(input("Digite um número inteiro: "))
def éprimo(x):
    fator=2
    while x % fator != 0 and fator<=(x/2):
        fator=fator+1
    if x%fator==0:
        return False
    else:
        return True

while n>0:
    if éprimo(n):
        print(n, "é primo")
    else:
        print(n ,"não é primo")
    n=int(input("Digite um número inteiro: "))
    