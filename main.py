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

def test_create_user(user_data):
    response = requests.post(base_url, json=user_data)
    if response.status_code == 201:
        print("Teste: criar usuário - SUCESSO")
        print(response.json())
    else:
        print("Teste: criar usuário - FALHA")

# Teste 1 - Obter todos os usuários
print("=== Teste 1 ===")
test_get_all_users()

# Teste 2 - Criar usuário
print("=== Teste 2 ===")
user_data = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'email': 'joao@example.com',
    'senha': 'senha123',
    'nasc': '1990-01-01'
}
test_create_user(user_data)