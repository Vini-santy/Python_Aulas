"""
Interpolação básica de sitrings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.9707665
variavel = '%s, o preço é R$%.2f' % (nome, preco)
# %s e %f são chamados de placeroders
# colocar o tipo certo de variavel
# f-strings, .format, interpolação
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))