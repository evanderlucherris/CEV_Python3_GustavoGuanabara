'''
Create a Python code that tests whether the **Pudim** website is accessible from the computer being used.
'''
import urllib
import urllib.request

try:
    response = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('O site Pudim está acessível!')