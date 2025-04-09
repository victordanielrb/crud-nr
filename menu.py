from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import user
import json
import hashlib
uri = 'mongodb+srv://root:root@1.ks1qhzy.mongodb.net/'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.db
key = 0
sub = 0

while (key != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuario")
            user.create_usuario()
            
        elif (sub == '2'):
            nome = input("Read usuário, deseja algum nome especifico? ")
            user.read_usuario(nome)
        
        elif (sub == '3'):
            nome = input("Update usuário, deseja algum nome especifico? ")
            user.update_usuario(nome)

        elif (sub == '4'):
            print("delete usuario")
            nome = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            user.delete_usuario(nome, sobrenome)
            
    elif (key == '2'):
        print("Menu do Vendedor")        
    elif (key == '3'):
        print("Menu do Produto")        

print("Tchau Prof...")
