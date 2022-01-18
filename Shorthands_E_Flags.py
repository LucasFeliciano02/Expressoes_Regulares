"""
MINUSCULO = ENCONTRA
MINUSCULO = NEGAÇÃO
"""

# \w  ->  [a-zA-Z0-9À-ú_]  =  encontra tds esse tipos de palavras com esses termos (MAIS USADO)
# \w  ->  [a-zA-Z0-9_] ->  re.A  = nao pega as palavras acentuadas
# \W  ->  [^a-zA-Z0-9_]  - W Maiusculo == negação
# \d  -> [0-9]  = encontra digitos entre 0 a 9
# \D  -> [^0-9]  = contrario, encontra nada de nenhum numero de 0-9, encontra tudo exeto numeros
# \s  -> [ \r\n\f\n\t]  =   qualquer tipo de espaço
# \b  = borda  == Vai encontrar uma string vazia no começo ou no fim de cada palavra
# \B  = nao borda

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print()

print(re.findall(r'\w+', texto, flags=re.A))  # Encontra palavras com e sem acento
print(re.findall(r'\W+', texto, flags=re.I))  # encontra o inverso, apenas pontuação
print()
print(re.findall(r'\d+', texto, flags=re.I))  # encontra Somente os numeros do texto
print(re.findall(r'\D+', texto, flags=re.I))  # encontra tudo exeto numeros
print()
print(re.findall(r'\s+', texto, flags=re.I))  # encontra os espaços do texto, quebras de linha = \n
print(re.findall(r'\S+', texto, flags=re.I))  # encontra Tudo menos espaço
print()
print(re.findall(r'\be\w+', texto, flags=re.I))  # Busca palavras Completas que começam com a letra 'e'
print(re.findall(r'\w+e\b', texto, flags=re.I))  # Traz apenas palavras quie terminam com a letra 'e'
print()
print(re.findall(r'\b\w{4}\b', texto, flags=re.I))  # Traz apenas palavras com 4 letras (sem a borda \b as palavras ficam cortadas)
