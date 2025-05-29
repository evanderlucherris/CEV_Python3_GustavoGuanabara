'''
python exercise 092: create a program that reads name, 
year of birth, and work card, and registers it (with age) in a dictionary. 
if the work card is different from zero, the dictionary will also receive the year of hiring and the salary. 
calculate and add, besides the age, at what age the person will retire.
'''

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-'*30)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')