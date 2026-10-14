exceptions = {
    "souris": "singulier",
    "bus": "singulier",
    "choix": "singulier",
    "prix": "singulier",
    "nez": "singulier",
    "gaz": "singulier",
}

termine = ("s", "x", "z")


def analyser_nombre_mot(word):
    word = word.lower().strip()

    if word in exceptions:
        return "ce mot est au singulier"

    if word.endswith(termine):
        return "ce mot est au pluriel"

    return "ce mot est au singulier"


resultat = analyser_nombre_mot(input("Quel est le mot : "))
print(resultat)
