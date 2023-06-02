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

def test_update_user_email(email, updated_data):
    url = base_url + '/' + email
    response = requests.put(url, json=updated_data)
    if response.status_code == 201:
        print("Teste: atualizar usuário email - FALHA")       
    else:
        print("Teste: atualizar usuário email - SUCESSO")

def test_delete_user(email):
    url = base_url + '/' + email
    response = requests.delete(url)
    if response.status_code == 200:
        print("Teste: excluir usuário - SUCESSO")
    else:
        print("Teste: excluir usuário - FALHA")

def test_delete_user_wrong(email):
    url = base_url + '/' + email
    response = requests.delete(url)
    if response.status_code != 200:
        print("Teste: excluir usuário errado - SUCESSO")
    else:
        print("Teste: excluir usuário errado - FALHA")

def test_create_user_without_valid_email(user_data):
    response = requests.post(base_url, json=user_data)
    if response.status_code != 201:
        print("Teste: criar usuário com email valido - SUCESSO")
    else:
        print("Teste: criar usuário com email válido - FALHA")

def test_worng_update_user(email, updated_data):
    url = base_url + '/' + email
    response = requests.put(url, json=updated_data)
    if response.status_code == 404:
        print("Teste: atualizar usuário inesistente - SUCESSO")
        print(response.json())
    else:
        print("Teste: atualizar usuário inesistente- FALHA")

def test_create_user_already_created(user_data):
    response = requests.post(base_url, json=user_data)
    if response.status_code != 201:
        print("Teste: criar usuário já criado - SUCESSO")
    else:
        print("Teste: criar usuário já criado - FALHA")

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

# Teste 6 - Tentar editar email
print("=== Teste 6 ===")
updated_data = {
    'email': 'novousuario@example.com',
}
test_update_user_email('joao@example.com', updated_data)

# Teste 7 - Excluir usuário
print("=== Teste 7 ===")
test_delete_user('joao@example.com')

# Teste 8 - o sistema não deve permitir exclusão do usuário não cadastrado
print("=== Teste 8 ===")
test_delete_user_wrong('emailIncorreto@inc.com') 

# Teste 9 - o sistema não deve permitir a criação de um usuário com email inválido
print("=== Teste 9 ===")
user_data = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'email': 'joaotestecom',
    'senha': 'senha123',
    'nasc': '1990-01-01'
}
test_create_user_without_valid_email(user_data)

# Teste 10 - o sistema não deve permitir que atualize um usuário com email não cadastrado
print("=== Teste 10 ===")
updated_data = {
    'nome': 'Kleber',
    'sobrenome': 'Silva',
    'nasc': '1990-01-01'
}
test_worng_update_user("emailErrado@gmail.com", updated_data)

# Teste 11 - o sistema não deve permitir o cadastro de usuário que ja existe
print("=== Teste 11 ===")
user_data = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'email': 'joao@example.com',
    'senha': 'senha123',
    'nasc': '1990-01-01'
}

test_create_user_already_created(user_data);