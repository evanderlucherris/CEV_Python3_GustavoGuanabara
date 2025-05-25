teste = []
teste.append('Evander')
teste.append(38)
galera = []
galera.append(teste[:])
teste[0] = 'Jéssica'
teste[1] = 34
galera.append(teste[:])
print(teste)
print(galera)
