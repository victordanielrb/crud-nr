def atualizar(query):
    
    for key,value in query.items():
        item = input(f"{key} ? \n ")
        if item != "":
            query[key] = item
    return query

module = "atualizar" = {
    atualizar
}