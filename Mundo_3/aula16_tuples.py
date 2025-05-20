lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis
# lanche[1] = 'Refrigerante' NÃO É POSSIVEL SUBSTITUIR VALORES EM TUPLAS.

for cont in range(0, len(lanche)):
    #print(cont) #SE QUISER CONTAR DE FORMA SIMPLES
    print(f'Eu vou comer {lanche[cont]}') #AQUI MOSTRA O VALORES NA TUPLA
print('Comi pra caramba!')
print('-'*50) #SEPARANDO OS EXEMPLOS

print(len(lanche)) #VAI CONTAR OS VALORES DENTRO DA TUPLA E IMPRIMIR
print('-'*50)

for comida in lanche: #FOR DE MANEIRA SIMPLES
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print('-'*50)

for pos, comida in enumerate(lanche): #ESSE FOR MOSTRA OS VALORES E A POSIÇÃO NA TUPLA
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
print('-'*50)

print(sorted(lanche)) #CRIOU UMA LISTA E COLOCOU EM ORDEM ALFABÉTICA
print(lanche)