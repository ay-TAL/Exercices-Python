def filtrer_mot(mot: str, limite: int) -> str:
    """Vérifie si la longueur du mot atteint la limite fixée."""
    if len(mot) < limite:
        return 'Le mot est trop court'
    return 'Mot valide'

def obtenir_saisie() -> str:
    return input('Veuillez saisir un mot : ').strip()

def obtenir_limite() -> int:
    while True:
        try:
            return int(input('Veuillez attribuer un nombre limite : '))
        except ValueError:
            print("Erreur : Veuillez entrer un chiffre valide.")

if __name__ == "__main__":
    mot_utilisateur = obtenir_saisie()
    limite_chiffre = obtenir_limite()
    
    resultat = filtrer_mot(mot_utilisateur, limite_chiffre)
    print(resultat)
