def ehPrimo(k):
    fator=2
    while k % fator !=0 and fator <= k/2:
       fator=fator+1
    if k%fator == 0:
        return False
    else:
        return True

def maior_primo(x):
    primo = x
    i = 0
    while i <= x:
        if ehPrimo(i):
            primo = i
        i = i + 1
    return primo
