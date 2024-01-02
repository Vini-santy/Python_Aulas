#       0 1 2 3 4 5 6 7 / 8 /  9 10 11 / 12 / 13 14 15 16 17 18
name = 'Vinicius dos Santos'
#    19 18 17 16 15 14 13 12 / 11 / 10 9  8 /  7 / 6 5 4 3 2 1

indice = 0
novo_nome = ''
while indice < len(name):
    letra = name[indice]
    novo_nome += f'*{letra}'
    indice += 1
    

novo_nome += '*'
print(novo_nome)