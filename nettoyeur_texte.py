import nltk
from nltk.corpus import stopwords


def nettoyer_mon_texte(phrase_brute):
    mots_inutiles = stopwords.words("french")
    phrase_propre = []

    mots_decoupes = nltk.word_tokenize(phrase_brute)

    for word in mots_decoupes:
        texte = word.lower().strip()
        if texte not in mots_inutiles:
            phrase_propre.append(texte)

    return phrase_propre


texte_test = input("Insérer votre texte à nettoyer : ")
resultat = nettoyer_mon_texte(texte_test)

print("\nRésultat final de votre liste :")
print(resultat)