def analyser_verbe(verbe):

    terminaisons = ["ons", "ent", "ez", "e", "es", "s"]
    verbe_propre = verbe.lower().strip()

    for term in terminaisons:
        if verbe_propre.endswith(term):
            longueur_radical = len(verbe_propre) - len(term)
            radical = verbe_propre[:longueur_radical]
            return radical, term

    return verbe_propre, "inconnue"


mot_saisi = input("Entrez un verbe du 1er groupe conjugué au présent : ")
racine, fin = analyser_verbe(mot_saisi)

print("Radical : " + racine)
print("Terminaison : " + fin)