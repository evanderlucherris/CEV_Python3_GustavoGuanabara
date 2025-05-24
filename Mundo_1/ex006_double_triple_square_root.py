'''
Python Exercise 006:
Create an algorithm that reads a number and shows its double, triple, and square root.
'''

n = int(input('Digite um valor: '))
print('O dobro {} vale {}, \no triplo {} vale {}, \na raiz quadrada de {} vale {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))