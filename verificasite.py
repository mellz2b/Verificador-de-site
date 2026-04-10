import requests # type: ignore

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=3)
        print(f"{url} está ONLINE - Status: {resposta.status_code}")
    except:
        print(f"{url} está OFFLINE")

url = input("Digite a URL: ")
verificar_site(url)