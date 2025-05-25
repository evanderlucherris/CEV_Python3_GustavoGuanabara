'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, 
acessíveis por chaves individuais.
'''

num = [2, 5, 9, 1]
num[2] = 3 #MUDA O NÚMERO NA POSIÇÃO 2 DA LISTA(9 POR 3)
num.append(7) #ADICIONA O NUMERO 7 NA AO FINAL DA LISTA
num.sort(reverse=True) #SORT - PÕE A LISTA EM ORDEM/REVERSE - INVERTE A ORDEM DA LISTA
num.insert(2, 2) #INSERE UM VALOR NA POSIÇÃO DA LISTA
num.remove(2) #REMOVE UM ELEMENTO DA LISTA, PROCURANDO A PRIMEIRA OCORRENCIA DA LISTA
if 4 in num: #VERIFICAÇÃO DE UM ELEMENTO DA LISTA
    num.remove(4)
else:
    print('Não achei o número 5')
#num.pop(2) TAMBÉM REMOVE UM ELEMENTO DA LISTA
print(num)
print(f'essa lista tem {len(num)} elementos') #MOSTRA QUANTOS ELEMENTOS TEM NA LISTA