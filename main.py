import requests
import json
import pprint

base_url = 'http://localhost:3000/cadastrados'

def check_return(response):
    return "nome" not in str(response) or "sobrenome" not in str(response) or "nasc" not in str(response)

def test_get_all_users():
    response = requests.get(base_url)
    if response.status_code == 200:
        print("Teste: obter todos os usuários - SUCESSO")   
    else:
        print("Teste: obter todos os usuários - FALHA")

def test_create_user(user_data):
    response = requests.post(base_url, json=user_data)
    if response.status_code == 201:
        print("Teste: criar usuário - SUCESSO")
    else:
        print("Teste: criar usuário - FALHA")

def test_login(user_data):
    url = base_url + '/login'
    response = requests.post(url, json=user_data)
    
    if response.status_code == 200:
        if check_return(str(response.json())):
             print("Teste: login - FALHA - NÃO RETORNA USUARIO")
        else:
           print("Teste: login - SUCESSO")
    else:
        print("Teste: login - FALHA")

def test_get_user_by_email(email):
    url = base_url + '/' + email
    response = requests.get(url)
    if response.status_code == 200:
        if check_return(str(response.json())):
             print(response.json())
             print("Teste: login - FALHA - NÃO RETORNA USUARIO")
        else:
           print("Teste: login - SUCESSO")
    else:
        print("Teste: obter usuário por nome - FALHA")


def test_update_user(email, updated_data):
    url = base_url + '/' + email
    response = requests.put(url, json=updated_data)
    if response.status_code == 201:
        print("Teste: atualizar usuário - SUCESSO")
    else:
        print("Teste: atualizar usuário - FALHA")

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

# Teste 3 - Login
print("=== Teste 3 ===")
login_data = {
    'email': 'joao@example.com',
    'senha': 'senha123'
}
test_login(login_data)

# Teste 4 - Obter usuário por email
print("=== Teste 4 ===")
test_get_user_by_email('joao@example.com')

# Teste 5 - Atualizar usuário
print("=== Teste 5 ===")
updated_data = {
    'nome': 'Kleber',
    'sobrenome': 'Silva',
    'nasc': '1990-01-01'
}
test_update_user('joao@example.com', updated_data)