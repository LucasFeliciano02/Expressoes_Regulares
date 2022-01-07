# https://regex101.com/r/ujwiWP/1  =  aonde esta as sentenças 
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

"""
Validando senhas fortes com Positive Lookahead

.*  = qualquer coisa mais
"""

import re

senhas_fortes_regexp = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$', 
    flags=re.M
)

string = '''
VÁLIDAS
2HO_6lX*9kl}
34<:oeWVPp,7
ox4H6n:LM6\~
]6TXdDx .b05
876~}qx>YOCo

SEM MINÚSCULAS
[W9NVX~57=0>
H5BH9]08$;&Y
W}9[8'FLJ<61
G[.4<@BAU853
1K^65M0)}I|U

SEM MINÚSCULAS E NÚMEROS
E?P`WL>R&,A\
W\]+_<NCTV;L
<YN{~K}H#CK-
U[(|C`UN RW`
N^S<~Q>{|DHF

SEM NÚMEROS CARACTERES E MINÚSCULAS
QLDTJDJZJBXT
UJGPQJSVLUSC
DKIDGXJKSIVM
NMETDWHSNABJ
DOUOOJYWLGUP

QUANTIDADE INVÁLIDA (6)
3cv}H9
"g30gY
5X_t8n
)o7H6b
?gJg40
'''

# VAI ENCONTRAR AS SENHAS FORTES EM TODA ESSA STRING
print(senhas_fortes_regexp.findall(string))
