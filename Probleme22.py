def name_scores() :
    def ListNoms(f):
        #créer la liste des noms contenus dans le fichier 
        L=[]
        for e in f :
            L.append(e)
        return L[0].split(',')
    def tri(ListNoms):
        #tri par ordre alphabétique les noms contenus dans la liste
        for i in range(len(ListNoms)):
            ListNoms[i]=ListNoms[i].replace('"','')
        return (sorted(ListNoms))
    def score(nom):
        #renvoit le score d'un nom
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        score=0
        for x in nom :
            for i in range(0,len(alphabet)):
                if x == alphabet[i] :
                    score+=i+1  
        return score
    f=open('p022_names.txt','r')
    score_total=0 
    ListNomstries=tri(ListNoms(f))
    for i in range (0,len(ListNomstries)):
        nom=ListNomstries[i]
        score_total += (i+1)*score(nom)
    return score_total

print(name_scores())      
