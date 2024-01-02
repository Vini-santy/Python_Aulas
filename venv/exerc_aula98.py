multiplier_1 = 10
multiplier_2 = 11

result_1 = 0
result_2 = 0 


    # CPF verified 1
        # cpf = '746.824.890-70' \
        #     .replace('.', '') \
        #     .replace(' ', '') \
        #     .replace('-', '')


    # CPF verified 2
        # cpf = input('CPF [746.824.890-70]: ')
        # cpf_verified = re.sub(
        #     r'[^0-9]',
        #     '',
        #     entrada
        # )

while True:
# CPF verified 3
    cpf = input('Enter your CPF \nExample (XXX.XXX.XXX-XX):  ')

    cpf_verified = ''.join(filter(str.isdigit, cpf)) 

    # Cheking the dices
    if len(cpf_verified) >= 12 or len(cpf_verified) <= 10:
        print('Your CPF is incomplete or incorrect.')
        continue

    repetition = cpf_verified[0] * len(cpf_verified)

    if repetition == cpf_verified:
        print('Your CPF is incomplete or incorrect.')
        continue
        

    # CPF's First number 
    cpf_1 = cpf_verified[:9]
    
    for number in cpf_1:
        result_1 += int(number) * multiplier_1

        multiplier_1 -= 1 

    digit_1 = (result_1 * 10) % 11

    if digit_1 > 9:
        digit_1 = 0

    # CPF's Second number
    cpf_2 = cpf_verified[:10] 
    
    for number_2 in cpf_2:
        result_2 += int(number_2) * multiplier_2

        multiplier_2 -= 1 

    digit_2 = (result_2 * 10) % 11

    if digit_2 > 9:
        digit_2 = 0

    # Part final
    digit_final_1 = cpf_verified[9]
    digit_final_2 = cpf_verified[10]

    cpf_int = f'{cpf_verified[:3]}.{cpf_verified[3:6]}.{cpf_verified[6:9]}-{digit_1}{digit_2}'

    if digit_1 == int(digit_final_1) and digit_2 == int(digit_final_2):
        print(f'Your CPF ({cpf_int}) is valid!!')
        break
    else:
        print('CPF is invalid')

    



    

    


