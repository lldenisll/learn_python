import requests
def retorna_response(url):
    response=requests.get(url)
    return response.text

if __name__ == '__main__':
    site=input("Cole a URL do site que procura: ")
    response=retorna_response(site)
    print(response)