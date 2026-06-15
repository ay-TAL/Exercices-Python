def filtrer_mot(mot,limit):


     if len(mot) < limit:
        return('est mot trop court ')
     else:
        return('mot valide')

def analyse_saisie():
    ver = input('veuiller saisire un mot: ')   
    return(ver)

def combien():
    cmb = input('veuiller attribuer le nombre: ')
    return(cmb)

res = filtrer_mot(analyse_saisie(),int(combien()))

print(res)