import json
import requests

# Solicitanto qua endereço IP voc:
endereco_ip = input("Informe o endereco IP que deseja buscar: ")

# Sua chave de API, disponível na página da sua conta da Abstract:
CHAVE_API = 'sua-chave-api'

resposta = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + CHAVE_API + '&ip_address=' + endereco_ip)
result = json.loads(resposta.content)
print(result)
