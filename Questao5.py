'''
Poderia apenas colocar invertida = palavra[::-1], porém achei que fazer com laço seria mais justo
dado o objetivo do teste.
'''

palavra = input()
invertida = ''
n = len(palavra)-1
while n >= 0:
    invertida += palavra[n]
    n-=1
print(invertida)