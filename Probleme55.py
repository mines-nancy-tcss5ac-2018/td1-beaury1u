def Lychrel_Numbers(n):
    def palindrome(nombre):
        #test si un nombre est un palindrome
        chaine=str(nombre)
        i , longueur_chaine = 0 , len(chaine)
        while i < longueur_chaine/2 :
            if chaine[i] == chaine[longueur_chaine-i-1] :
                i+=1
            else :
                return False
        return True
    def inversion(chaine):
        #retourne la chaine inversée d'une chaine de caractère
        chaine_inverse=''
        for lettre in reversed(chaine):
            chaine_inverse +=lettre
        return chaine_inverse
    def Is_Lychrel(p) :
        #test si un nombre est un nombre de Lychrel
        for i in range(1,51):
            chaine=str(p)
            p=int(chaine)+int(inversion(chaine))
            if palindrome(p) :
                return False
        return True
    Nombres_Lychrel = 0
    for p in range(0,n+1):
        if Is_Lychrel(p) :
            Nombres_Lychrel+=1
    return Nombres_Lychrel


print(Lychrel_Numbers(10000))