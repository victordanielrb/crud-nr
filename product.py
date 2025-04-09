import atualizar
def delete_produto(nome):
    #Delete
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o produto \n",mydoc)

def create_produto():
    #Insert
    global db
    mycol = db.produto
    print("\nInserindo um novo produto")
    nome = input("Nome: ")
    preco = input("Preço: ")
    descricao = input("Descrição: ")
    vendedor = db.vendedor.find_one({"nome":input("Vendedor: ")})
    if vendedor:
        print("Vendedor: ",vendedor)
    else:
        print("Vendedor não encontrado")
        vendedor=""
  
    key = 1
    
    mydoc = { "nome": nome, "preco":preco, "descricao": descricao, "vendedor":vendedor,  }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_produto(prod_nome):
    #Read
    global db
    mycol = db.produto
    print("Produtos existentes: ")
    if not len(prod_nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["preco"])
    else:
        myquery = {"nome": prod_nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto(nome):
    #Read
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("atualizar produto: ",mydoc)
    atualizar.atualizar(mydoc)
    print("atualizar produto: ",mydoc)
    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

module = "product" = {
    create_produto,
    read_produto,
    update_produto,
    delete_produto
}
