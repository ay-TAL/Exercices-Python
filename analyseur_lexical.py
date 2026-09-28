def analyseur_de_phrase(phrase):
    
    mots = phrase.lower().split()
    total_mots = len(mots)
    
    print(f"Le nombre total de mots est : {total_mots}")
    
    mots_longs = []
    for mot in mots:
        if len(mot) >= 4:
            mots_longs.append(mot)
            
    return mots_longs

phrase_utilisateur = input('Insérez votre phrase : ')

resultat = analyseur_de_phrase(phrase_utilisateur)

print("Les mots de quatre lettres ou plus sont :", resultat)
