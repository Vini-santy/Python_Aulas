valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1 > valor2:
    print(
        f'O primeiro valor {valor1} é maior que o segundo valor {valor2} '
)
elif valor1 < valor2:
    print(
        f'O segundo valor {valor2} é maior que o primeiro valor {valor1}'
)
else:
    print(
        'Os dois valores são iguais'
)