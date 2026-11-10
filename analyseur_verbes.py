def analyser_verbe_tal_avance(verbe: str) -> tuple:
    
    REGLES = {
        "issons": (["nous"], ["ir"]),
        "issez": (["vous"], ["ir"]),
        "issent": (["ils / elles"], ["ir"]),
        "ons": (["nous"], ["er", "re", "oir"]),
        "ent": (["ils / elles"], ["er", "re"]),
        "ez": (["vous"], ["er", "re"]),
        "is": (["je", "tu"], ["ir", "re"]),
        "it": (["il / elle"], ["ir", "re"]),
        "es": (["tu"], ["er"]),
        "e": (["je", "il / elle"], ["er"])
    }

    VERBES_VALIDES = {
        "parler", "manger", "finir", "grandir", "prendre", "voir",
        "vendre", "attendre", "perdre", "rendre", "entendre"
    }
    
    verbe_propre = verbe.lower().strip()
    
    regles_triees = sorted(REGLES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for term, (pronoms, suffixes) in regles_triees:
        if verbe_propre.endswith(term):
            radical = verbe_propre[:-len(term)]
            candidats = []
            for suf in suffixes:
                
                candidat = radical + "dre" if (suf == "re" and radical.endswith("pren")) else radical + suf
                candidats.append(candidat)
            
            valides = [c for c in candidats if c in VERBES_VALIDES]
            infinitifs_proposes = valides if valides else candidats
                        
            return radical, term, " / ".join(pronoms), " / ".join(infinitifs_proposes)
            
    return verbe_propre, "inconnue", "inconnu", "inconnu"

tests = ["parlons", "finissez", "manges", "grandit", "prenons", "rendent"]
for test in tests:
    racine, fin, sujet, verbe_base = analyser_verbe_tal_avance(test)
    print(f"{test.ljust(10)} -> Sujet : {sujet.ljust(15)} | Infinitif : {verbe_base}")

tests = ["parlons", "finissez", "manges", "grandit", "prenons"]
for test in tests:
    racine, fin, sujet, verbe_base = analyser_verbe_tal_avance(test)
    print(f"{test} -> Sujet : {sujet} | Infinitif proposé : {verbe_base}")
