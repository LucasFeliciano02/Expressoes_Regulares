"""
re.A  = Encontra utilizando a tabela ASCII
re.I  = IGNORCASE
re.M  = Multiline -> aplicado em caracteres ( ^ $ )
re.S  = Dotall
"""

import re

texto = '''
312.544.654-12
534.123.543-54
312.456.653-96
'''

print()

texto2 = 'O João gosta de folia \nE adora ser amado'
print(re.findall(r'^o.*$', texto2, flags=re.I | re.S))  # reconhece quebras de linahs 
