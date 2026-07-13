def analyser_verbe_tal(verbe):
    
    regles = {
        "ons": ("nous", "er"),
        "ent": ("ils / elles", "er"),
        "ez": ("vous", "er"),
        "es": ("tu", "er"),
        "e": ("je / il / elle / on", "er"),
        "s": ("je / tu (attention aux exceptions)", "er")
    }
    
    verbe_propre = verbe.lower().strip()
    
    for term, (pronom, suffixe_infinitif) in regles.items():
        if verbe_propre.endswith(term):
            longueur_radical = len(verbe_propre) - len(term)
            radical = verbe_propre[:longueur_radical]
            infinitif = radical + suffixe_infinitif
            return radical, term, pronom, infinitif
            
    return verbe_propre, "inconnue", "inconnu", "inconnu"

mot = input("Veuillez saisir le mot à analyser: ")
racine, fin, sujet, verbe_base = analyser_verbe_tal(mot)
print(f"Mot analysé : {mot} -> Sujet probable : {sujet} | Infinitif : {verbe_base} | terminaison : {fin}")
