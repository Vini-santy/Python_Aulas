# f-strings
"""
Formatação básica de strings
s - string
d - int
f - float
.<n° de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - Centro
= - força o numero a aparecer antes dos zeros
Sinal - + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.787284756234:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500: 08X}')
print(f'{variavel!r}')