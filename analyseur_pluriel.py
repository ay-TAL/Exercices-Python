EXCEPTIONS = {
    "souris",
    "bus",
    "choix",
    "prix",
    "nez",
    "gaz",
}

TERMINAISONS_PLURIEL = ("s", "x", "z")


def analyser_nombre_mot(mot: str) -> str:
    """Détermine si un mot donné est au singulier ou au pluriel.

    Args:
        mot (str): Le mot à analyser.

    Returns:
        str: Une phrase indiquant le nombre du mot ("singulier" ou "pluriel").
    """

    mot_nettoye = mot.lower().strip()

    if not mot_nettoye:
        return "Erreur : Le texte saisi est vide."


    if mot_nettoye in EXCEPTIONS:
        return f"Le mot '{mot}' est au singulier."


    if mot_nettoye.endswith(TERMINAISONS_PLURIEL):
        return f"Le mot '{mot}' est au pluriel."

    return f"Le mot '{mot}' est au singulier."



if __name__ == "__main__":
    saisie_utilisateur = input("Quel est le mot : ")
    resultat = analyser_nombre_mot(saisie_utilisateur)
    print(resultat)
