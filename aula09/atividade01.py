lista_contato = []


for i in range(3):
    print(f'Lista {i+1}')

    lista = {}

    lista['nome'] = input('Informe o nome completo: ')
    lista['telefone'] = int(input('Informe o telefone: '))
    lista['email'] = input('Informe o email: ')

    lista_contato.append(lista)


for elemento in lista_contato:
    print(f'\nNome: {elemento['nome']} ')
    print(f'telefone: {elemento['telefone']} ')
    print(f'email: {elemento['email']} ')

    # print(elemento)
    # print(lista_contato)