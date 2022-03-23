def cripto(frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa": tradutor = tradutor + "@" 
        elif letra in "Bb": tradutor = tradutor + "#"
        elif letra in "Cc": tradutor = tradutor + "?"
        elif letra in "Dd": tradutor = tradutor + "X"
        elif letra in "Ee": tradutor = tradutor + "$"
        elif letra in "Ff": tradutor = tradutor + "!"
        elif letra in "Ll": tradutor = tradutor + "&"
        elif letra in "Uu": tradutor = tradutor + "%" 
        else: tradutor = tradutor + letra
    return tradutor
            
print(cripto(input('Digite sua frase:')))
