nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')

    print(f'Seu nome tem {len(nome)}')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última de letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, mas você deixou campos vazios.')