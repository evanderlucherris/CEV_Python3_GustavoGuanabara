'''
Python Exercise 059:
Create a program that reads two values and shows a menu on the screen:
[ 1 ] add
[ 2 ] multiply
[ 3 ] find the greater
[ 4 ] enter new numbers
[ 5 ] exit the program
Your program should perform the requested operation in each case.
'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! volte sempre!')