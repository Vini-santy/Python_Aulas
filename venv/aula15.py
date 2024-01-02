# nome = input('Qual é o seu nome?')
# 1 - print(f'O seu nome é {nome=}')

# formato = 'O seu nome é nome={}'
# print(formato.format(nome))

# OBS: input só devolve <str>

# numero1 = int(input('Digite um número: '))
# numero2 = int(input('Digite outro numero: '))
# OBS: não colocar o (int) nas mesma linha do codigo pq se o usuario digitar uma letra 
# quebra o codigo.

numero1 = input('Digite um número: ')
numero2 = input('Digite outro numero: ')

int_numero1 = int(numero1)
int_numero2 = int(numero2)
# outra forma de fazer, fazendo a transoformação em uma outra variavel

print(f'A soma dos números é: {numero1 + numero2}')