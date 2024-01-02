#calculadora com while

while True:
    num1 = input('Enter one number: ')
    num2 = input('Enter another number: ')
    operator = input('Enter the operator(+-/*): ')

    # Validação dos dados
    num_valid = None
    
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num1)
        num_2_float = float(num2)
        num_valid = True
    except:
        num_valid = None
        
    if num_valid is None:
        print('One of the number is invalid.')
        continue

    authorised_operators = '+-/*'

    if operator not in authorised_operators:
        print('Invalid Operator.')
        continue

    if len(operator) > 1:
        print('Enter only one operator.')
        continue

    # executando a conta
    print('Running your account. Check out the result below:')
    if operator == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operator == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operator == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operator == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('WHATTT????')
    end = input('Are you finished? [y]es: ').lower().startswith('y')

    if end is True:
        break
