def remplissage(annee):
    cal={}
    jour="Vendredi"
    for i in range(annee+1):
        x='annee'+str(i)
        cal[x]={"Janvier":{},"Février":{},"Mars":{},"Avril":{},"Mai":{},"Juin":{},"Juillet":{},"Aout":{},"Septembre":{},"Octobre":{},"Novembre":{},"Décembre":{}}

        sem=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
        o=0
        liste=list(cal[x])
        while o<12:
            if o in [0,2,4,6,7,9,11]:
                u=31
            elif o==1 and i%4==0:
                u=29
            elif o==1:
                u=28
            elif o in [3,5,8,10]:
                u=30
            for y in range(len(sem)):
                if sem[y]==jour:
                    dep=y
            for f in range(u):
                cal[x][liste[o]][f]=sem[dep]
                if dep<6:
                    dep+=1
                    jour=sem[dep]
                else:
                    dep=0
                    jour=sem[dep]
            o+=1
    return cal

test=remplissage(2042)

def jour(jour,mois,année,dic):
    real='annee'+str(année)
    mois1=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
    print(dic[real][mois1[mois-1]][jour-1])

def mois(mois,année,dic):
    mois1=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
    real='annee'+str(année)
    print(dic[real][mois1[mois-1]])

def annee(année,dic):
    real='annee'+str(année)
    print(dic[real])

jour(13,4,2042,test)