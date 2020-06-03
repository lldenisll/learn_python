import random
class pokemon:
    def __init__(self,nome,golpe1,golpe2,golpe3,golpe4,vida,tipo):
        self.nome=nome
        self.golpe1=golpe1
        self.golpe2=golpe2
        self.golpe3=golpe3
        self.golpe4=golpe4
        self.vida=vida
        self.tipo=tipo

lisstapokemons=[pokemon("Bubassauro","Leaf storm","Takle","Sleep Power","Razor leaf",100,"grama"),
          pokemon("Charmander","Ember","Scrach","Flametower","Growl",100,"fogo"),
          pokemon("Squirtle","Bubble","Water Gun","Takle","Tail Whip",100,"agua")]
pokemonpc = random.choice(lisstapokemons)


def hits(lista):
    y=1
    if pokemonusuario.tipo=="fogo" and pokemonpc.tipo == "grama":
        y=2
    if pokemonusuario.tipo=="agua" and pokemonpc.tipo == "fogo":
        y=2
    if pokemonusuario.tipo == "grama" and pokemonpc.tipo == "fogo":
        y = 2
    if pokemonusuario.tipo == "fogo" and pokemonpc.tipo == "agua":
        y= 0.5
    if pokemonusuario.tipo == "grama" and pokemonpc.tipo == "agua":
        y=2
    x = random.randint(0, 40)*y

    lista.append(x)
    if x == 0:
        print("E.. errou!!")
    if x < 10:
        print("Um golpe fraco",x)
    if x > 10 and x < 25:
        print("Acertou em cheio",x)
    if x > 25:
        print("UM DANO CRÍTICO!",x)
    return lista
def hitspc(lista):

    x = random.randint(0, 40)
    lista.append(x)
    if x == 0:
        print("E.. errou!!")
    if x < 10:
        print("Um golpe fraco")
    if x > 10 and x < 25:
        print("Acertou em cheio")
    if x > 25:
        print("UM DANO CRÍTICO!")
    return lista


def batalha():
    nova_vida=pokemonpc.vida
    soma_hits=[]
    soma_hitspc=[]
    nova_vidausu=pokemonusuario.vida

    print()
    while nova_vida>0 or nova_vidausu>0:
        print()
        print("Turno do oponente com: ",pokemonpc.nome)
        golpes=[pokemonpc.golpe1,pokemonpc.golpe2,pokemonpc.golpe3,pokemonpc.golpe4]
        print("O",pokemonpc.nome,"usou",random.choice(golpes))
        print()
        nova_vidausu = pokemonusuario.vida - sum(hitspc(soma_hitspc))

        if nova_vidausu >0:
            print("A vida do seu pokemon é: ", nova_vidausu)
        else:
            print("O seu pokemon morreu")
            break
        print()
        print("Seu turno com: ",pokemonusuario.nome)
        print("1- ",pokemonusuario.golpe1,"/ 2- ",pokemonusuario.golpe2,"/ 3- ",pokemonusuario.golpe3,"/ 4- ",pokemonusuario.golpe4)
        golpe_escolhido=int(input("Digite o número do golpe escolhido: "))
        if golpe_escolhido == 1:
            print(pokemonusuario.nome,"Use",pokemonusuario.golpe1)
        if golpe_escolhido == 2:
            print(pokemonusuario.nome,"Use",pokemonusuario.golpe2)
        if golpe_escolhido == 3:
            print(pokemonusuario.nome,"Use",pokemonusuario.golpe3)
        if golpe_escolhido == 4:
            print(pokemonusuario.nome,"Use",pokemonusuario.golpe4)
        print()

        nova_vida=pokemonpc.vida - sum(hits(soma_hits))
        if nova_vida>0:
            print("A vida do pokemon do seu oponente é: ", nova_vida)
        else:
            print("O pokemon do seu oponente morreu, e você venceu")
            break
    else:
        print("O pokemon do seu oponente morreu")


print("O computador escolheu", pokemonpc.nome)
print()
pokemonusuario = int(input("Escolha um Pokemon, entre 1 para Bubassauro, 2 para Charmander ou 3 para Squirtle "))

if pokemonusuario == 1:
    print("Você escolheu o Bubassauro")
    pokemonusuario=lisstapokemons[0]
if pokemonusuario == 2:
    print("Você escolheu o Charmander")
    pokemonusuario=lisstapokemons[1]
if pokemonusuario == 3:
    print("Você escolheu o Squirtle")
    pokemonusuario=lisstapokemons[2]
print()
print("Vamos a batalha!")
batalha()
