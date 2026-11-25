lista_catalogo = []

for i in range(2):
    print(f'\nLivro {i+1}')
    
    livro = {}

    livro['titulo'] = input('informe o nome do livro: ')
    livro['autor'] = input('informe o autor do livro: ')
    livro['ano'] = int(input('informe o ano de publicação: '))
    livro['genero'] = input('informe o genero do livro: ')
    livro['paginas'] = int(input('informe o numero de paginas do livro: '))
    
    lista_catalogo.append(livro)

# print(lista_catalogo)

for elemento in lista_catalogo: # roda 3 vezes
    # print(elemento)
    if elemento['ano'] >= 2020:
        print(f'Nome: {elemento['titulo']}')
        print(f'ano: {elemento['ano']}')

