'''
Python Exercise 037:
Write a Python program that reads any integer and asks the user to choose the base for conversion: 
1 for binary, 2 for octal, and 3 for hexadecimal.
'''

num = int(input('Digite um número inteiro: '))
print('''Digite uma das bases para conversão:
      [ 1 ] Converter para BINÁRIO.
      [ 2 ] Converter para OCTAL.
      [ 3 ] Converter para HEXADECIMAL.''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente.')