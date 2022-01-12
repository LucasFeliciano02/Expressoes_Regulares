
"""
SEMPRE COMEÇA COM ^$  = COMEÇA COM, TERMINA COM  = Melhora a performance da sua expressao regular

+  =  pode ocorrer mais de uma vez  
\w+  =  Qualquer letra de a-zA-Z0-9  =  aceita letras maiusculas/minusculas e numero
(?:[.\-+%])  =  () Sao as coisas que sao permitidas  e [] pois sao um Conjunto de caracteres
[^\s@]+@  =  Conjunto negado, pode ser qualquer coisa com exceção de um espaço ==  Vai pegar qualquer caracter que 
nao for um espaço e que tenha arroba@
"""


"""

VALIDAÇÃO BÁSICA 1 (valida e é rapida)

https://regex101.com/r/jfaOGY/1

r"^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$

"""


"""

VALIDAÇÃO BÁSICA 2, COM NEGAÇÃO (valida e aceita e aceita palavras acentuadas e não é tão lenta)

https://regex101.com/r/suqA0k/1

r"^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$

"""


"""

PADRÃO RFC 5322 (valida emails e ip e nao valida emails invalidos)
# Padrao de email mesmo, porém nao aceita palavras acentuadas

^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$

https://regex101.com/r/fkxI15/1/

"""


import re

emails = """
Valid email addresses
o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
"email"@example.com
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com


Invalid email addresses
Abc.example.com
<aqui-te-um@email-pra-validar.com.br>
A@b@c@example.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
just"not"right@example.com
this is"not\allowed@example.com
this\ still\"not\\allowed@example.com
plainaddress
#@%^%#$@#$@#.com
@example.com
<email@example.com>
email.example.com
email@example@example.com
.email@example.com
email.@example.com
email..email@example.com
あいうえお@example.com
email@example
email@-example.com
email@example..com
Abc..123@example.com
”(),:;<>[\]@example.com
just”not”right@example.com
this\ is"really"not\allowed@example.com
"""
