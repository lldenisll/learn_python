def maiusculas(frase):
    import re
    x=re.findall('[A-Z]',frase)
    y=''.join((x))
    return(y)


print(maiusculas('Programamos em python 2?'))
print(maiusculas('Programamos em Python 3.'))
print(maiusculas('PrOgRaMaMoS em python!'))