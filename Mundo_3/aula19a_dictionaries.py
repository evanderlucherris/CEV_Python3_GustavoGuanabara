pessoas = {'Nome': 'Evander', 'Sexo': 'M', 'Idade': 38}
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')