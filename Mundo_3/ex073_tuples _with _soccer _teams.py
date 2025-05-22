times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino',
         'Ceará SC', 'Bahia', 'Fluminense', 'Corinthians',
         'Atlético MG', 'Botafogo', 'São Paulo', 'Mirassol',
         'Vasco da Gama', 'Fortaleza', 'Internacional', 'EC Vitória',
         'Grêmio', 'Juventude', 'Santos', 'Sport Recife')
print(f'Lista de times de futebol: {times}')
print('='*80)
print(f'Os 5 primeiros são: \n{times[:5]}')
print('='*80)
print(f'Os últimos 4 são: \n{times[-4:]}')
print('='*80)
print(f'Times em ordem alfabética: \n{sorted(times)}')
print('='*80)
print(f'O Grêmio está na {times.index("Grêmio")+1}ª posição')