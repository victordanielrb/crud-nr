def atualizar(query):
    print('____________________________________')
    for key,value in query.items():
        if key != "_id":
            item = input(f"{key} ? \n ")
        elif key == "favoritos":
            key = 1
            favoritos = []
            while (key != 'N'):
                produto = input("Produto favorito: ")
                if produto:
                    print("Produto adicionado: ",produto)
                    favoritos.append(produto)
                else:
                    print("Produto não encontrado")
                
                
                key = input("Deseja cadastrar um novo produto favorito (S/N)? ")
        if item != "":
            query[key] = item
    return query
