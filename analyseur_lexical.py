import sys
from typing import Final

PONCTUATION_A_NETTOYER: Final[set[str]] = set(".,;:!?()[]{}«»'\"_-\n\r\t")


def nettoyer_et_decouper(texte: str, caracteres_a_exclure: set[str]) -> list[str]:
    """Nettoie la ponctuation d'un texte et le découpe en mots isolés."""
    texte_nettoye = "".join(" " if c in caracteres_a_exclure else c for c in texte)
    return texte_nettoye.lower().split()


def filtrer_mots_par_taille(mots: list[str], limite_taille: int) -> list[str]:
    """Filtre une liste de mots pour ne garder que ceux atteignant la taille minimale.

    Utilise une compréhension de liste (List Comprehension) pour des performances optimales.
    """
    return [mot for mot in mots if len(mot) >= limite_taille]


def recuperer_limite_securisee() -> int:
    """Demande la taille minimale à l'utilisateur et sécurise la conversion en entier."""
    while True:
        try:
            return int(input("Choisir la taille minimale des mots : "))
        except ValueError:
            print("[Erreur] Veuillez entrer un nombre entier valide.", file=sys.stderr)


def main() -> None:
    """Point d'entrée du programme orchestrant la logique applicative."""
    try:
        phrase_utilisateur = input("Insérer la phrase : ").strip()
        taille_minimale = recuperer_limite_securisee()
    except (KeyboardInterrupt, EOFError):
        print("\n[Info] Programme interrompu par l'utilisateur.", file=sys.stderr)
        sys.exit(0)

    tous_les_mots = nettoyer_et_decouper(phrase_utilisateur, PONCTUATION_A_NETTOYER)
    print(f"\nNombre total de mots détectés : {len(tous_les_mots)}")

    mots_valides = filtrer_mots_par_taille(tous_les_mots, taille_minimale)

    print(f"Les mots de {taille_minimale} lettres ou plus sont : {mots_valides}")


if __name__ == "__main__":
    main()
