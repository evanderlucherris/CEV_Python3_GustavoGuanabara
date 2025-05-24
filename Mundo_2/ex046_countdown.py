'''
Python Exercise 046:
Write a program that shows a countdown on the screen for a fireworks display, 
going from 10 to 0, with a 1-second pause between each number.
'''

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!')