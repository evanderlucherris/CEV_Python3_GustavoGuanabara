'''cidade = str(input('Em que cidade você nasceu? '))
print('santo' in cidade.lower().split())'''

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')