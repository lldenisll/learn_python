#arquivo=open('teste.txt', 'w') #criar um arquivo novo
def escrever_arquivo(texto):

    arquivo=open('teste.txt', 'w') #cria o arquivo
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')  # edita o arquivo existente
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo=open(nome_arquivo, 'r') #formato r de read
    texto=arquivo.read()
    print(texto)
def cad_usuario(nome_arquivo):
    arquivo=open(nome_arquivo, 'r')
    usuario=arquivo.read()
    usuario=usuario.split('\n')
    for x in usuario:
        lista_usuarios=x.split(",")
        print(lista_usuarios) #imprime a lsita completa de usuarios
        us=lista_usuarios[0]
        print(us) #imprime apenas o usuário
def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(teste.txt,"/Users/namorado")

if __name__ == '__main__':
    #escrever_arquivo("Primeira linha")

    usuario=input("Nome do usuário: ")
    tipo=input("Escreva o tipo de usuário: ")
    cadastro=("\n"+usuario + "," + tipo)
    atualizar_arquivo("teste.txt",cadastro)
    cad_usuario('teste.txt')
    #item=input("Digite o próximo item: ")
    #lista_mercado=item+"\n"
    #atualizar_arquivo("teste.txt", lista_mercado)
    #ler_arquivo('teste.txt')

