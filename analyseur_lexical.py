import string

def analyseur_de_phrase(phrase):

    phrase_nettoyee = phrase.translate(str.maketrans('', '', string.punctuation))
    mots = phrase_nettoyee.lower().split()
    
    total_mots = len(mots)
    print(f"Le nombre total de mots est : {total_mots}")
    
  
    mots_longs = [mot for mot in mots if len(mot) >= 4]
    
    return mots_longs


phrase_utilisateur = input("Insérez la phrase : ")

resultat = analyseur_de_phrase(phrase_utilisateur)

print("Les mots de 4 lettres ou plus sont :", resultat)
