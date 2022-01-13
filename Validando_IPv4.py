"""
# VALIDANDO CPF E IP

IP  =  0.0.0.0.255.255.255.255  -> CADA CASA DO IP É UM NUMERO INTEIRO, PODENDO TER VARIAS COMBINAÇOES
CPF =  321.323.443-10   

^$  =  vai validar o campo precisamente, se tiver um espaço, letra antes, nao vai validar
começa com, termina com

"""
import re

print()

# VALIDANDO CPF
cpf = '321.323.443-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
print(cpf_reg_exp.search(cpf))


# VALIDANDO IP

# MANEIRA MAIS PRECISA PARA MONTAR UMA EXPRESSAO REGULAR

ip_reg_exp = re.compile(r'''
    ^
    (?:
        25[0-5]|  # range de 250-255
        2[0-4][0-9]| # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \.    
    (?:
        25[0-5]|  # range de 250-255
        2[0-4][0-9]| # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \.     
    (?:
        25[0-5]|  # range de 250-255
        2[0-4][0-9]| # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    \. 
    (?:
        25[0-5]|  # range de 250-255
        2[0-4][0-9]| # 200-249
        1[0-9]{2}|  # 100-199
        [1-9][0-9]|  # 10-99
        [0-9]  # 0-9
    )
    
    
    # MESMA COISA QUE OS DE CIMA SO QUE MENOR E REPETINDO AS MESMAS COISAS
    # PRA FUNCIONAR TEM QUE DAR Ctrl + x nas funções de cima
    
    ^
    (?:
        (?:
            25[0-5]|  
            2[0-4][0-9]| 
            1[0-9]{2}|  
            [1-9][0-9]|  
            [0-9]
        )
        \.?  
    ){4}
    \b
    $
''', flags=re.X)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
    