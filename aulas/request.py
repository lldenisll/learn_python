import requests
def retorna_cep(cep):

    response=requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    #print(response.status_code)
    #print(response.json())
    dados_cep=response.json()
    print(dados_cep)
    print("Entregar pedido para rua "+dados_cep['logradouro'])
    return dados_cep
def retorna_dados_pokemon(pokemon):
    response=requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon))
    dados_pokemon=response.json()
    for e in dados_pokemon['moves']:
        print(e)
    print(dados_pokemon['moves'])
    return dados_pokemon



if __name__ == '__main__':
    cep=input("Digite um CEP: ")
    retorna_cep(cep)
    pokemon=input("Digite um pokemon: ")
    retorna_dados_pokemon(pokemon)