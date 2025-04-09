import atualizar
def delete_usuario(nome, sobrenome):
    #Delete
    global db
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome":sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o usuário ",mydoc)

def create_usuario():
    #Insert
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    favorito = db.produto.find_one({"nome":input("Produto Favorito: ")})
    if favorito:
        print("Produto Favorito: ",favorito)
    else:
        print("Produto não encontrado")
        favorito=""
    key = 1
    end = []
    while (key != 'N'):
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {        #isso nao eh json, isso é chave-valor, eh um obj
            "rua":rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) #estou inserindo na lista
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
    mydoc = { "nome": nome, "sobrenome": sobrenome, "cpf": cpf, "favorito":favorito, "end": end }
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)

def read_usuario(nome):
    #Read
    global db
    mycol = db.usuario
    print("Usuários existentes: ")
    if not len(nome):
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"],x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nome):
    #Read
    global db
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do usuário: ",mydoc)
    atualizar.atualizar(mydoc)

    newvalues = { "$set": mydoc }
    mycol.update_one(myquery, newvalues)

module = "user" = {
    create_usuario,
    read_usuario,
    update_usuario,
    delete_usuario
}
