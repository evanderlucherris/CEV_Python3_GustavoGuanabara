'''
in this lesson, we will learn what dictionaries are and how to use dictionaries in python. 
dictionaries are composite variables that allow storing multiple 
values in a single structure, accessible by literal keys.
'''

pessoas = {'Nome': 'Evander', 'Sexo': 'M', 'Idade': 38}
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*30)
for k in pessoas.keys():
    print(k)
print('-='*30)
for k in pessoas.values():
    print(k)
print('-='*30)
for k in pessoas.items():
    print(k)
print('-='*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)