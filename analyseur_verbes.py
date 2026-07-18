def analyser_verbe_tal_avance(verbe):
    regles = {
        "issons": ("nous", "ir"),
        "issez": ("vous", "ir"),
        "issent": ("ils / elles", "ir"),
        "ons": ("nous", "er / re / oir"),
        "ent": ("ils / elles", "er / re"),
        "ez": ("vous", "er / re"),
        "is": ("je / tu", "ir / re"),
        "it": ("il / elle", "ir / re"),
        "es": ("tu", "er"),
        "e": ("je / il / elle", "er")
    }

    VERBES_VALIDES = {
        "parler", "manger", "finir", "grandir", "prendre", "voir",
        "vendre", "attendre", "perdre", "rendering", "entendre"
    }
    
    verbe_propre = verbe.lower().strip()
    
    regles_triees = sorted(regles.items(), key=lambda x: len(x[0]), reverse=True)
    
    for term, (pronom, suffixe_infinitif) in regles_triees:
        if verbe_propre.endswith(term):
            longueur_radical = len(verbe_propre) - len(term)
            radical = verbe_propre[:longueur_radical]
            
            liste_suffixes = suffixe_infinitif.split(" / ")
            infinitifs_proposes = []
            
            for suf in liste_suffixes:
                if suf == "re" and radical.endswith("pren"):
                    candidat = radical + "dre"
                else:
                    candidat = radical + suf
                
                if candidat in VERBES_VALIDES:
                    infinitifs_proposes.append(candidat)
            
            if not infinitifs_proposes:
                for suf in liste_suffixes:
                    if suf == "re" and radical.endswith("pren"):
                        infinitifs_proposes.append(radical + "dre")
                    else:
                        infinitifs_proposes.append(radical + suf)
                        
            infinitif = " / ".join(infinitifs_proposes)
            return radical, term, pronom, infinitif
            
    return verbe_propre, "inconnue", "inconnu", "inconnu"

tests = ["parlons", "finissez", "manges", "grandit", "prenons"]
for test in tests:
    racine, fin, sujet, verbe_base = analyser_verbe_tal_avance(test)
    print(f"{test} -> Sujet : {sujet} | Infinitif proposé : {verbe_base}")
