def analyseur_de_phrase(phrase, limite):
    phrase_nettoiee = phrase.lower().strip()
    liste_mots = phrase_nettoiee.split()

    print("Nombre total de mots est :", len(liste_mots))

    mots_valides = []
    for mot in liste_mots:
        if len(mot) >= limite:
            mots_valides.append(mot)

    return mots_valides


phrase_utilisateur = input("Insérer la phrase : ")
taille_minimale = int(input("Choisir la taille minimale des mots : "))

resultat = analyseur_de_phrase(phrase_utilisateur, taille_minimale)
print(f"Les mots de {taille_minimale} lettres ou plus sont :", resultat)
