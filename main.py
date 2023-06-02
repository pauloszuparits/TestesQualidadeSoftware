import requests
import json
import pprint

base_url = 'http://localhost:3000/cadastrados'

def test_get_all_users():
    response = requests.get(base_url)
    if response.status_code == 200:
        print("Teste: obter todos os usuários - SUCESSO")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(response.json())    
    else:
        print("Teste: obter todos os usuários - FALHA")

# Teste 1 - Obter todos os usuários
print("=== Teste 1 ===")
test_get_all_users()