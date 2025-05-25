valores = [] #CRIA UMA LISTA VAZIA
for cont in range(0, 5): 
    valores.append(int(input('Digite um valor: '))) #COOMANDO PARA INSERIR VALORES NA LISTA POR INTERAÇÃO

for c, v in enumerate(valores): #ENCONTRA A CHAVE/POSIÇÃO NA LISTA
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')