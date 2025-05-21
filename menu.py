from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import product
import user
import vendedor
import compra

uri = 'mongodb+srv://root:root@1.ks1qhzy.mongodb.net/'
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.db
key = 0
sub = 0

while (key != 'S'):
    print("1-CRUD Usuário")
    print("2-CRUD Vendedor")
    print("3-CRUD Produto")
    print("4-CRUD Compra")
    key = input("Digite a opção desejada? (S para sair) ")

    if (key == '1'):
        print("Menu do Usuário")
        print("1-Create Usuário")
        print("2-Read Usuário")
        print("3-Update Usuário")
        print("4-Delete Usuário")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create usuário")
            user.create_usuario()
        elif (sub == '2'):
            nome = input("Read usuário, deseja algum nome específico? ")
            user.read_usuario(nome)
        elif (sub == '3'):
            nome = input("Update usuário, deseja algum nome específico? ")
            user.update_usuario(nome)
        elif (sub == '4'):
            print("Delete usuário")
            nome = input("Nome a ser deletado: ")
            sobrenome = input("Sobrenome a ser deletado: ")
            user.delete_usuario(nome, sobrenome)
            
    elif (key == '2'):
        print("Menu do Vendedor")
        print("1-Create Vendedor")
        print("2-Read Vendedor")
        print("3-Update Vendedor")
        print("4-Delete Vendedor")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create vendedor")
            vendedor.create_vendedor()
        elif (sub == '2'):
            nome = input("Read vendedor, deseja algum nome específico? ")
            vendedor.read_vendedor(nome)
        elif (sub == '3'):
            nome = input("Update vendedor, deseja algum nome específico? ")
            vendedor.update_vendedor(nome)
        elif (sub == '4'):
            print("Delete vendedor")
            nome = input("Nome a ser deletado: ")
            vendedor.delete_vendedor(nome)
            
    elif (key == '3'):
        print("Menu do Produto")
        print("1-Create Produto")
        print("2-Read Produto")
        print("3-Update Produto")
        print("4-Delete Produto")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create produto")
            product.create_produto()
        elif (sub == '2'):
            nome = input("Read produto, deseja algum nome específico? ")
            product.read_produto(nome)
        elif (sub == '3'):
            nome = input("Update produto, deseja algum nome específico? ")
            product.update_produto(nome)
        elif (sub == '4'):
            print("Delete produto")
            nome = input("Nome a ser deletado: ")
            product.delete_produto(nome)
            
    elif (key == '4'):
        print("Menu da Compra")
        print("1-Create Compra")
        print("2-Read Compra")
        print("3-Update Compra")
        print("4-Delete Compra")
        sub = input("Digite a opção desejada? (V para voltar) ")
        if (sub == '1'):
            print("Create compra")
            compra.create_compra()
        elif (sub == '2'):
            nome = input("Read compra, deseja algum usuário específico? ")
            compra.read_compra(nome)
        elif (sub == '3'):
            nome = input("Update compra, deseja algum usuário específico? ")
            compra.update_compra(nome)
        elif (sub == '4'):
            print("Delete compra")
            nome = input("Nome do usuário a ser deletado: ")
            compra.delete_compra(nome)

print("Tchau Prof...")