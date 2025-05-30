def contador(*num):
    s = 0
    for v in num:
        s += v
    print(f'Somando os valores {num} temo {s}')
    #tam = len(num)
    #print(f'Recebi os valores {num} e são ao todo {tam} números.')
    #for valor in num:
        #print(f'{valor} ', end='')
    #print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)