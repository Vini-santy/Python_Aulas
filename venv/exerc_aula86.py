lista = ['Maria', 'Helena', 'Luiz']

i = 0

for nome in lista:  
    print('[',i,']',nome)

    i += 1

for nome in enumerate(lista):
    ...