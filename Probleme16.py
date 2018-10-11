def somme_digits(n):
    nombre=str(n)
    somme=0
    for x in nombre :
        somme+=int(x)
    return somme

assert somme_digits(2**15) == 26
print(somme_digits(2**1000))
        
