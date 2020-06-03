import random
class pokemon:
    def __init__(self,nome,golpe1,golpe2,golpe3,golpe4,vida):
        self.nome=nome
        self.golpe1=golpe1
        self.golpe2=golpe2
        self.golpe3=golpe3
        self.golpe4=golpe4
        self.vida=vida

lisstapokemons=[pokemon("Bubassauro","Leaf storm","Takle","Sleep Power","Razor leaf",100),
          pokemon("Charmander","Ember","Scrach","Flametower","Growl",100),
          pokemon("Squirtle","Bubble","Water Gun","Takle","Tail Whip",100)]
pokemonpc = random.choice(lisstapokemons)
def hits():
    x = random.randint(0, 40)
    if x == 0:
        print("E.. errou!!")
    if x < 10:
        print("Um golpe fraco")
    if x > 10 and x < 25:
        print("Acertou em cheio")
    if x > 25:
        print("UM DANO CRÍTICO!")

def batalha():

    print()
    print(pokemonusuario.nome)
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
    nova_vida=pokemonpc.vida
    print("A vida do pokemon do seu oponente é: ", nova_vida)
    jogada_pc()

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
jogada_pc()
