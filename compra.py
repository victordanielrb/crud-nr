from pymongo import MongoClient
from pymongo.server_api import ServerApi
import atualizar

uri = 'mongodb+srv://root:root@1.ks1qhzy.mongodb.net/'
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.db

def create_compra():
    global db
    mycol = db.compra
    print("\nInserindo uma nova compra")
    usuario = input("Nome do usuário: ")
    usuario_doc = db.usuario.find_one({"nome": usuario})
    if not usuario_doc:
        print("Usuário não encontrado")
        return
    produto = input("Nome do produto: ")
    produto_doc = db.produto.find_one({"nome": produto})
    if not produto_doc:
        print("Produto não encontrado")
        return
    vendedor = input("Nome do vendedor: ")
    vendedor_doc = db.vendedor.find_one({"nome": vendedor})
    if not vendedor_doc:
        print("Vendedor não encontrado")
        return
    data = input("Data da compra (DD/MM/AAAA): ")
    endereco = input("Endereço de entrega: ")
    mydoc = {
        "usuario": usuario,
        "produto": produto,
        "vendedor": vendedor,
        "data": data,
        "end de entrega": endereco
    }
    x = mycol.insert_one(mydoc)
    print("Compra inserida com ID ", x.inserted_id)

def read_compra(nome=""):
    global db
    mycol = db.compra
    print("\nCompras existentes:")
    if not nome:
        mydoc = mycol.find().sort("usuario")
        for x in mydoc:
            print(f"Usuário: {x['usuario']}, Produto: {x['produto']}, Vendedor: {x['vendedor']}, Data: {x['data']}, Endereço: {x['end de entrega']}")
    else:
        myquery = {"usuario": nome}
        mydoc = mycol.find(myquery)
        found = False
        for x in mydoc:
            print(f"Usuário: {x['usuario']}, Produto: {x['produto']}, Vendedor: {x['vendedor']}, Data: {x['data']}, Endereço: {x['end de entrega']}")
            found = True
        if not found:
            print("Nenhuma compra encontrada para o usuário")

def update_compra(nome):
    global db
    mycol = db.compra
    myquery = {"usuario": nome}
    mydoc = mycol.find_one(myquery)
    if not mydoc:
        print("Compra não encontrada")
        return
    print("\nAtualizando compra: ", mydoc)
    updated_doc = atualizar.atualizar(mydoc)
    if not db.usuario.find_one({"nome": updated_doc["usuario"]}):
        print("Usuário não encontrado")
        return
    if not db.produto.find_one({"nome": updated_doc["produto"]}):
        print("Produto não encontrado")
        return
    if not db.vendedor.find_one({"nome": updated_doc["vendedor"]}):
        print("Vendedor não encontrado")
        return
    newvalues = {"$set": updated_doc}
    mycol.update_one(myquery, newvalues)
    print("Compra atualizada com sucesso")

def delete_compra(nome):
    global db
    mycol = db.compra
    myquery = {"usuario": nome}
    mydoc = mycol.find_one(myquery)
    if not mydoc:
        print("Compra não encontrada")
        return
    mycol.delete_one(myquery)
    print("Compra deletada: ", mydoc)