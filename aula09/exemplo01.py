produto1 = {} #dicionario vazio

produto = {

    'nome': 'notebook',
    'preco': 3500.80,
    'marca': 'lenovo',


}

# type(produto)
print(produto) #todas as chaves e valores
print(produto['nome']) # chaves e nome
print(produto['preco']) # chaves e preço

# alterando o valor 
produto['marca'] = "positivo"
print(produto['marca'])

# adicionando chaves
produto['tela'] = "18"
# print(produto)

#deletando uma chave 

del produto['marca'] 
print(produto)

print(produto.keys()) #chaves
print(produto.values()) #valores
print(produto.items()) #valores
