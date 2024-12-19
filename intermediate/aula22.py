# Dictionary Comprehension e Set Comprehension 
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto.items())

dc = {
    chave: valor 
    for chave, valor 
    in produto.items()
}

print(dc)