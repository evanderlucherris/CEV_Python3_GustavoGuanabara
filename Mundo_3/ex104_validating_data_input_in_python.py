'''
Create a program that has a function called **readInt()**, 
which will work similarly to Python’s **input()** function, 
but with validation to accept only a numeric value.
Example: `n = readInt('Enter a number: ')`
'''
def leiaInt(msg):
    """
    Lê um número inteiro com validação.
    
    :param msg: mensagem a ser exibida no input
    :return: valor inteiro digitado pelo usuário
    """
    while True:
        valor = input(msg)
        if valor.strip().lstrip('-').isdigit():  # aceita números negativos também
            return int(valor)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
