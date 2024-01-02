
def multiplicar(*args):
    result = 1 
    if '0'in args:
        print("Como há um '0' na conta, o resultado é 0")
        return 0
    
    for number in args:
        result *= number
    print(f"The result is {result}")
    return result

multiplicar(9, 7, 5, 8, 10, 900, 33)

def par_impar(*args):
    for number in args:
        if number % 2 == 0:
            print(f"O número ({number}) é par.")
        else:
            print(f'O número ({number}) é impar')

par_impar(100, 37, 2087, 4756654)
        
        