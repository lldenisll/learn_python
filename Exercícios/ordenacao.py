n1=int(input("Preencha o numero um: "))
n2=int(input("Preencha o numero dois: "))
n3=int(input("Preencha o numero tres: "))

if (n1<n2) and (n1<n3) and (n2<n3):
        print("crescente")
else:
        print("não está em ordem crescente")