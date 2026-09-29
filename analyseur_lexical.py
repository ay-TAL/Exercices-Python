def analyser_phrase(phrase: str) -> list[str]:
    """Nettoie la phrase sans RegEx et filtre les mots de 4 lettres ou plus."""

    ponctuation = ".,;:!?()[]{}«»'\"-_"
    
    phrase_nettoyee = "".join(c if c not in ponctuation else " " for c in phrase)
    

    mots = phrase_nettoyee.lower().split()
    

    return [mot for mot in mots if len(mot) >= 4]


if __name__ == "__main__":
    phrase_utilisateur = input("Insérez la phrase : ")
    
    mots_filtrés = analyser_phrase(phrase_utilisateur)
    
    print(f"\nNombre de mots de 4 lettres ou plus : {len(mots_filtrés)}")
    
    print("Les mots retenus sont :", mots_filtrés)
