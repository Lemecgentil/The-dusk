#!/usr/bin/env python3
"""Une lettre (« a ») qui renaît dix fois, chaque vie durant un quart d'heure.

Usage :
    python3 lettre_renaissante.py                 # 10 vies de 15 minutes (2 h 30 au total)
    python3 lettre_renaissante.py --duree 5       # vies de 5 secondes (pour tester)
    python3 lettre_renaissante.py --lettre b --vies 3
"""

import argparse
import sys
import time

QUART_D_HEURE = 15 * 60  # secondes


def formater(secondes: int) -> str:
    minutes, sec = divmod(max(0, secondes), 60)
    return f"{minutes:02d}:{sec:02d}"


def vivre(lettre: str, numero: int, total: int, duree: float) -> None:
    """Fait vivre la lettre pendant `duree` secondes, avec un compte à rebours."""
    print(f"\n✨ Renaissance {numero}/{total} : « {lettre} » revient à la vie.")
    fin = time.monotonic() + duree
    while True:
        restant = fin - time.monotonic()
        if restant <= 0:
            break
        sys.stdout.write(f"\r   {lettre}   — temps restant {formater(int(restant + 0.999))} ")
        sys.stdout.flush()
        time.sleep(min(1, restant))
    sys.stdout.write(f"\r   {lettre}   — temps restant {formater(0)} \n")
    print(f"🕯️  La lettre « {lettre} » s'éteint (vie {numero}).")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--lettre", default="a", help="lettre à faire renaître (défaut : a)")
    parser.add_argument("--vies", type=int, default=10, help="nombre de renaissances (défaut : 10)")
    parser.add_argument(
        "--duree", type=float, default=QUART_D_HEURE,
        help="durée de chaque vie en secondes (défaut : 900 = un quart d'heure)",
    )
    args = parser.parse_args()

    try:
        for i in range(1, args.vies + 1):
            vivre(args.lettre, i, args.vies, args.duree)
    except KeyboardInterrupt:
        print("\n⏹️  Cycle interrompu.")
        return
    print(f"\nLa lettre « {args.lettre} » a vécu ses {args.vies} vies. Fin du cycle.")


if __name__ == "__main__":
    main()
