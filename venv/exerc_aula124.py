# Exercício - sistema de perguntas e respostas lista_op1 
import os

while True:
    Hits = 0

    questions  = [
        { # d1
            'Pergunta': 'Quanto é 2+2?', 
            'Opções': ['6', '3', '4', '7'], 
            'Resposta': '4' 
        }, 
        { # d2
            'Pergunta': 'Quanto é 5x5?',
            'Opções': ['25', '55', '35', '5'],
            'Resposta': '25',
        },
        { # d3
            'Pergunta': 'Quanto é 30/2',
            'Opções': ['25', '15', '13', '60'],
            'Resposta': '15',
        },
    ]

    # ------Acessing the first question------
    d1 = questions[0]

    # -----Acessing d1['Pergunta']------
    print(f"Pergunta: {d1['Pergunta']}")
    print()# space

    #-----------Alternatives--------------
    print('Opções: ')

    answers = d1['Opções']
    for indice, number in enumerate(answers):
        print(f'{indice}) {number}')

    print()# space
    
    # ------------Choices----------------
    choice = input('Escolha uma resposta: ')

    if (choice == '0' or choice == answers[0]) and answers[0] == d1['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1
    
    elif (choice == '1' or choice == answers[1]) and answers[1] == d1['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1

    elif (choice == '2' or choice == answers[2]) and answers[2] == d1['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1

    elif (choice == '3' or choice == answers[3]) and answers[3] == d1['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1
    else:
        print('Missed ❌')


    print(f'Got {Hits}/3 questions correct')
    print()

    # ------Acessing the second question------
    d2 = questions[1]

    # -----Acessing d2['Pergunta']------
    print(f"Pergunta: {d2['Pergunta']}")
    
    print()# space

    print('Opções: ')
    answers = d2['Opções']
    for indice, number in enumerate(answers):
        print(f'{indice}) {number}')

    print()# space
    
    # ------------Choices----------------
    choice = input('Escolha uma resposta: ')

    if (choice == '0' or choice == answers[0]) and answers[0] == d2['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1
    
    elif (choice == '1' or choice == answers[1]) and answers[1] == d2['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1

    elif (choice == '2' or choice == answers[2]) and answers[2] == d2['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1

    elif (choice == '3' or choice == answers[3]) and answers[3] == d2['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1
    else:
        print('Missed ❌')


    print(f'Got {Hits}/3 questions correct')

    print()

    # ------Acessing the third question------
    d3 = questions[2]

    # -----Acessing d3['Pergunta']------
    print(f"Pergunta: {d3['Pergunta']}")
    
    print()# space

    print('Opções: ')
    answers = d3['Opções']
    for indice, number in enumerate(answers):
        print(f'{indice}) {number}')

    print()# space
    
    # ------------Choices----------------
    choice = input('Escolha uma resposta: ')

    if (choice == '0' or choice == answers[0]) and answers[0] == d3['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1
    
    elif (choice == '1' or choice == answers[1]) and answers[1] == d3['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1

    elif (choice == '2' or choice == answers[2]) and answers[2] == d3['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1

    elif (choice == '3' or choice == answers[3]) and answers[3] == d3['Resposta']:
        print('Acertou!!! ✅')
        Hits += 1
    else:
        print('Missed ❌')

    # ---------finalization---------------
    if Hits == 3:
        os.system('cls')
        print('🥳🎉 (≧∀≦)ゞ💯Congratilations💯(≧∀≦)ゞ 🥳🎉')
        print(f'Got {Hits}/3 questions correct')
    else:
        os.system('cls')
        print('😭💥 (￣_￣|||)💀You Lost💀(￣_￣|||) 😭💥')
        print(f'Got {Hits}/3 questions correct')
    
    try_again = input('Want to play again?[yes/no] ')

    if try_again == 'yes' or try_again == 'sim':
        os.system('cls')
        continue
    else:
        os.system('cls')
        print('😀 Thanks for playing my game!! 🫡')
        break


    
