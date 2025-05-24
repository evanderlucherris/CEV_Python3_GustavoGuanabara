'''
Python Exercise 042:
Redo CHALLENGE 35 about triangles, adding the feature to show what type of triangle will be formed:
EQUILATERAL: all sides equal
ISOSCELES: two sides equal, one different
SCALENE: all sides different
'''

print('-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end=' ')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')