import os

secret_word1 = "Futebol"

right_letters = ''

attempt = 0
attempt_max = 20

while True:
    user_letter = input('Digit one word: ')

    attempt += 1
    print(f'attempts: {attempt}/{attempt_max}')

    if len(user_letter) > 1:
        print('Please, enter only one word.')
        continue

    if user_letter in secret_word1:
        right_letters += user_letter


    format_word = ''  
    for secret_letter in secret_word1:
        if secret_letter in right_letters:
            format_word += secret_letter
        else:
            format_word += '*'

    print(format_word)

    if attempt > attempt_max:
        print('Your attempts ended')

    
    if format_word == secret_word1:
        os.system('cls')
        print('You win!!!')
        print('Congratulations!!!')
        print('The secret word is:', secret_word1)
        print('Attempts: ', attempt)
        
        

    