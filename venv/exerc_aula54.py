"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#num = input('Digite um número: ') # devolve um string


#if num.isdigit():
#    num_int = int(num)
#    par = num_int % 2 == 0 
#    if par:
#        print(f'O número {num_int} é par')
#    else:
#        print(f'O número {num_int} é impar') 
#else: 
#    print('Seu número não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input("Que horas são em número inteiro: ")

#hora_int = float(hora)

#try:
    #if 0 <= hora_int or hora_int <= 11:
    #    print("Bom dia!!!")
    #elif 12 <= hora_int or hora_int <= 17:
    #    print("Boa Tarde!!!")
    #elif 18 <= hora_int or hora_int <= 23:
    #    print("Boa noite!!!")
    #else: 
    #    print("Esse horário não existe!!!")
#except:
#    print('Por favor, coloque uma hora!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Qual é o seu primeiro nome? ')


try:
    tamanho = len(entrada)

    if tamanho <= 4:
        print("Seu nome é curto.")
    elif tamanho == 5 or tamanho == 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
except:
    print("Digite seu nome")