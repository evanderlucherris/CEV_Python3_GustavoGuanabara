'''
Python Exercise 024:
Create a program that reads the name of a city and tells if it starts with the name "SANTO" or not.
'''

'''cidade = str(input('Em que cidade você nasceu? '))
print('santo' in cidade.lower().split())'''

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')