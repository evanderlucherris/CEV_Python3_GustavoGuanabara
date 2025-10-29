'''
Create a mini-system that uses Python’s **Interactive Help**. 
The user will type a command, and the manual will appear. 
When the user types the word **‘END’**, the program will terminate. 
Important: use colors.
'''
def ajuda():
    """
    Mini-sistema de ajuda interativa do Python.
    """
    from time import sleep

    while True:
        print('\033[1;34m~' * 30)
        print('\033[1;33mSISTEMA DE AJUDA PYTHON\033[m')
        print('\033[1;34m~' * 30)
        comando = input('\033[1;32mFunção ou Biblioteca > \033[m').strip()
        if comando.upper() == 'FIM':
            print('\033[1;31mEncerrando o sistema... Até mais!\033[m')
            break
        print('\033[1;35m~' * 30)
        print(f'\033[1;36mAcessando o manual de {comando}\033[m')
        print('\033[1;35m~' * 30)
        sleep(0.5)
        help(comando)
        print('\033[1;34m~' * 30)

# Executa o mini-sistema
ajuda()
