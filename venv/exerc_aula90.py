# import os 

# lista = []

# while True:
#     #print('Selecione uma opção')
#     #enunciado = input('[i]nserir [a]pagar [l]istar: ') 
#     user_data = input('Selecione uma opção \n[i]nserir [a]pagar [l]istar: ').lower()
    
#     if user_data == 'i':
#             os.system('cls')
#             valor_inserido = input('Valor: ')
#             lista.append(valor_inserido)
    
#     elif user_data == 'a':
#          try:
#               valor_apagado = int(input('Choose an index to delete: '))
#               del lista[valor_apagado]
#          except ValueError:
#               print('Please, type an integer')
#          except IndexError:
#               print("Index doesn't exist in the list")
#          except Exception:
#               print('unknown error')
        
#     elif user_data == 'l':
#          os.system('cls')
#          if lista == []:
#               print('Não há nada na lista.')
#          else:
#             for i, nome in enumerate(lista):
#               print(i, nome)
         
#     else:
#         print('Please, enter one of the letters shown.')

    
tuple(1, 2, 3)