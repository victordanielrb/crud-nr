def atualizar(query):
    print('____________________________________')
    for key,value in query.items():
        if key != "_id":
            item = input(f"{key} ? \n ")
        if item != "":
            query[key] = item
    return query
