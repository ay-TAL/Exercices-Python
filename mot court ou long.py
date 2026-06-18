def filtrer_mot(mot, limit):
    if len(mot) < limit:
        return 'le mot est trop court'
    else:
        return 'mot valide'

def analyse_saisie():
    ver = input('veuiller saisire un mot: ')
    return ver

def combien():
    cmb = input('veuiller attribuer le nombre: ')
    return cmb

mot_utilisateur = analyse_saisie()
limite_texte = combien()
limite_chiffre = int(limite_texte)

res = filtrer_mot(mot_utilisateur, limite_chiffre)

print(res)
