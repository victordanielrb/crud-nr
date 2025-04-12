from pymongo import MongoClient
from pymongo.server_api import ServerApi
import atualizar

uri = 'mongodb+srv://root:root@1.ks1qhzy.mongodb.net/'
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.db

def create_vendedor():
    global db
    mycol = db.vendedor
    print("\nInserindo um novo vendedor")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    if mycol.find_one({"cpf": cpf}):
        print("Erro: CPF já cadastrado!")
        return
    mydoc = {"nome": nome, "cpf": cpf}
    x = mycol.insert_one(mydoc)
    print("Vendedor inserido com ID ", x.inserted_id)

def read_vendedor(vend_nome=""):
    global db
    mycol = db.vendedor
    print("\nVendedores existentes:")
    if not vend_nome:
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(f"Nome: {x['nome']}, CPF: {x['cpf']}")
    else:
        myquery = {"nome": vend_nome}
        mydoc = mycol.find_one(myquery)
        if mydoc:
            print(f"Nome: {mydoc['nome']}, CPF: {mydoc['cpf']}")
        else:
            print("Vendedor não encontrado")

def update_vendedor(nome):
    global db
    mycol = db.vendedor
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    if not mydoc:
        print("Vendedor não encontrado")
        return
    print("\nAtualizando vendedor: ", mydoc)
    updated_doc = atualizar.atualizar(mydoc)
    if updated_doc["cpf"] != mydoc["cpf"] and mycol.find_one({"cpf": updated_doc["cpf"]}):
        print("Erro: CPF já cadastrado!")
        return
    newvalues = {"$set": updated_doc}
    mycol.update_one(myquery, newvalues)
    print("Vendedor atualizado com sucesso")

def delete_vendedor(nome):
    global db
    mycol = db.vendedor
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    if not mydoc:
        print("Vendedor não encontrado")
        return
    mycol.delete_one(myquery)
    print("Vendedor deletado: ", mydoc)